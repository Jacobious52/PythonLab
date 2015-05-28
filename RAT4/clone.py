from os import mkdir, path
from colors import colors

FILES = 'file'
FOLDERS = 'dir'

def items_in(d, sock, cmd):
	sock.send('%s&%s' % (cmd, d))
	d_list = sock.recv().split('\n')
	sock.recv()
	for d in d_list:
		if d == '':
			d_list.remove(d)
		elif not d:
			d_list.remove(d)
		elif d.startswith('.'):
			d_list.remove(d)
		elif d.startswith('~'):
			d_list.remove(d)
	return d_list

def clone_folder(name):
	try:
		if not path.exists(name):
			mkdir(name)
	except:
		print(colors.FAIL + ('failed: %s' % name) + colors.ENDC)

def clone_file(name):
	try:
		open(name, 'a').close()
	except:
		print(colors.FAIL + ('failed: %s' % name) + colors.ENDC)
	

def clone_all(current, root, sock):
	for d in items_in(current, sock, FOLDERS):
		if d == 'Directory not found' or d == 'waiting' or d == 'timeout from server':
			print(colors.WARNING + ('%s not found' % current) + colors.ENDC)
			print('skipping')
			continue
		mac_full_d = '%s/%s' % (current, d)
		windows_full_d = mac_full_d
		mac_full_d = mac_full_d.replace(root, 'Clone')
		if mac_full_d.endswith('////'):
			break
		clone_folder(mac_full_d)
		print(colors.OKGREEN + ('cloned: %s' % mac_full_d) + colors.ENDC)
		for f in items_in(windows_full_d, sock, FILES):
			if f == 'Directory not found' or d == 'waiting' or d == 'timeout from server':
				print(colors.WARNING + ('%s not found' % d) + colors.ENDC)
				print('skipping')
				continue
			mac_full_f = '%s/%s' % (windows_full_d, f)
			mac_full_f = mac_full_f.replace(root, 'Clone')
			clone_file(mac_full_f)
			print(colors.OKGREEN + ('cloned: %s' % mac_full_f) + colors.ENDC)
		clone_all(windows_full_d, root, sock)

def clone_from(top, sock):
	clone_folder('Clone')
	clone_all(top, top, sock)