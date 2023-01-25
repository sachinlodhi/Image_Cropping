import cv2
import cv2 as cv
import rembg
import numpy as np
# Read the input image
image_path = 'TEST IMAGES/1.jpg'  # specify the input image path here
image = cv2.imread(image_path)
cv.namedWindow('Input Image', cv.WINDOW_NORMAL)
cv.namedWindow('Output Image', cv.WINDOW_NORMAL)
# Display the image
cv2.imshow('Input Image', image)

while True:
    # Ask the user to draw a rectangle over an object in the image
    r = cv2.selectROI('Input Image', image)

    # Crop the selected Region Of Interest (ROI) and pass it to the Rembg library
    roi = image[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    object_image = rembg.remove(roi)

    # Draw an outline over the object
    object_outline = cv2.Canny(object_image, 100, 200)



    object_outline = cv2.resize(object_outline, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_NEAREST)
    object_outline = object_outline.astype(image.dtype)

    # Overlay the object outline in the original input image and show it as output
    image_outline = cv2.bitwise_and(image, image, mask=object_outline)
    cv2.imshow('Output Image', image_outline)

    # Wait for user input
    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):  # exit the loop if 'q' is pressed
        break
    elif key == ord('c'):  # clear the outline if 'c' is pressed
        image_outline = np.copy(image)

cv2.destroyAllWindows()