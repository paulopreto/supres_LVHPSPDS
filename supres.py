"""
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

import sys
import numpy as np
from PIL import Image

def increase_resolution(image_path, weights):
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
    sr_img = model.predict(lr_img, by_patch_of_size=50)

    # Convert the numpy array back into an image
    high_res_img = Image.fromarray(sr_img)
    high_res_img.save('high_res_'+weights+'_'+image_path)

    # Return the high-resolution image so it can be used later
    return sr_img

if __name__ == "__main__":
    # Check if the user provided the correct arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <image_path> <weights>")
        sys.exit(1)

    # Retrieve the command line arguments
    image_path = sys.argv[1]
    weights = sys.argv[2]

    # Apply the model and save the resulting image
    high_res_img = increase_resolution(image_path, weights)