import qrcode 
from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4)

qr.add_data("https://youtu.be/gb8vlammvRI?si=Ax-05lQr0pQI1245")
qr.make(fit=True)

img=qr.make_image(fill_color="orange",back_color="grey")

img.save("chhave1.png")