#!/bin/python3

# 
# This module provides the function displayed_files() which returns the set of 
# file names of PDFs that are being displayed by PDF_VIEWER.

# This module can also be run as a script to print displayed_files(). 

import dbus
import re
import fnmatch

# Example:
# from displayed_files import displayed_files, debug_displayed_files      
# displayed_files.displayed_files()    

# ------------------------------------------------------------------------------------------------------------------
# This code could be extended to other PDF viewers.
# At present it is only written for Okular on the KDE desktop and config variable PDF_VIEWER is nowhere used,
PDF_VIEWER = 'okular'

# ------------------------------------------------------------------------------------------------------------------
# Printing of debug info.

# Default value,
debug = False

def debug_displayed_files(d):
    global debug
    debug = d

# ------------------------------------------------------------------------------------------------------------------
# Match string for file names to exclude from output of displayed_files().

# Default value (no exclusions),
match_string = ''

def exclude_file_names(m):
    global match_string
    match_string = m 

# ------------------------------------------------------------------------------------------------------------------
    
last_window_list = []         # only used to limit debug printing.

def okular_window_list():
    global last_window_list   # only used to limit debug printing.
    window_list = []
    for service in dbus.SessionBus().list_names():
        if 'okular' in service:
            window_list.append(str(service))
    if debug:
        if not (window_list == last_window_list):
            print('okular_window_list():', window_list)
            last_window_list = window_list
    return window_list

def tab_paths(w):
    try:
        obj = dbus.SessionBus().get_object(w, '/')
        xml = obj.Introspect()
    except:
        xml = ''
    p = re.findall('"okular[0123456789]*"', xml) 
    return map(slash, p)

# The following is used in the above map() for doing '"okularN"' -> '/okularN'
def slash(s): return '/'+s[1:-1]

# If any okular windows are being used then 
# dbus path /okular always exists, even if its document has been closed, in which case asking for it gives,
#   Error: org.freedesktop.DBus.Error.UnknownInterface
#   No such interface 'org.kde.okular' at object path '/okular'
# Hence using try...

def files_in_window(w):
    obj_paths = tab_paths(w)
    # if debug: print('files_in_window(): obj_paths =', obj_paths)
    files = []
    for p in obj_paths:
        try:
            obj = dbus.SessionBus().get_object(w, p)
            f = str(obj.currentDocument())
        except:
            pass
        else:
            files.append(f)
    return files

def displayed_files():
    global match_string
    files = []
    windows = okular_window_list()
    for w in windows:
        files.extend(files_in_window(w))
    # if debug: print('displayed_files(): files =', files)
    g = filter(lambda f: not fnmatch.fnmatchcase(f, match_string), files)
    return set(g)

# ------------------------------------------------------------------------------------------------------------------
# For running as a script,

if __name__ == "__main__":
    print(displayed_files())


