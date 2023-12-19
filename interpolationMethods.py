import cv2

# Specify the path to your image
image_path = r".\sampleImage.jpg"

# Read the image
image = cv2.imread(image_path)

# Get the height and width of the image
height, width = image.shape[:2]

# Define the scaling factor
scale_factor = 2.0

# Resize the image using different interpolation methods
nearest_neighbor = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_NEAREST)
bilinear = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
cubic = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

# Display the original and resized images using different interpolation methods
cv2.imshow("Original Image", image)
cv2.imshow("Nearest Neighbor Interpolation", nearest_neighbor)
cv2.imshow("Bilinear Interpolation", bilinear)
cv2.imshow("Cubic Interpolation", cubic)
cv2.waitKey(0)
cv2.destroyAllWindows()
