import cv2 

image = cv2.imread("../test.png")

if image is None:
    print("Error: Could not read image.")
else:
    print("Image read successfully.")
    # Resize
    # resize = cv2.resize(image, (200, 200))
    # Crop
    cropped = image[50:150, 50:150]
    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped Image", cropped)
    cv2.imwrite("test_cropped.png", cropped)
    # cv2.imshow("Resized Image", resize)
    # cv2.imwrite("test_resized.png", resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
