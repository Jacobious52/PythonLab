#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jacob Gonzalez
# @Date:   2015-07-27 20:24:52
# @Last Modified by:   Jacob Gonzalez
# @Last Modified time: 2015-07-27 23:05:54

mods = ('private:', 'public:', 'protected:', '};', 'property:', 'readonly:')

def load_lines(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line)
    return lines;

def modifier_range(mod, lines):
    start = -1
    end = -1
    for i in xrange(0,len(lines)):
        line = lines[i].strip()
        if line == mod:
            start = i
        elif start != -1 and end == -1:
            if any(line == m and line != mod for m in mods):
                end = i
    return (start, end)

def generate_property(i, type, name, lines):
    lines.insert(i+1, '\t// getter/setter for %s _%s\n' % (type, name))
    lines.insert(i+2, '\t%s get_%s() const;\n' % (type, name))
    lines.insert(i+3, '\tvoid set_%s(%s %s);\n' % (name, type, name))
    lines.insert(i+4, '\n')
    return (lines, 4)

def generate_readonly(i, type, name, lines):
    lines.insert(i+1, '\t// readonly getter for %s _%s\n' % (type, name))
    lines.insert(i+2, '\t%s get_%s() const;\n' % (type, name))
    lines.insert(i+3, '\n')
    return (lines, 3)

def create_properties(mod_range, lines, generator):
    i = mod_range[0]
    if i == -1:
        return lines
    del lines[i]
    end = mod_range[1]-1
    while i < end:
        line = lines[i].strip().replace(';', ' ')
        print i
        print line
        if line != '':
            parts = line.split(' ')
            print parts
            if len(parts) == 3:
                del lines[i]
                i-=1
                type = parts[0]
                name = parts[1]
                lines, step = generator(i, type, name, lines)
                i+=step
                end+=step-1
                priv_range = modifier_range(mods[0], lines)
                if priv_range != (-1, -1):
                    lines.insert(priv_range[0]+1, '\t%s %s;\n' % (type, name))
        i+=1
    return lines

def modify_file(filename):
    lines = load_lines(filename)

    #properties
    mod_prop_range = modifier_range(mods[-2], lines)
    print mod_prop_range
    lines = create_properties(mod_prop_range, lines, generate_property)

    #readonly
    mod_read_range = modifier_range(mods[-1], lines)
    print mod_read_range
    lines = create_properties(mod_read_range, lines, generate_readonly)

    with open('_%s' % filename, 'w') as f:
        for l in lines:
            f.write(l)


def main():
    modify_file('modtest.cpp')

if __name__ == '__main__':
    main()
