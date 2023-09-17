from PIL import Image

# Load the steganographed image
steganographed_image = Image.open('/home/meanzad/Desktop/Projects/dsp/steganographed_image.png')


# Convert the steganographed image to RGB mode
steganographed_image = steganographed_image.convert('RGB')

# Create a new image with the same dimensions as the steganographed image
secret_image = Image.new('RGB', steganographed_image.size)

# Iterate over each pixel of the steganographed image to extract the LSB
steganographed_pixels = steganographed_image.load()
secret_pixels = secret_image.load()
width, height = steganographed_image.size

for x in range(width):
    for y in range(height):
        r, g, b = steganographed_pixels[x, y]
        # Extract the LSB (least significant bit)
        r_secret = (r & 1) << 7
        g_secret = (g & 1) << 7
        b_secret = (b & 1) << 7
        secret_pixels[x, y] = (r_secret, g_secret, b_secret)


# Save the extracted secret image
secret_image.save('/home/meanzad/Desktop/Projects/dsp/extracted_secret_image.png')

print("Secret image extracted and saved as extracted_secret_image.png.")

#Display the extracted secret image using matplotlib
extracted_secret_image = Image.open('/home/meanzad/Desktop/Projects/dsp/extracted_secret_image.png')
