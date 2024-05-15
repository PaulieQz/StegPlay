from PIL import Image
import numpy as np

def embed_message(image_path: str, message: str) -> Image:
    image = Image.open(image_path)
    image = image.convert("RGB")
    data = np.array(image)

    message += chr(0)  # Null character as a message delimiter
    binary_message = ''.join([format(ord(char), '08b') for char in message])
    message_length = len(binary_message)

    if message_length > data.size:
        raise ValueError("Message is too large to fit in the image.")

    idx = 0
    for value in np.nditer(data, op_flags=['readwrite']):
        if idx < message_length:
            value[...] = int(format(value, '08b')[:-1] + binary_message[idx], 2)
            idx += 1

    stego_image = Image.fromarray(data)
    return stego_image

def extract_message(image_path: str):
    image = Image.open(image_path)
    image = image.convert("RGB")
    data = np.array(image)

    binary_message = ""
    chunk_size = 1024  # Adjust as needed for performance
    total_pixels = data.size
    processed_pixels = 0

    for chunk in np.nditer(data, flags=['external_loop'], op_flags=['readwrite'], buffersize=chunk_size):
        binary_message += ''.join([format(value, '08b')[-1] for value in chunk])
        processed_pixels += chunk.size

        # Provide progress feedback
        progress = (processed_pixels / total_pixels) * 100
        print(f"Progress: {progress:.2f}%")

        # Check for the null character every 1024 bits
        message_bytes = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
        message = ''.join([chr(int(byte, 2)) for byte in message_bytes])
        null_char_index = message.find(chr(0))
        if null_char_index != -1:
            return message[:null_char_index]

    return message.split(chr(0))[0]  # Split at the null character and return the message
