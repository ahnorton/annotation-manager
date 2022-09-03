#!/bin/sh

# To auto-start annotation-ctrl after KDE starts, create a link to this file in autostart-scripts.
# This can be done using System Settings -> Autostart -> Add.
# Alternatively, use the commands,
# 
#   cd ~/.config/autostart-scripts
#   ln -s <path-to-script-dir>/start-annotation-ctrl
#
# ----------------------------------------------------------------------------------------

# This shell script should be in the same directory as the annotation-ctrl and annotation-mgr 
# python scripts. $d is the directory of this script,

d=$( dirname -- "$( readlink -f -- "$0"; )"; )

# Edit the following command to add any options that you require (i.e., --exclude or --position),

$d/annotation-ctrl &




