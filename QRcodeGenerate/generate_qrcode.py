import qrcode as qr

img= qr.make("https://pypi.org/project/qrcode/")

img.save("firstqr.png")