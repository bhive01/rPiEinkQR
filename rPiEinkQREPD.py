import sys
import os
import time
from PIL import Image
from PIL import ImageOps
from EPD import EPD

#initiate oldcmd
oldcmd = ""

#initiate epd element
epd = EPD()


while True:
	# takes input from the command line. Keyboard or scanner emulating a keyboard. newline/return to send.
	usercmd = raw_input("Command:")
	
	# test for 'end' so we can stop the script when done
	if usercmd == 'end':
		break
	else:
		# are oldcmd and usercmd the same? If so, nothing new has been input, go around the loop again
		if oldcmd == usercmd:
			pass #do nothing, need pass, can't have empty if in python
		else: 
			#put together system command for making the QR code from usercmd
			QRname = "qrencode -o qrcode.png -s 7 -l L -v 1 -m 1 \"" + usercmd + "\""
			# s is size of single block, l is level of code 1 = simple, m is border in blocks (relative to s)
			# send assembled system command
			os.system(QRname)
			
			#load image for processing into correct size
			imgName = "qrcode.png"
			im = Image.open(imgName)
			
			#put together system command to pad picture with white pixels and put it on the right end of the image 
			convertname = "convert " + imgName + " -background white -gravity east -extent 264x176 "+ imgName
			#send assembled system command
			os.system(convertname)
			
			#add text label of usercmd to image for human readabilty
			convertlabel = "convert " + imgName + " -rotate -90 -gravity South -pointsize 20 -font 'FreeMono-Bold' -annotate +0+2 \""+ usercmd + "\"" " -rotate 90 " + imgName
			os.system(convertlabel)
			
			#reopen image after padding (need exact size for epyper)
			im = Image.open(imgName)
			im = ImageOps.grayscale(im)
			
			#clear epd 
			epd.clear()
			
			#display it!
			epd.display(im)
			epd.update()
			
			# set oldcmd to the usercmd so it's ready for next loop test
			oldcmd = usercmd
