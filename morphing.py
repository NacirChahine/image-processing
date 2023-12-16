import cv2
import numpy as np

# Specify the paths to your source and target images
source_path = r"C:\Users\nacwo\Desktop\open cv sample\source_image.jpg"
target_path = r"C:\Users\nacwo\Desktop\open cv sample\target_image.jpg"

# Read the source and target images
source_image = cv2.imread(source_path)
target_image = cv2.imread(target_path)

# Ensure both images have the same size
source_image = cv2.resize(source_image, (target_image.shape[1], target_image.shape[0]))

# Define corresponding points in the source and target images
source_points = np.array([[50, 50], [300, 50], [50, 200], [300, 200]], dtype=np.float32)
target_points = np.array([[70, 80], [320, 60], [90, 230], [310, 210]], dtype=np.float32)

# Calculate the morphing parameters
morphing_percentage = 0.5  # Adjust the percentage for different morphing stages
interpolated_points = (1 - morphing_percentage) * source_points + morphing_percentage * target_points

# Perform the morphing
morphed_image = cv2.warpPerspective(source_image, cv2.getPerspectiveTransform(source_points, interpolated_points), (source_image.shape[1], source_image.shape[0]))

# Display the source, target, and morphed images
cv2.imshow("Source Image", source_image)
cv2.imshow("Target Image", target_image)
cv2.imshow("Morphed Image", morphed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
