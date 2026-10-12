import qrcode

img = qrcode.make("https://www.instagram.com/p/DbAkBOjke9C/?igsh=YnlkdGZhNTlsdnhw")
img.save("myqr.png")

print("QR Code Created")





img = qrcode.make("https://www.instagram.com/p/DbAkBOjke9C/?igsh=YnlkdGZhNTlsdnhw")
img.save("myqr.jpg")

print("QR Code Created")