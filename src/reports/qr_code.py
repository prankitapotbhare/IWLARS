# QR code generation logic (placeholder) 

import qrcode

def generate_qr_code(url, out_path):
    img = qrcode.make(url)
    img.save(out_path) 