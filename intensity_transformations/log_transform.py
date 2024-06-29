import math
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

C = lambda mx: 255/math.log(1+mx)
S = lambda c, r:  c * math.log(1 + r)

def log_transform(input_image):
    image = np.zeros(input_image.shape)

    # Calculate C
    max_intensity_value = 0
    for row in input_image:
        for rv in row:
            if rv > max_intensity_value:
                max_intensity_value = rv
    c_value = C(max_intensity_value)
    
    # Calculate log transform value for each image
    for r_idx in range(input_image.shape[0]):
        for c_idx in range(input_image.shape[1]):
            image[r_idx][c_idx] = S(c_value, input_image[r_idx][c_idx])
    
    return image



image_path = "/home/imran/Desktop/Academic/Image/Image Processing Practice/images/low_light_image.png"
image_data = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

log_image = log_transform(image_data)


# Plotting
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].imshow(image_data, cmap="gray")
ax[1].imshow(log_image, cmap="gray")
ax[0].set_title("Original Image")
ax[1].set_title("Log Tranformed Image")
ax[0].axis("off")
ax[1].axis("off")
plt.tight_layout()
plt.savefig("/home/imran/Desktop/Academic/Image/Image Processing Practice/output/log_tranformation_output.png")
plt.show()
