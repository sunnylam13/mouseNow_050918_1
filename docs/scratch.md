# Scratch Notes and Logs

## Wednesday, May 9, 2018 9:53 PM

High level overview

* display the current x, y coordinates of the mouse cursor

* update the coordinates as the mouse moves around the screen

Code actions

* call the `position()` function to get current coordinates

* erase previously coordinates using `\b` back space characters

* handle `KeyboardInterrupt` exceptions so user can quit with Ctrl + C

## Wednesday, May 9, 2018 10:04 PM

	print(positionStr,end="")
	print( "\b" * len(positionStr),end="",flush=True )

`end=""` prevents the default newline character from being added at the end of a printed line

it's possible to erase

NOTE:  It’s possible to erase text you’ve already printed to the screen — but only for the most recent line of text.

to erase text, print the `\b` escape character...

It's a special character that erases a character at the end of the current line on the screen...

It uses string replication string with as many `\b` characters as the length of the strength stored in `positionStr` which has the effect of erasing the string last printed...

WARNING:  technical reasons, always pass `flush=True` to `print()` calls that print `\b`...  Otherwise the screen might not update the text as desired...