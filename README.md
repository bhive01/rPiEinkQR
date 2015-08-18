# rPiEinkQR
Scan a code or input it via command line and a QR Code is generated, resized, and output to the [Embedded Artists 2.7" screen] (http://www.embeddedartists.com/products/displays/lcd_27_epaper.php) from a raspberry pi

# Starting from scratch? 
Below are the require libraries for getting started. ImageMagick will install a large amount of libraries to pull from for all different types of images. epyper will pull in Wiring and Pillow as requirements through pip. 

* [qrencode] (https://fukuchi.org/works/qrencode/)
  * `sudo apt-get install qrencode`
* [ImageMagick](http://www.imagemagick.org/)
  * `sudo apt-get install imagemagick`
* [LibFUSE Driver](https://www.gnu.org/software/hurd/hurd/libfuse.html)
  * `sudo apt-get install libfuse-dev`
* [git](http://github.com)
  * `sudo apt-get install git`
* [EPD driver] (https://github.com/embeddedartists/gratis)
  * In a suitable directory `git clone https://github.com/embeddedartists/gratis.git`
* [This repository] (https://github.com/bhive01/rPiEinkQR)
  * In a suitable directory `git clone https://github.com/bhive01/rPiEinkQR.git`
* Turn on SPI interface
  * `sudo raspi-config`
  * 8 Advanced Options > A6 SPI > Enable > Yes (load by default) > OK > Finish
  * `sudo reboot`

# EPD Tests and Usage
From: https://github.com/repaper/gratis/tree/master/PlatformWithOS

To Test EPD:
``` Shell
sudo modprobe spi-bcm2708
make rpi-epd_test COG_VERSION=V2
sudo ./driver-common/epd_test 2.7
```
To Install EPD Driver:
``` Shell
sudo make rpi-install   # bb-install
sudo service epd-fuse start
ls -l /dev/epd
```
	
Usage:
``` Shell
sudo python rPiEinkQREPD.py
```
## Barcode Scanners
Most barcode readers are seen as keyboards by the OS. The important part is to have it set to add a newline after each read. This newline will cause the program to proceed with the code. If there are issues, see the following help forums:
https://www.raspberrypi.org/forums/viewtopic.php?f=45&t=55100

## ePyper
ePpyper is a library built in python to write to these displays, but for some reason it no longer works with the display. It doesn't require installation of the EPD driver because it has its own built-in. I believe it might have been built for the previous version of the screen, which might explain why it doesn't write to the screen itself. 
### Epyper Installation
* [pip](https://pip.pypa.io/en/stable/) (Python Package Installer)
    * Python 2
      * `sudo apt-get install python-pip`
    * Python 3? [Visit here](https://www.raspberrypi.org/documentation/linux/software/python.md) 
* [epyper](https://github.com/mnowotka/epyper)
	* `pip install epyper` 
