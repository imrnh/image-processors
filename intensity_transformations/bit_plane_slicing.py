import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

image_path = "/home/imran/Desktop/Academic/Image/Image Processing Practice/images/lena.png"
image_data = cv.imread(image_path, cv.IMREAD_GRAYSCALE)



# Plotting
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].imshow(image_data)
# ax[1].imshow(neg_img)
ax[0].set_title("Original Image")
ax[1].set_title("Negative Image")
ax[0].axis("off")
ax[1].axis("off")
plt.tight_layout()
plt.show()