from flask import Flask, render_template, request, redirect, url_for, send_file
import qrcode
from PIL import Image
import io

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('data_input')
        logo_file = request.files.get('logo_file')

        if user_input:
            qr = qrcode.QRCode(
                version=3,
                box_size=20,
                border=10,
                error_correction=qrcode.constants.ERROR_CORRECT_H
            )
            qr.add_data(user_input)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert("RGB")


            if logo_file and logo_file.filename:

                try:
                    logo = Image.open(logo_file).convert("RGBA")


                    qr_w, qr_h = img.size
                    logo_size = int(qr_w / 5)
                    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
                    pos = ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)


                    img.paste(logo, pos, logo)
                except Exception as e:
                    print(f"Error adding logo: {e}")

            file_object = io.BytesIO()
            img.save(file_object, 'PNG')
            file_object.seek(0)


            return send_file(
                file_object,
                mimetype='image/png',
                as_attachment=True,
                download_name=f'qrcode_{user_input}.png'
            )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
