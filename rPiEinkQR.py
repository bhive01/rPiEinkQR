import os, time
from PIL import Image
from epyper.displayCOGProcess import Display
from epyper.displayController import DisplayController

#initiate oldcmd
oldcmd = ""

while True:
	usercmd = raw_input("Command:")
	if usercmd == 'end':
		break
	else:
		if oldcmd == usercmd:
			pass #do nothing
		else: 
			#put together system command for making the QR code
			QRname = "qrencode -o qrcode.png -s 7 -l L -v 1 -m 1 \"" + usercmd + "\""
			# s is size of single block, l is level of code 1 = simple, m is border in blocks (relative to s)
			# send assembled system command
			os.system(QRname)
			
			#load image for processing into correct size
			imgName = "qrcode.png"
			im = Image.open(imgName)
			
			#put together system command to pad picture with white pixels  
			convertname = "convert " + imgName + " -background white -gravity east -extent 264x176 "+ imgName
			#send assembled system command
			os.system(convertname)
			
			#add label to image
			convertlabel = "convert " + imgName + " -rotate -90 -gravity South -pointsize 20 -font 'FreeMono-Bold' -annotate +0+2 \""+ usercmd + "\"" " -rotate 90 " + imgName
			print(convertlabel)
			os.system(convertlabel)
			
			#reopen image after padding (need exact size for epyper)
			im = Image.open(imgName)
			
			#create DisplayController instance specifying display type as an argument
			display = DisplayController(Display.EPD_TYPE_270)
			
			#display it!
			display.displayImg(im)
			
			oldcmd = usercmd
