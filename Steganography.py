from PIL import Image

# Load the cover image and secret image
cover_image = Image.open('/home/meanzad/Desktop/Projects/dsp/carrier.png')
secret_image = Image.open('/home/meanzad/Desktop/Projects/dsp/hidden.png')

# Convert images to grayscale if not already
cover_image = cover_image.convert('L')
secret_image = secret_image.convert('L')

# Ensure secret image dimensions are not larger than cover image dimensions
if secret_image.size[0] > cover_image.size[0] or secret_image.size[1] > cover_image.size[1]:
    print("Error: Secret image dimensions exceed cover image dimensions.")
else:
    # Iterate over each pixel and modify the LSB
    cover_pixels = cover_image.load()
    secret_pixels = secret_image.load()
    width = secret_image.width
    height = secret_image.height
    for x in range(width):
        for y in range(height):
            cover_pixel = cover_pixels[x, y]
            secret_pixel = secret_pixels[x, y]
            new_pixel_value = (cover_pixel & 0xFE) | (secret_pixel >> 7)  # Replace LSB with secret bit
            cover_image.putpixel((x, y), new_pixel_value)

    # Save the steganographed image
    cover_image.save('/home/meanzad/Desktop/Projects/dsp/steganographed_image.png')

    print("Steganography complete. Saved as steganographed_image.png.")

#Display the steganographed image 
steganographed_image = Image.open('/home/meanzad/Desktop/Projects/dsp/steganographed_image.png')
steganographed_image.show()