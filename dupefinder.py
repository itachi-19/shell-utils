#!/bin/python

# itachi-19 

import subprocess as sp
import sys
import os

class File:
    #TODO
    # 'size': size,
    # 'filename': filename,
    # 'folder': folder,
    # 'extension', 
    pass

printf = lambda x: print(x.decode('utf-8'), end="")
path = '/home/itachi/coding/'
query = r'%p\t%s\n'
#command = f'find {path} -type f printf p\''
# print(command)
#sys.exit(0)
proc = sp.run(['find', path, '-type', 'f', '-printf', '%p\\t%s\\0'], capture_output=True,text=True)
lines = proc.stdout.split('\0')

filepath_map = {}
file_map = {}

for line in lines:
    if not line: continue
    filepath, size = line.split('\t')
    # absfilepath =  os.path.abspath(filepath)
    file = filepath #TODO modify
    filename = filepath.split('/')[-1]
    filepath_map[file] =  {
            'size': size,
            'filename': filename,
            # TODO
            # 'folder': folder,
            # 'extension', 
    }

    if filename not in file_map:
        file_map[filename] = []
    file_map[filename].append(filepath)



f = lambda y: print(file_map[y])

f('countwatch.sh')
f('shop.md')
