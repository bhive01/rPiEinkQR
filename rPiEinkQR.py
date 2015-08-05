import os
from PIL import Image
from epyper.displayCOGProcess import Display
from epyper.displayController import DisplayController

# code to create QR code of good size for eink screen
# qrencode -o qrcode.png -s 7 -l L -v 1 -m 1 "TestThree003"

QRname = "qrencode -o qrcode.png -s 7 -l L -v 1 -m 1 \"" + "TestThree04" + "\""
os.system(QRname)

imgName = "qrcode.png"

im = Image.open(imgName)

convertname = "convert " + imgName + " -background white -gravity center -extent 264x176 "+ imgName
os.system(convertname)

im = Image.open(imgName)

#create DisplayController instance specifying display type as an argument
display = DisplayController(Display.EPD_TYPE_270)

#display it!
display.displayImg(im)
