import cv2

image = cv2.imread("../test.png")

if image is None:
    print("Oops! Your image is not working")

else:
    print("Image loaded successfully!")

    pt1 = (50,100)
    pt2 = (300,300)
    color = (255, 0, 0)
    thickness = 10

    cv2.line(image, pt1, pt2, color, thickness)
    cv2.rectangle(image, pt1, pt2, color, thickness)

    cv2.imshow("Line Drawing" ,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()