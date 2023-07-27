""""
Author: Paulo R. P. Santiago

This script is used to enhance the resolution of an image using either the
RDN (Residual Dense Network) or RRDN (Residual in Residual Dense Network) models
from the Image Super-Resolution (ISR) library.

The model to use is determined by the 'weights' parameter.
The 'psnr-large', 'psnr-small', and 'noise-cancel' weights will use the RDN model,
while the 'gans' weights will use the RRDN model.

The image to enhance and the weights are both provided as command-line arguments.

Usage: python script.py <image_path> <weights>

<image_path>: The path to the image you want to enhance.
<weights>: The weights parameter to determine which model to use.
           Acceptable values are 'psnr-large', 'psnr-small', 'noise-cancel', or 'gans'.

Citation
If you use this script for your research, please cite the following work:
F. Cardinale et al., ISR, 2018. [Online]. Available: https://github.com/idealo/image-super-resolution
"""

import os
import sys
import numpy as np
from PIL import Image

def increase_resolution(image_path, weights, output_folder, patch_size=None):
    """
    This function increases the resolution of the image specified by image_path.
    The type of model used is determined by the 'weights' parameter.
    The high-resolution image is saved in the output_folder.
    If patch_size is specified, the image is processed in patches of that size.
    If patch_size is None, the image is processed all at once.
    """
    # Load the image and convert it to a numpy array
    img = Image.open(image_path)
    lr_img = np.array(img)

    # Create the appropriate model based on the weights provided
    if weights in ['psnr-large', 'psnr-small', 'noise-cancel']:
        from ISR.models import RDN
        model = RDN(weights=weights)
    elif weights == 'gans':
        from ISR.models import RRDN
        model = RRDN(weights=weights)
    else:
        raise ValueError("The provided weights are not valid.")

    # Use the model to increase the resolution of the image
    if patch_size is None:
        sr_img = model.predict(lr_img)
    else:
        sr_img = model.predict(lr_img, by_patch_of_size=patch_size)

    # Convert the numpy array back into an image
    high_res_img = Image.fromarray(sr_img)

    # Save the high-resolution image in the output folder
    print(f"Saving image to: {output_folder}") # This line is new
    high_res_img.save(os.path.join(output_folder, 'high_res_'+weights+'_'+os.path.basename(image_path)))

    # Return the high-resolution image so it can be used later
    return sr_img

if __name__ == "__main__":
    # Check if the user provided the correct arguments
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python script.py <image_path> <weights> [<patch_size>]")
        sys.exit(1)

    # Retrieve the command line arguments
    image_path = sys.argv[1]
    weights = sys.argv[2]
    patch_size = int(sys.argv[3]) if len(sys.argv) == 4 else None

    # Create output folder inside image folder
    output_folder = os.path.join(image_path, "output")
    os.makedirs(output_folder, exist_ok=True)

    # Process all images in the specified directory
    for file_name in os.listdir(image_path):
        if file_name.endswith(".jpg") or file_name.endswith(".png"):
            high_res_img = increase_resolution(os.path.join(image_path, file_name), weights, output_folder, patch_size)
