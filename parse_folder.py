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



def mftf(src,dest,data):
    """
    Move Files to specified folder.
    :param: None
    :return:
    """

    # if not set_dir(src):
    #     print('Source Folder does not exist')
    #     return
    #
    # if not os.path.isdir(dest):
    #     print('Creating directory TEMP folder in %s...' % src)
    #     os.mkdir('%s' % dest)


    command = "ls -l | cut -w -f 6,7,9"
    # print("Moving {f} to {d}".format(f= ', '.join(data.split(' ')),d=dest))
    # #print(command)
    # os.system(command)
    # set_dir(reset=True)
    # print('Done!')

    os.popen(command).read().split('\n'))

data = list(filter(len,os.popen('ls -l | cut -w -f 6,7,9').read().replace('\t',' ').split('\n')))

key_func = lambda x: x[0:5]

itertools.groupby(data, key_func):

for key, group in itertools.groupby(L, key_func):
    print(key + " :", list(group))