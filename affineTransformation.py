import cv2
import numpy as np

# Specify the path to your image
image_path = r"C:\Users\nacwo\Desktop\open cv sample\sampleImage.jpg"

# Read the image
image = cv2.imread(image_path)

# Get the height and width of the image
height, width = image.shape[:2]

# Define the scaling factor and translation parameters
scale_factor = 0.5
translation_x = 100
translation_y = 50

# Define the affine transformation matrix
# | scale_factor   0   translation_x |
# | 0   scale_factor   translation_y |
affine_matrix = np.float32([[scale_factor, 0, translation_x],
                            [0, scale_factor, translation_y]])

# Apply the affine transformation
affine_transformed_image = cv2.warpAffine(image, affine_matrix, (width, height))

# Display the original and transformed images
cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", affine_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
