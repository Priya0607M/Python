# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 08:14:19 2025

@author: Priya
"""

#a.	Write a Python program to display details of an image (dimension of an image, shape of an image, min pixel value at channel B).

from PIL import Image
import numpy as np
 
img = Image.open(r"C:\Users\Priya\Desktop\PWP\MU.jpg")

image_width, image_height = img.size
print("Image Dimensions:", image_width, "x", image_height)

img_arr = np.array(img)

img_shape = img_arr.shape
print("Image Shape :", img_shape)

if len(img_shape) == 3: 
    blue_channel = img_arr[:, :, 2]
    min_pixel_value_b = np.min(blue_channel)
    print("Minimum Pixel Value at Channel B:", min_pixel_value_b)
else:
    print("Image is not a color image, cannot determine min pixel value for channel B.")


#b.	Write a Python program to padding black spaces 

from PIL import Image
import matplotlib.pyplot as plt

padding_left = 20
padding_top = 20
padding_right = 20
padding_bottom = 20


original_image = Image.open(r"C:\Users\Priya\Desktop\PWP\MU.jpg")

original_width, original_height = original_image.size

new_width = original_width + padding_left + padding_right
new_height = original_height + padding_top + padding_bottom

padded = Image.new("RGB", (new_width, new_height), (0, 0, 0))


padded.paste(original_image, (padding_left, padding_top))

plt.imshow(padded)
plt.axis("off")
plt.show()

#c.	Write a Python program to visualize RGB channels 

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open(r"C:\Users\Priya\Desktop\PWP\MU.jpg").convert('RGB')
img_arr = np.array(img)

red = img_arr[:, :, 0]
green = img_arr[:, :, 1]
blue = img_arr[:, :, 2]

red_tint = np.zeros_like(img_arr)
red_tint[:, :, 0] = red

green_tint = np.zeros_like(img_arr)
green_tint[:, :, 1] = green

blue_tint = np.zeros_like(img_arr)
blue_tint[:, :, 2] = blue

fig, axes = plt.subplots(2, 4, figsize=(16, 8))

axes[0, 0].imshow(img_arr)
axes[0, 0].set_title("Original")
axes[0, 0].axis('off')

axes[0, 1].imshow(red, cmap='gray')
axes[0, 1].set_title("Red channel (gray)")
axes[0, 1].axis('off')

axes[0, 2].imshow(green, cmap='gray')
axes[0, 2].set_title("Green channel (gray)")
axes[0, 2].axis('off')

axes[0, 3].imshow(blue, cmap='gray')
axes[0, 3].set_title("Blue channel (gray)")
axes[0, 3].axis('off')

axes[1, 0].imshow(red_tint)
axes[1, 0].set_title("Red channel (tinted)")
axes[1, 0].axis('off')

axes[1, 1].imshow(green_tint)
axes[1, 1].set_title("Green channel (tinted)")
axes[1, 1].axis('off')

axes[1, 2].imshow(blue_tint)
axes[1, 2].set_title("Blue channel (tinted)")
axes[1, 2].axis('off')

axes[1, 3].imshow(img_arr)
axes[1, 3].set_title("Combined / Original")
axes[1, 3].axis('off')

plt.tight_layout()
plt.show()


