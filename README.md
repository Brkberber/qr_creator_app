# Flask QR Code Generator

A simple and robust web application built with Python and Flask that generates QR codes with optional custom logos. The application ensures high readability of the QR codes by using advanced error correction, even when a logo is embedded.

## Features

- **QR Code Generation** — Generate a QR code for any text or URL.
- **Custom Logo Integration** — Upload and embed a custom logo in the center of the QR code.
- **High Readability** — Utilizes the highest error correction level (`ERROR_CORRECT_H`) to ensure the QR code remains scannable even with a logo covering up to 30% of the data.
- **Clean UI** — A simple and intuitive web interface for easy use.
- **File Download** — The generated QR code is automatically downloaded as a PNG file.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.7+  
- pip (Python package installer)

## Installation

Clone this repository to your local machine:
```bash
git clone https://github.com/Brkberber/qr_creator_app.git
cd qr_creator_app
```

Install the required Python packages:
```bash
pip install Flask qrcode Pillow
```

## Usage

Run the Flask application from your terminal:
```bash
python main.py
```

Open your web browser and go to `http://127.0.0.1:5000` to access the application.

1. Enter the text or URL you want to encode.  
2. Optionally, upload a logo to embed inside the QR code.  
3. Click **"Generate & Download"** to create and download your QR code.

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
