import cv2

print("Give the file location as input")

file_location = input()

image = cv2.imread(file_location)

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
else:
    print("Error: Could not convert image to grayscale.")

print("Press 1 to save\nPress 2 to show")

choice = input()

if choice == "1":
    if gray is not None:
        print("Provide filename please")
        file_name = input()
        success = cv2.imwrite(f"{file_name}.png", gray)
        if success:
            print("Image saved successfully.")
        else:
            print("Error: Could not save image.")
    else:
        print("Error: Could not read image.")

elif choice == "2":
    if gray is not None:
        cv2.imshow("Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Could not display image.")
