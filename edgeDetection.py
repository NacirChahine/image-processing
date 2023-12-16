import cv2
import numpy as np

# Specify the path to your image
image_path = r"C:\Users\nacwo\Desktop\open cv sample\sampleImage.jpg"

# Read the image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel operator for gradient calculation
gradient_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

# Combine the gradients to get the magnitude
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
gradient_magnitude = np.uint8(255 * gradient_magnitude / np.max(gradient_magnitude))

# Apply Laplacian for edge detection
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
laplacian = np.uint8(np.abs(laplacian))

# Display the original, gradient, and Laplacian images
cv2.imshow("Original Image", image)
cv2.imshow("Gradient Magnitude", gradient_magnitude)
cv2.imshow("Laplacian Edge Detection", laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
