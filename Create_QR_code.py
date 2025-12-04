#Normal Process 
import qrcode as qr
# Create instance of QRCode
img = qr.make("https://www.youtube.com/watch?v=JSoAvy8Y1DU")
img.save("kajal_youtube_qr.png")

#High Level Process (WITH CUSTOMIZATION)
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4,)

qr.add_data("https://www.youtube.com/watch?v=JSoAvy8Y1DU")
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="Purple")
img.save("kajal_youtube_qr_custom.png")