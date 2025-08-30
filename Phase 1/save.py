import cv2

image = cv2.imread("test.png")

if image is not None:
    success = cv2.imwrite("test_copy.png", image)
    if success:
        print("Image saved successfully.")
    else:
        print("Error: Could not save image.")
else:
    print("Error: Could not read image.")