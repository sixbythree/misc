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

# Lists the date and filename for each file in folder
# Final result is converted into a list.

data = list(filter(len,os.popen("ls | xargs stat -f '%SB %N' -t'%m-%d-%y'").read().split('\n')))

def files_dict(data):
    """
    Creates dictionary for data where key is file creation date and values are list of files of key date.
    Data must be in 'MM-DD-YY <FILE>' Format.

    :param data (list): List of files with date information.
    :return:
    """

    files = {}
    key_func = lambda x: x[0:8]

    for key, value in itertools.groupby(data,key_func):
        files[key] = [i.replace('{}'.format(key),'').lstrip(' ') for i in list(value)]

    return files

def files_of(data, key):

    files = ' '.join(data[key])

    return files

dest = '/Users/sammyoge/photo_temp/' + list(files.keys())[7]
os.mkdir('%s' % dest)
command = 'cp {f} {d}'.format(f=docs,d=dest)


