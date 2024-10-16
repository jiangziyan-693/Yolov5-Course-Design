import cv2
import numpy as np

def custom_augmentation(image, labels):
    # Example: Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Example: Add Gaussian noise
    noise = np.random.normal(0, 25, gray_image.shape).astype(np.uint8)
    noisy_image = cv2.add(gray_image, noise)

    # Ensure to maintain the shape of the original image
    if len(noisy_image.shape) == 2:
        noisy_image = cv2.cvtColor(noisy_image, cv2.COLOR_GRAY2BGR)

    return noisy_image, labels
