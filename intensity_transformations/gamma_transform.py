import numpy as np
import matplotlib.pyplot as plt

IMAGE_SHAPE = 3

# make sample image
sample_image = []
for i in range(IMAGE_SHAPE):
    r_arr = []
    for j in range(3):
        ival = np.random.randint(low=1, high=255)
        r_arr.append(ival)
    sample_image.append(r_arr)

def gamma_transform(image, C, Gamma):
    new_image = np.zeros((IMAGE_SHAPE, IMAGE_SHAPE))
    
    S = lambda c, r, g: c * (r ** g)
    for r_idx in range(IMAGE_SHAPE):
        for c_idx in range(IMAGE_SHAPE):
            new_image[r_idx][c_idx] = S(C, image[r_idx][c_idx], Gamma)

    return new_image



gamma_images = []
gamma_values = [0.04, 0.1, 0.8, 1, 1.5, 5, 10, 20]
for g_val in gamma_values:
    gamma_image = gamma_transform(sample_image, C=1, Gamma=g_val)
    gamma_images.append(gamma_image)

    print(f"Gamma value: {g_val}")
    print(f"\nGamma Image: {gamma_image}")
    print("\n\n")

# Plotting
num_images = len(gamma_images)
num_cols = 5
num_rows = int(np.ceil(num_images / num_cols)) + 1  # Calculate number of rows needed

fig, ax = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(15, 15))

# Display the original image
ax[0, 0].imshow(sample_image, cmap="gray")
ax[0, 0].set_title("Original Image")
ax[0, 0].axis("off")

# Plot gamma corrected images
for idx, gamma_image in enumerate(gamma_images):
    row = (idx // num_cols) + 1
    col = idx % num_cols
    gval = gamma_values[idx]
    ax[row, col].imshow(gamma_image, cmap="gray")
    ax[row, col].set_title(f"Gamma: {gval}")
    ax[row, col].axis("off")

# Remove empty subplots
for i in range(num_images, num_rows * num_cols):
    ax.flatten()[i].axis('off')

# plt.tight_layout()
fig.savefig("/home/imran/Desktop/Academic/Image/Image Processing Practice/output/gamma_transform_output.png")
plt.show()