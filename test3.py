import time

import cv2 as cv
from rembg import remove

# reading image and displaying original image
input_image_path = './TEST IMAGES/1.jpg' # change this to take input from user

img = cv.imread(input_image_path)
cv.namedWindow("Input_Image", cv.WINDOW_NORMAL)
cv.imshow("Input_Image", img)
cv.waitKey(0)
# cv.destroyWindow("Input_Image")
# drawing ROI and extracting it
cv.namedWindow("Select ROI", cv.WINDOW_NORMAL)
roi = cv.selectROI("Select ROI", img)
cropped = img[int(roi[1]) : int(roi[1] + roi[3]), int(roi[0]): int(roi[0] + roi[2])]
print(roi[0], roi[1], roi[2], roi[3])
cv.destroyWindow("Select ROI")
cv.namedWindow("Selected ROI", cv.WINDOW_NORMAL)
cv.imshow("Selected ROI", cropped)
cv.waitKey(0)
cv.destroyWindow("Selected ROI")

# Background removal
bg_removed = remove(cropped)
print(bg_removed.shape)
cv.namedWindow("Background Removed", cv.WINDOW_NORMAL)
cv.imshow('Background Removed', bg_removed)
cv.waitKey(0)
cv.destroyWindow("Background Removed")

# draw outline
bg_removed_copy = bg_removed.copy()
color = (255, 0 , 0)
thickness = 5
radius = 5
last_pt = (0,0)
outline_points = []
def draw_outline(event, x,y, flags, param):
    global last_pt, outline_points
    if event == cv.EVENT_LBUTTONDOWN: # if mouse button is being pressed
        last_pt = (x, y)
        outline_points.append(last_pt)
        # cv.circle(bg_removed, (x,y), radius, color, thickness)
    elif event == cv.EVENT_MOUSEMOVE and flags & cv.EVENT_FLAG_LBUTTON: # if mouse moves and button is pressed
        cv.line(bg_removed_copy, last_pt, (x,y), color, thickness )
        last_pt = (x, y)
        outline_points.append(last_pt)
cv.namedWindow('Draw Outline', cv.WINDOW_NORMAL)
cv.setMouseCallback('Draw Outline', draw_outline)

while True:
    cv.imshow('Draw Outline', bg_removed_copy)
    # print('printing')
    if cv.waitKey(1) & 0xFF == ord('q'):
        print('q pressed')
        break
    if cv.waitKey(1) & 0xFF == ord('c'):
        print('C pressed')
        bg_removed_copy = bg_removed.copy()
        outline_points = []

# transferring the oultine to the original image
Hfactor =  img.shape[0] / cropped.shape[0]
Wfactor = img.shape[1] / cropped.shape[1]
print(Hfactor, Wfactor)
cv.namedWindow("Final Image", cv.WINDOW_NORMAL)
for i in range(len(outline_points) - 1):
    #cv.circle(img, (outline_points[i][0] + roi[0], outline_points[i][1] + roi[1]), 5, color, -1) # Thickness = -1 for inward filling
    cv.line(img, (outline_points[i][0] + roi[0],outline_points[i][1] + roi[1] ), (outline_points[i+1][0] + roi[0],outline_points[i+1][1] + roi[1] ) , color, thickness)
    print(outline_points[i], outline_points[i+1])
    # Uncomment this to see th e final image updation in real time.
    # cv.imshow("Final Image", img)
    # if cv.waitKey(5) & 0xFF == ord('q'):
    #     print('q pressed')
    #     break

cv.namedWindow("Final Image", cv.WINDOW_NORMAL)
cv.imshow("Final Image", img)
cv.waitKey(0)

cv.destroyAllWindows()
