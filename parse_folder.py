import datetime
# import pandas as pd
# import numpy as np
import os
import itertools
import configparser
import helper as hlp
import re
import sys
import webbrowser
import subprocess as sp
import webbrowser as wb
# import requests
orig_dir = os.getcwd()
phq = '/Users/sammyoge/photo_hq'
folder_path = '/Volumes/NIKON D850 /DCIM/115ND850'

config = configparser.ConfigParser()
config.read(phq + 'phq.cfg')

def read_files(path=None):

    folder = path or orig_dir

    data = list(filter(len,os.popen("ls | xargs stat -f '%SB %N' -t'%m-%d-%y'").read().split('\n')))

    return

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
os.system(command)

