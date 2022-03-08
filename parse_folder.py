import datetime
# import pandas as pd
# import numpy as np
import os
import itertools
import re
import sys
import webbrowser
import subprocess as sp
import webbrowser as wb
# import requests
orig_dir = os.getcwd()
folder_path = '/Volumes/NIKON D850 /DCIM/115ND850'


# def mftf(src,dest,data):
#     """
#     Move Files to specified folder.
#     :param: None
#     :return:
#     """
#
#     # if not set_dir(src):
#     #     print('Source Folder does not exist')
#     #     return
#     #
#     # if not os.path.isdir(dest):
#     #     print('Creating directory TEMP folder in %s...' % src)
#     #     os.mkdir('%s' % dest)
#
#
#     command = "ls -l | cut -w -f 6,7,9"
#     # print("Moving {f} to {d}".format(f= ', '.join(data.split(' ')),d=dest))
#     # #print(command)
#     # os.system(command)
#     # set_dir(reset=True)
#     # print('Done!')
#
#     os.popen(command).read().split('\n'))

# Lists all files in folder in long format (displaying file details) and cuts
# results by consecutive whitespaces and choosing which columns to keep.
# Final result is converted into a list.

data = list(filter(len,os.popen('ls -l | cut -w -f 6,7,9').read().replace('\t',' ').split('\n')))

key_func = lambda x: x[0:6]

files = {}

for key, value in itertools.groupby(data,key_func):
    files[key.rstrip(' ').replace(' ','_')] = [i.replace('{}'.format(key),'').lstrip(' ') for i in list(value)]

if not os.path.isdir(dest):
    print('Creating directory TEMP folder in %s...' % src)
    os.mkdir('%s' % dest)



files[list(files.keys())[0]]

docs = ' '.join(files[list(files.keys())[7]])

dest = '/Users/sammyoge/photo_temp/' + list(files.keys())[7]
os.mkdir('%s' % dest)
command = 'cp {f} {d}'.format(f=docs,d=dest)


