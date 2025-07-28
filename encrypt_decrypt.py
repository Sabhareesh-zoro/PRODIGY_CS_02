from PIL import Image

KEY = 50  # Encryption key

def encrypt_image(image_path, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + KEY) % 256,
                (g + KEY) % 256,
                (b + KEY) % 256
            )

    img.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - KEY) % 256,
                (g - KEY) % 256,
                (b - KEY) % 256
            )

    img.save(output_path)
    print(f"Decrypted image saved to {output_path}")

# Run the functions
encrypt_image("sample_input.png", "encrypted.png")
decrypt_image("encrypted.png", "decrypted.png")
