from PIL import Image
import numpy as np

def reconstruct_image(share1_path, share2_path, output_path):
    try:
        # Open the two share images
        share1 = Image.open(share1_path)
        share2 = Image.open(share2_path)

        # Convert the share images to NumPy arrays
        share1_array = np.array(share1)
        share2_array = np.array(share2)

        # Reconstruct the original image by adding the two shares
        reconstructed_image_array = np.mod(share1_array + share2_array, 256).astype(np.uint8)
        reconstructed_image = Image.fromarray(reconstructed_image_array)

        # Save the reconstructed image
        reconstructed_image.save(output_path)
        return 1
    except:
        return 0


# Example usage
# share1_path = 'share1.png'
# share2_path = 'share2.png'
# output_path_reconstructed = 'reconstructed_image.png'

# reconstruct_image(share1_path, share2_path, output_path_reconstructed)
