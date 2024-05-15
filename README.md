# Steganography App

This is a simple FastAPI web application that allows you to embed and extract hidden messages in images using steganography. The application provides two main functionalities: encrypting messages into images and decrypting messages from images.

## Features

- **Encrypt**: Upload an image and enter a secret message to embed within the image. The modified image will be available for download.
- **Decrypt**: Upload an image to extract and display the hidden message.
- **Progress Feedback**: Provides progress updates during the decryption process.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pillow
- NumPy

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/PaulieQz/StegPlay.git
    cd steganography_app
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\Activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the required dependencies:

    ```bash
    pip install fastapi uvicorn pillow numpy
    ```

## Usage

1. Run the FastAPI application:

    ```bash
    uvicorn app.main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

## Project Structure

```
steganography_app/
├── app/
│ ├── __init__.py
│ ├── main.py
│ ├── steganography.py
│ ├── static/
│ └── templates/
│ ├── index.html
│ └── decrypt_result.html
├── venv/
├── requirements.txt
└── README.md
```

## How It Works

### Encryption

1. Upload an image and enter the secret message on the encrypt tab.
2. The application embeds the message into the image using the least significant bit (LSB) steganography technique.
3. The modified image is provided for download.

### Decryption

1. Upload an image on the decrypt tab.
2. The application extracts the hidden message from the image.
3. Progress feedback is provided during the decryption process.
4. The hidden message is displayed upon completion.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pillow](https://python-pillow.org/)
- [NumPy](https://numpy.org/)
