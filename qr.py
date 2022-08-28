#Generate a QR code for any text/link. In the end, it automatically opens up the newly generated QR code image file.

import os
import qrcode

data = input('Enter Data to Covert to QR: ')
fileName = input('Save File As: ')
img = qrcode.make(data)
img.save(fileName + ".png", "PNG")
os.system("open " + fileName + ".png")
