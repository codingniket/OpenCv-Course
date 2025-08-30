import cv2

image = cv2.imread('test.png')
# image = cv2.imread('image.jpg',flag)
# flag is optinal 1 = color 0 = greyscale -1 = unchanged

if image is None:
    print("Error: Could not load image.")
else:
    print("Success")