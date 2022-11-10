#!/usr/bin/env python3

#PROJECT MODULES
from data import *
from client import *
from browser_check import *

#OTHER
from os import system
'''
v_br, v_dr = getChromeVersion()
print( f"Browser version >>> {v_br}, \nDriver version  >>> {v_dr}" )

'''
system( "clear" )


browser, canvas = connectToClient() 
frame_tensor    = getCanvasTensor( browser, canvas )
zoneA, zoneB, zoneC, zoneD, zoneE = splitTensorToZones( frame_tensor )
viewImg( zoneA )
