import datetime
# import pandas as pd
# import numpy as np
import os
import re
import sys
import webbrowser
import subprocess as sp
import webbrowser as wb
# import requests
orig_dir = os.getcwd()

# SCRIPT PURPOSE
# - CREATE A SCRIPT THAT MOVE SPECIFIED FILES FROM SOURCE FOLDER TO NEW DIRECTORY.

# WORKFLOW:
# A. SOURCE FOLDER
#    i. PROVIDED:
#    ii. NOT PROVIDED:
# B. DESTINATION FOLDER
#    i. PROVIDED:
#    ii. NOT PROVIDED:
# C. FILE LIST
#    - TESTING HAS BEEN DONE PRIMARILY ON A LIST OF .NEF FILES.
#    i. PROVIDED: FORMAT FILE LIST TO ENSURE THAT ALL FILES TO BE MOVED ARE SPECIFIED.
#    ii. NOT PROVIDED: END SCRIPT

# 1. FUNCTIONS

def abbrev():
    """
    Prints out list of all abbreviations.
    :return:
    """

    abv = {
        'cwd': 'current working directory'
    }

    print (abv)


def set_dir(path='None', reset = False):
    """
    Set directory to specified path.
    :param path (string): Path string to set cwd to.
    :param reset (False): Boolean to reset cwd to original directory (orig_dir).
    :return:
    """

    if reset:
        os.chdir(orig_dir)
        return

    if not os.path.isdir(path):
        return False
    else:
        os.chdir(path)
    return True


def file_input(files=None, folder='/User/sammyoge/Destkop'):

    if not files:
        data = input('Enter files or .txt: ').strip(' ')
        if not data:
            print("No files specified. Searching folder for all files...")
            set_dir(folder)
            command = "ls -p | grep -v /"
            files = list(filter(None,os.popen(command).read().split('\n')))
            set_dir(reset=True)
            return ' '.join(files)
        return raw_plus_jpg(data)


    if '.txt' in files:
        print('Text file input..')
        with open(files) as f:
            content = f.readlines()
            data = raw_plus_jpg(content)
            return data
    else:
        print('List of files...')
        data = raw_plus_jpg(str(files))
        return data

def raw_plus_jpg(files):
    """
    Format.
    :param: None
    :return:
    """

    if type(files) == str:
        nefs = list(filter(None,files.split()))
    elif type(files) == list:
        nefs = ','.join(files).replace('\n', '').split(',')

    jpgs = ','.join(nefs).replace('.NEF','.JPG').split(',')

    return ' '.join(sorted(nefs + jpgs))


def mftf(src,dest,data):
    """
    Move Files to specified folder.
    :param: None
    :return:
    """

    if not set_dir(src):
        print('Source Folder does not exist')
        return

    if not os.path.isdir(dest):
        print('Creating directory TEMP folder in %s...' % src)
        os.mkdir('%s' % dest)


    command = "mv {f} {d}".format(f=data,d=dest)
    print("Moving {f} to {d}".format(f= ', '.join(data.split(' ')),d=dest))
    #print(command)
    os.system(command)
    set_dir(reset=True)
    print('Done!')


def run(src=None,dest=None,files=None):

    if not src:
        src = input('Enter source folder: ').replace('\'','').strip(' ')
        if not src:
            print("No source folder provided. Goodbye!")
            return
    if not dest:
        dest = input('Enter destination folder: ').replace('\'','').strip(' ') or\
               input("Making new directory in %s. Enter directory name else 'temp'"
                     " will be used: " % src).replace('\'','').strip(' ') or\
               src + '/temp'

    data = file_input(files,src)
    #print (data)
    mftf(src, dest, data)


if __name__ == "__main__":

    # webbrowser.open('file:///Users/sammyoge/Desktop/Blessing_to_Burden')
    # src = '/Users/sammyoge/Desktop/Blessing_to_Burden'
    # dest = '/Users/sammyoge/Desktop/Blessing_to_Burden/TEMP'

    # files = """DSC_6601.NEF, DSC_6503.NEF, DSC_6621.NEF, DSC_6515.NEF, DSC_6525.NEF, DSC_6624.NEF, DSC_6590.NEF
    # DSC_6528.NEF, DSC_6612.NEF, DSC_6542.NEF, DSC_6504.NEF, DSC_6631.NEF, DSC_6521.NEF, DSC_6632.NEF, DSC_6578.NEF
    # DSC_6574.NEF, DSC_6628.NEF, DSC_6623.NEF, DSC_6516.NEF, DSC_6614.NEF, DSC_6625.NEF, DSC_6626.NEF, DSC_6629.NEF
    # DSC_6627.NEF, DSC_6619.NEF, DSC_6536.NEF, DSC_6591.NEF, DSC_6508.NEF, DSC_6606.NEF"""

    run()

