# Importing the OpenCV library
# cv2 is the module name used to access OpenCV functions in Python
import cv2

source="rereizzes.jpg"
destination = "newImage.png"
scale_percent = 50 # This means resize to 50% of the original size

# Read an image from the file named 'harry.jpeg'
# cv2.IMREAD_UNCHANGED tells OpenCV to read the image as it is (including alpha channel if present)
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# (Optional) Show the image in a window titled "title"
# This is commented out to prevent the image window from opening automatically
# cv2.imshow("title", src)

# Set the percentage by which the image should be resized
 

# Calculate the new width of the image (50% of original width)
new_width = int(src.shape[1] * scale_percent / 100)

# Calculate the new height of the image (50% of original height)
new_height = int(src.shape[0] * scale_percent / 100)

# Resize the image using the new dimensions
# cv2.resize() takes the source image and a tuple (width, height)
output = cv2.resize(src, (new_width, new_height))

# Save the resized image to a new file named 'newImage.png'
cv2.imwrite(destination, output) # the new image will be half of the old imageh

