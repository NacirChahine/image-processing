import cv2

# Specify the path to your image
image_path = r"C:\Users\nacwo\Desktop\open cv sample\sampleImage.jpg"

# Read the image
image = cv2.imread(image_path)

# Specify the rotation angle (in degrees)
angle = 45

# Get the height and width of the image
height, width = image.shape[:2]

# Calculate the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

# Perform the actual rotation
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Display the original and rotated images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
