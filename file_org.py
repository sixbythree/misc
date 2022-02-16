import datetime
# import pandas as pd
# import numpy as np
import os
import re
import webbrowser
import subprocess as sp
import webbrowser as wb
# import requests
orig_dir = os.getcwd()

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


def raw_plus_jpg(files):
    """
    Format.
    :param: None
    :return:
    """

    if type(files) == str:
        nefs = list(filter(None,re.sub(r"[\n]*", "", files).split(' ')))
    elif type(files) == list:
        nefs = ''.join(files).replace('\n', '').split(' ')

    jpgs = ','.join(nefs).replace('.NEF','.JPG').split(',')

    return ' '.join(sorted(nefs + jpgs))


def mftf(src,dest,files):
    """
    Move Files to specified folder.
    :param: None
    :return:
    """

    if not set_dir(src):
        print('Source Folder does not exist')
        return

    if not os.path.isdir(dest):
        print('Creating directory %s' % dest)
        os.mkdir('%s' % dest)
    command = "mv {f} {d}".format(f=files,d=dest)
    print (command)
    os.system(command)
    set_dir(reset=True)
    print('Done!')


def run(src=None,dest=None,files=None):

    if not src:
        src = input('Enter source folder: ').replace('\'','')
    if not dest:
        dest = input('Enter destination folder: ').replace('\'','')
    if not files:
        files = input('Enter files or .txt: ' )

    if '.txt' in files:
        with open(files) as f:
            content = f.readlines()
            data = raw_plus_jpg(content)
    else:
        data = raw_plus_jpg(files)

    mftf(src, dest, data)


if __name__ == "__main__":

    # webbrowser.open('file:///Users/sammyoge/Desktop/Blessing_to_Burden')
    # src = '/Users/sammyoge/Desktop/Blessing_to_Burden'
    # dest = '/Users/sammyoge/Desktop/Blessing_to_Burden/TEMP'

    files = """DSC_6601.NEF 
    DSC_6503.NEF 
    DSC_6621.NEF 
    DSC_6515.NEF 
    DSC_6525.NEF 
    DSC_6624.NEF 
    DSC_6590.NEF 
    DSC_6528.NEF 
    DSC_6612.NEF 
    DSC_6542.NEF 
    DSC_6504.NEF 
    DSC_6631.NEF 
    DSC_6521.NEF 
    DSC_6632.NEF 
    DSC_6578.NEF 
    DSC_6574.NEF 
    DSC_6628.NEF 
    DSC_6623.NEF 
    DSC_6516.NEF 
    DSC_6614.NEF 
    DSC_6625.NEF 
    DSC_6626.NEF 
    DSC_6629.NEF 
    DSC_6627.NEF 
    DSC_6619.NEF 
    DSC_6536.NEF 
    DSC_6591.NEF 
    DSC_6508.NEF 
    DSC_6606.NEF"""

    run()






