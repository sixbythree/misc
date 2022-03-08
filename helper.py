import datetime
# import pandas as pd
# import numpy as np
import os
import itertools
import configparser
import re
import sys
import webbrowser
import subprocess as sp
import webbrowser as wb
# import requests


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