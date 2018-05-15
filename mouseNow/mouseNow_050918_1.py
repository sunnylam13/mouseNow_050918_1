# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 mouseNow_050918_1.py

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

import pyautogui

print("Print Ctrl-C to quit.")

try:
	while True:
		# get and print the mouse coordinates
		x,y = pyautogui.position()
		positionStr = "X:  " + str(x).rjust(4) + " Y:  " + str(y).rjust(4)
		# logging.debug( positionStr )
		
		# color analysis
		pixelColor = pyautogui.screenshot().getpixel( (x,y) )
		positionStr += ' RGB: (' + str( pixelColor[0] ).rjust(3)
		positionStr += ', ' + str( pixelColor[1] ).rjust(3)
		positionStr += ', ' + str( pixelColor[2] ).rjust(3) + ')'

		print(positionStr,end="")
		print( "\b" * len(positionStr),end="",flush=True )
except KeyboardInterrupt:
	print("\nDone.")
