
import pickle
import os


# -----------------------------------------------------------------------------------------
# Location constants.

# Default, 
controls_file = 'controls.dat'

# To change the default,
def controls_file_location(f):
    global controls_file
    controls_file = f
    
# -----------------------------------------------------------------------------------------

controls_dict = {}
controls_mtime = 0                

def controls_write():
    global controls_file, controls_dict, controls_mtime
    with open(controls_file, 'wb') as g:
        pickle.dump(controls_dict, g, protocol=0)  # 0 => human readable.
    controls_mtime = os.path.getmtime(controls_file)

def controls_read():                   
    global controls_file, controls_dict
    try:
        with open(controls_file, 'rb') as g:
            controls_dict = pickle.load(g)
    except:
        controls_dict = {} 

def controls_modified_q():
    global controls_file, controls_mtime
    mtime = os.path.getmtime(controls_file)    
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

