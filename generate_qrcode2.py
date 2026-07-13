import qrcode

from PIL import Image

qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=10, border=4,)

qr.add_data("https://search.brave.com/search?q=qr+code+module+in+python&summary=1&conversation=095123df7fd4044f7b358fa3277a0f27292f")
qr.make(fit=True)

img=qr.make_image(fill_color="blue", back_color="black")

img.save("qrcode_brave.png")