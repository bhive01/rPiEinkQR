# rPiEinkQR
Scan a code or input it via command line and a QR Code is generated, resized, and output to the Embedded Artists 2.7" screen from a raspberry pi

# Starting from scratch? 
Below are the require libraries for getting started. ImageMagick will install a large amount of libraries to pull from for all different types of images. epyper will pull in Wiring and Pillow as requirements through pip. 

* [qrencode] (https://fukuchi.org/works/qrencode/)
  * `sudo apt-get install qrencode`
* [ImageMagick](http://www.imagemagick.org/)
  * `sudo apt-get install imagemagick`
* [pip](https://pip.pypa.io/en/stable/) (Python Package Installer)
    * Python 2
      * `sudo apt-get install python-pip`
    * Python 3? [Visit here](https://www.raspberrypi.org/documentation/linux/software/python.md) 
* [epyper](https://github.com/mnowotka/epyper)
	* `pip install epyper` 
	
Usage:
``` Shell
sudo python rPiEinkQR.py
```

Some pages for reading from a barcode scanner:
https://www.raspberrypi.org/forums/viewtopic.php?f=45&t=55100

