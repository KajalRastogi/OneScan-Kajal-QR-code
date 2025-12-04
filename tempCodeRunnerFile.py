import qrcode
from PIL import Image

# QR base
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data("https://www.youtube.com/watch?v=JSoAvy8Y1DU")
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Add logo
logo = Image.open("E:\\Python_projects\\kajal_logo.png")  # your image file
logo = logo.resize((80, 80))  # resize for balance

# Position in center
pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
qr_img.paste(logo, pos)

qr_img.save("kajal_name_qr_logo.png")
