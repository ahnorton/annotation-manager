#!/bin/sh

# To auto-start annotation-ctrl after KDE starts, create a link to this file in autostart-scripts.
# This can be done using System Settings -> Autostart -> Add.
# Alternatively, use the commands,
# 
#   cd ~/.config/autostart-scripts
#   ln -s amdir/start-annotation-ctrl.sh
#
# where "amdir" is the path to the directory that contains the annotation manager
# files (including this script).
#
# ----------------------------------------------------------------------------------------

amdir=$( dirname -- "$( readlink -f -- "$0"; )"; )
# echo $amdir

# Edit the following command to add any --exclude option that you require,

$amdir/annotation-ctrl &
