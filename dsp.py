from PIL import Image

def encode_lsb_image(base_image_path, secret_image_path, output_path):
    # Open the base image
    base_image = Image.open(base_image_path)

    # Open the secret image
    secret_image = Image.open(secret_image_path)

    # Convert the secret image to grayscale
    secret_image = secret_image.convert("L")

    secret_image = secret_image.resize(base_image.size)

    # Create a copy of the base image to modify
    encoded_image = base_image.copy()

    for y in range(encoded_image.height):
        for x in range(encoded_image.width):
            base_pixel = list(encoded_image.getpixel((x, y)))
            secret_pixel = secret_image.getpixel((x, y))

            for color_channel in range(3):
                base_pixel[color_channel] &= 0xFE  # Clear the LSB
                base_pixel[color_channel] |= (secret_pixel & 0x01)
                secret_pixel >>= 1

            encoded_image.putpixel((x, y), tuple(base_pixel))

    # Save the encoded image
    encoded_image.save(output_path)
    print("LSB image insertion complete.")

def decode_lsb_image(encoded_image_path, output_path):
    # Open the encoded image
    encoded_image = Image.open(encoded_image_path)

    # Create a new image to store the extracted secret
    decoded_image = Image.new("RGB", encoded_image.size)

    for y in range(encoded_image.height):
        for x in range(encoded_image.width):
            encoded_pixel = list(encoded_image.getpixel((x, y)))
            decoded_pixel = [encoded_pixel[channel] & 0x01 for channel in range(3)]
            decoded_pixel = [pixel * 255 for pixel in decoded_pixel]  # Scale to 0-255

            decoded_image.putpixel((x, y), tuple(decoded_pixel))

    # Save the decoded image
    decoded_image.save(output_path)
    print("LSB image extraction complete.")

# Example usage
base_image_path = "/home/meanzad/Desktop/Projects/dsp/carrier.png"  # Replace with your base image path
secret_image_path = "/home/meanzad/Desktop/Projects/dsp/hidden.png"  # Replace with your secret image path
encoded_image_path = "/home/meanzad/Desktop/Projects/dsp/encoded_image_with_secret.png"  # Output path for encoded image
decoded_image_path = "/home/meanzad/Desktop/Projects/dsp/decoded_hidden_image.png"  # Output path for decoded image

# Encode the secret image into the base image
encode_lsb_image(base_image_path, secret_image_path, encoded_image_path)

# Decode the hidden image from the encoded image
decode_lsb_image(encoded_image_path, decoded_image_path)