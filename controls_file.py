
# The idea is to separate a GUI program and main program by having them read/write a controls file.
# Importing this module to a GUI program and main program makes this easy to do.
#
# Usage:
# from controls_file import *   

__all__ = [
    'controls_file',
    'controls_write',
    'controls_read',
    'controls_modified_q',
    'controls_set',
    'controls_get' ]

import pickle
import os

# -----------------------------------------------------------------------------------------
# Location constants.

# Default, 
cfile = 'controls.dat'

def controls_file(f):
    global cfile
    cfile = f
    
# -----------------------------------------------------------------------------------------

# Initially,
controls_dict = {}
controls_mtime = 0                

def controls_write():
    global cfile, controls_dict, controls_mtime
    dir = os.path.dirname(os.path.realpath(cfile))
    os.makedirs(dir, exist_ok = True)
    with open(cfile, 'wb') as g:
        pickle.dump(controls_dict, g, protocol=0)  # 0 => human readable.
    controls_mtime = os.path.getmtime(cfile)

def controls_read():                   
    global cfile, controls_dict
    try:
        with open(cfile, 'rb') as g:
            controls_dict = pickle.load(g)
    except:
        controls_dict = {} 

def controls_modified_q():
    global cfile, controls_mtime
    mtime = os.path.getmtime(cfile)    
    ans = not (mtime == controls_mtime)
    if ans:
       controls_mtime = mtime 
    return ans

def controls_set(k, v):
    global controls_dict
    controls_dict[k] = v

def controls_get(k):
    global controls_dict
    return controls_dict.get(k, None)

