#genereuje qr kody z url
import pyqrcode
#súčasť knižnice Pillow - pre prácu s obrázkami
from PIL import Image

#vložiť link do premennej link
link = input('Zadajte url:')

#funkcia create() z knižnice pyqrcode 
#z premennej link vezme url a vytvorí objekt QR kódu
qr_code = pyqrcode.create(link)

#uloží obrázok ako obrázok pod názvom 
qr_code.png("QRcode.png")
img = Image.open("QRcode.png")
img.show()

#Image.open("QRcode.png").show("QRcode.png")
