#qrcode generator

import qrcode

feature = qrcode.QRCode(version=1, box_size=10, border=5)

feature.add_data("https://github.com/shashinihewage") #add data/link to qr code
feature.make(fit=True)
generate_img = feature.make_image(fill="black", back_color="white") #qr code color can change according to the user preference
generate_img.save("qr.png")
