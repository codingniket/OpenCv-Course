import cv2

image = cv2.imread("test.png")

if image is not None:
    h,w,c = image.shape
    print(f"Image shape: Height={h}, Width={w}, Channels={c}")
else:
    print("Error: Could not read image.")

# Changing to grayscale
if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not convert image to grayscale.")

