
# This module provides the functions,
# dialog(msg)
# dialog_q(msg)
#
# Example:
#
# from trivial_dialogs import dialog, dialog_q
#
# dialog("hello")
# if dialog_q("Quit?"): quit()

import subprocess

# --------------------------------------------------------------------------------
# Configuration.
#
# Potentially, this could be 'kdialog', 'zenity', 'xmessage', 'tkinter', ...
# At present only 'kdialog' (from KDE) is implemented, 

DIALOG_CMD = 'kdialog'       # https://develop.kde.org/deploy/kdialog/

# --------------------------------------------------------------------------------

if DIALOG_CMD == 'kdialog':

    # A message with OK button,
    def dialog(msg):
        dialog_cmd = 'kdialog --title annotation-manager --msgbox "' + msg + '"'
        subprocess.run(dialog_cmd, shell=True)

    # A question with Yes/No buttons. Return values: (Yes, No) -> (True, False).  
    def dialog_q(msg):
        dialog_cmd = 'kdialog --title annotation-manager --yesno "' + msg + '"'
        return 0 == subprocess.run(dialog_cmd, shell=True).returncode 
        
elif DIALOG_CMD == 'zenity':

    print('zenity code for dialog() has not been written yet.')
    quit()

else:

    print('Unknown value for configuration constant DIALOG_CMD.')      
    quit()

