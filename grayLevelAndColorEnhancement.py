import cv2
import numpy as np

# Specify the path to your image
image_path = r"C:\Users\nacwo\Desktop\open cv sample\sampleImage.jpg"

# Read the image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization to enhance color
color_enhanced_image = cv2.equalizeHist(gray_image)

# Display the original, grayscale, and color-enhanced images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.imshow("Color-Enhanced Image", color_enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
