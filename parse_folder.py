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

# Paths
# A. parse_folder folder path
# B. photo_hq folder path
# C. sd folder path

orig_dir = os.getcwd()  # A.
phq = '/Users/sammyoge/photo_hq/'  # B.
folder_path = '/Volumes/NIKON D850 /DCIM/115ND850'  # C.

# Config
# A. creating global config object
# B. reading phq.cfg file

config = configparser.ConfigParser()  # A.
config.read(phq + 'phq.cfg')  # B.


def client(ctype=None, c=False):
    """

    :param reset (False): Boolean to reset cwd to original directory (orig_dir).
    :return:


    Description:

    A. creating local config object.
    B. reading phq.cfg file into config object.
    """

    config = configparser.ConfigParser()  # A.
    config.read(phq + 'phq.cfg')

    if c==True:
        folder = ctype or input("""Enter desired subfolder for file copying from the available folders listed below:
                          \n{} \n>""".format((sp.run('ls', cwd=config['PATHS']['sd_path'],shell=True
                                                     ,capture_output=True,text=True).stdout))) + '/'
        return config['PATHS']['sd_path'] + folder


    if ctype == 'x3':
        return config['PATHS']['bythree_dest_path']
    elif ctype == 'rwci':
        return config['PATHS']['rwci_dest_path']
    else:
        return input('Enter desired directory for writing files to:') or '/Users/sammyoge/photo_hq/'

def read_files(path=None):
    """

    :param path (str): Folder path.
    :return:
    """

    folder = path or orig_dir

    data = sp.run("ls | xargs stat -f '%SB %N' -t'%m-%d-%y'",
                  cwd=folder, shell=True, capture_output=True, text=True).stdout
    d = list(filter(None,data.split('\n')))
        # The first parameter is a function which has a condition to filter the input.
        # It returns True on success or False otherwise. However, if you provide a None,
        # then it removes all items except those evaluate to True.
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
    # This function takes the first 8 charachters of each file string

    for key, value in itertools.groupby(data,key_func):
        # itertools groups the data by the key_function. So in this case, the data will be grouped
        # by their first 8 characters where in this case is the date. The keys will be the date and
        # the values will be each file that has that same date.

        files[key] = [i.replace('{}'.format(key),'').lstrip(' ') for i in list(value)]
        # files now becomes a dictionary that who's keys are the dates of the files and the values are
        # the files themselves of that key date.

    return files


def form(data,sep=' '):

    return '{}'.format(sep).join(data)


def select_dates(content):

    d = input("""Enter desired date for file copying from the available 
                 dates listed below:\n{} \n>""".format('\n'.join(list(content.keys()))))

    return d.split() or list(content.keys())


def run(t=None,f=None):
    """
    :param data (list): List of files with date information.
    :return:

    Description:

    A. recording user input for source directory in fr
    B. recording user input for destination directory in to
    C. storing file path of src directory for copying files in fr
    D. storing file path of destination directory for copying files in to
    """

    # fr = f or input('Enter source directory:')  # A.
    # to = t or input('Enter destination directory:')  # B.

    src = client(ctype=f, c=True)
    dest = client(ctype=t)

    print('Reading contents of %s' % src)
    data = read_files(path=src)
    content = files_dict(data)
    catalog = select_dates(content)
    folders = form(catalog)
    print(folders)

    print('Writing contents of %s to %s' % (src, dest))
    cmd1 = 'mkdir %s' % folders
    sp.run(cmd1, cwd=dest, shell=True)
    # print(content)
    # cmd1 = 'mkdir {%s}' % ','.join(list(catalog.keys()))

    cp_cmd = []
    cp_cmd += ['cp {f} "{d}"'.format(f=form(content[k]), d=dest + k) for k in catalog]
    print(cp_cmd)
    [sp.run(cmd,cwd=src,shell=True) for cmd in cp_cmd]

    wb.open('file:///' + dest)
    #os.mkdir('{%s}' % dest)


# dest = '/Users/sammyoge/photo_temp/' + list(files.keys())[7]
# os.mkdir('%s' % dest)
# command = 'cp {f} {d}'.format(f=docs,d=dest)
# os.system(command)


if __name__ == "__main__":

    run()


