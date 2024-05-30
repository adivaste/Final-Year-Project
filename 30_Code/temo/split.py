from PIL import Image
import numpy as np
import cv2

def encrypt_split_image(image_path, output_path_share1, output_path_share2):
    # Open the image
    original_image = Image.open(image_path)

    # Convert the image to grayscale
    gray_image = original_image.convert('L')

    # Convert the image to a NumPy array
    image_array = np.array(gray_image)

    # Generate two random images with the same dimensions
    random_image1 = np.random.randint(0, 256, size=image_array.shape, dtype=np.uint8)
    random_image2 = np.mod(image_array - random_image1, 256).astype(np.uint8)

    # Convert the NumPy arrays back to PIL images
    share1 = Image.fromarray(random_image1)
    share2 = Image.fromarray(random_image2)

    # Save the shares
    share1.save(output_path_share1)
    share2.save(output_path_share2)

# Example usage
# input_image_path = 'output_image.png'
# output_path_share1 = 'share1.png'
# output_path_share2 = 'share2.png'

# encrypt_image(input_image_path, output_path_share1, output_path_share2)