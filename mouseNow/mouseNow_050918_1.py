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
		positionStr = "X:  " + str(x).rjust(4) + "Y:  " + str(y).rjust(4)
except KeyboardInterrupt:
	print("\nDone.")

print(positionStr,end="")
print( "\b" * len(positionStr),end="",flush=True )

