#Generate a QR code for any text/link.

import os
import qrcode

data = input('Enter Data to Covert to QR: ')
fileName = input('Save File As: ')
img = qrcode.make(data)
img.save(fileName + ".png", "PNG")
os.system("open " + fileName + ".png")
