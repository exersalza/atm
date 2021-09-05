import qrcode

from ..server.etc.config import FORMAT, HEADER, PORT


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=6,
    border=2,
)


data = {
    "content": {
        "header": {
            "format": FORMAT,
            "header": HEADER,
            "port": PORT
        },
        "body": {

        }
    }
}
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color=(0, 0, 0), back_color=(255, 165, 0))
img.save('test.png')