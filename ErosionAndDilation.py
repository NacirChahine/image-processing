import cv2
import numpy as np

# Specify the path to your image
image_path = r"C:\Users\nacwo\Desktop\open cv sample\sampleImage.jpg"

# Read the image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold (convert the image to binary)
_, binary_image = cv2.threshold(gray_image, 160, 255, cv2.THRESH_BINARY)

# Define the kernel for erosion and dilation
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)

# Perform erosion
eroded_image = cv2.erode(binary_image, kernel, iterations=1)

# Perform dilation
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

# Display the original, binary, eroded, and dilated images
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary_image)
cv2.imshow("Eroded Image", eroded_image)
cv2.imshow("Dilated Image", dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
