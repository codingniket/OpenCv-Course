import cv2

image = cv2.imread('../test.png')

if image is not None:
    write = cv2.putText(image, 'Hello, OpenCV!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('Image', write)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found.")