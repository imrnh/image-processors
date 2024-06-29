import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

image_path = "/home/imran/Desktop/Academic/Image/Image Processing Practice/images/lena.png"
image_data = cv.imread(image_path, cv.IMREAD_GRAYSCALE)


def make_negatives(image, r=255):
    new_image = np.zeros(image.shape) # Creating a new image cause this operation replace original image.
    for r_idx in range(new_image.shape[0]):
        for c_idx in range(new_image.shape[1]):
            new_image[r_idx][c_idx] = r - image[r_idx][c_idx] # (image[r_idx][c_idx])-r doesn't work cause plt ultimately add 255 when showing and making the image positive. 
        
    return new_image


neg_img = make_negatives(image_data)
print(image_data)
print(neg_img)

fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].imshow(image_data)
ax[1].imshow(neg_img)
ax[0].set_title("Original Image")
ax[1].set_title("Negative Image")
ax[0].axis("off")
ax[1].axis("off")
plt.tight_layout()
plt.show()