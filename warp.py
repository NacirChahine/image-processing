import cv2
import numpy as np

# Specify the path to your image
image_path = r".\sampleImage.jpg"

# Read the image
image = cv2.imread(image_path)

# Get the height and width of the image
height, width = image.shape[:2]

# Define the source points (coordinates of a rectangle in the original image)
source_pts = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])

# Define the corresponding destination points (where the source points will be mapped to)
# Here, I'm shifting the rectangle to the bottom-right corner
destination_pts = np.float32([[width // 2, 0], [width - 1, height // 2], [0, height - 1]])

# Calculate the perspective transformation matrix
warp_matrix = cv2.getAffineTransform(source_pts, destination_pts)

# Apply the perspective transformation
warped_image = cv2.warpAffine(image, warp_matrix, (width, height))

# Display the original and warped images
cv2.imshow("Original Image", image)
cv2.imshow("Warped Image", warped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
