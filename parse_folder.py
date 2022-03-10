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
phq = '/Users/sammyoge/photo_hq/'
folder_path = '/Volumes/NIKON D850 /DCIM/115ND850'

config = configparser.ConfigParser()
config.read(phq + 'phq.cfg')

def client(ctype=None):
    config = configparser.ConfigParser()
    config.read(phq + 'phq.cfg')

    if ctype == 'sd':
        return config['PATHS']['sd_path']
    elif ctype == 'x3':
        return config['PATHS']['bythree_dest_path']
    elif ctype == 'rwci':
        return config['PATHS']['rwci_dest_path']
    else:
        return input('Enter desired directory:') or '/Users/sammyoge/photo_hq/'

def read_files(path=None):
    """

    :param path (str): Folder path.
    :return:
    """

    folder = path or orig_dir

    data = sp.run("ls | xargs stat -f '%SB %N' -t'%m-%d-%y'",
                  cwd=folder, shell=True,capture_output=True, text=True ).stdout
    d = list(filter(len,data.split('\n')))

    return d

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


def form(data,sep=' '):

    return '{}'.format(sep).join(data)


def run(to=None,fr=None):
    """
    :param data (list): List of files with date information.
    :return:
    """

    src = client(fr)
    print('Reading contents of %s' % src)

    dest = client(to)
    print('Writing contents of %s to %s' % (src,dest))

    data = read_files(path=src)
    content = files_dict(data)
    catalog = form(list(content.keys()))
    print(catalog)
    cmd1 = 'mkdir %s' % catalog
    sp.run(cmd1, cwd=dest, shell=True)
    print(content)
    #cmd1 = 'mkdir {%s}' % ','.join(list(catalog.keys()))

    [sp.run('cp {f} {d}'.format(f=form(content[k]), d=dest + k), cwd=src,
            shell=True) for k in list(content.keys())]

    wb.open('file:///' + dest)
    #os.mkdir('{%s}' % dest)


# dest = '/Users/sammyoge/photo_temp/' + list(files.keys())[7]
# os.mkdir('%s' % dest)
# command = 'cp {f} {d}'.format(f=docs,d=dest)
# os.system(command)