import cv2
import numpy as np

# Specify the paths to your source and target images
source_path = r".\source_image.jpg"
target_path = r".\target_image.jpg"

# Read the source and target images
source_image = cv2.imread(source_path)
target_image = cv2.imread(target_path)

# Ensure both images have the same size
source_image = cv2.resize(source_image, (target_image.shape[1], target_image.shape[0]))

# Define corresponding points in the source and target images
source_points = np.array([[50, 50], [300, 50], [50, 200], [300, 200]], dtype=np.float32)
target_points = np.array([[70, 80], [320, 60], [90, 230], [310, 210]], dtype=np.float32)

# Calculate the morphing parameters
num_frames = 30  # Adjust the number of frames for the animation
for frame in range(num_frames):
    morphing_percentage = frame / (num_frames - 1)  # Vary the percentage over frames

    # Interpolate points based on the morphing percentage
    interpolated_points = (1 - morphing_percentage) * source_points + morphing_percentage * target_points

    # Perform the morphing
    morphed_image = cv2.warpPerspective(source_image, cv2.getPerspectiveTransform(source_points, interpolated_points), (source_image.shape[1], source_image.shape[0]))

    # Display the morphed image
    cv2.imshow("Morphing Animation", morphed_image)
    cv2.waitKey(50)  # Adjust the delay between frames (in milliseconds)

cv2.destroyAllWindows()
