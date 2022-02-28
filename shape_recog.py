import cv2
import numpy as np
from matplotlib import pyplot as plt

def find_shape(approx):
  x, y, width, height = cv2.boundingRect(approx)

  if len(approx) == 3:
    shape = "Triangle"
  
  elif len(approx) == 4:
    area = width / float(height)
    if area >= 0.95:
      shape = "Square"
    else:
      shape = "Rectangle"
    
  elif len(approx) == 5:
    shape = "Pentagon"
  
  elif len(approx) == 8:
    shape = "Octagon"

  elif 9 < len(approx) < 15:
    shape = "Ellipse"
    
  else:
    shape = "Circle"
  
  return shape, x, y, width, height

# reading image
orig = cv2.imread('samples/2-min.png', cv2.IMREAD_UNCHANGED)


img = orig.copy()

# img = cv2.equalizeHist(img)
# cv2.imwrite('samples/equalized-color.png',img)

# converting image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('samples/gray.png',gray)

# # # Equalization
# equalized = cv2.equalizeHist(gray)
# cv2.imwrite('samples/equalized.png',equalized)

# # # Blur
blur = cv2.GaussianBlur(gray, (5, 5), 1)

#bilateral_filtered_image = cv2.bilateralFilter(gray, 5, 175, 175)

# Canny Edge Detection
edges = cv2.Canny(blur, 80, 100) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imwrite('samples/canny.png',edges)

# kernel = np.ones((3))
# dilated = cv2.dilate(edges, kernel, iterations=1)
# cv2.imwrite('samples/dilated.png',dilated)

# setting threshold of gray image
#_, threshold = cv2.threshold(edges, 230, 255, cv2.THRESH_BINARY)

# using a findContours() function
contours, _ = cv2.findContours(
	edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

i = 0

contour_list = []

# list for storing names of shapes
for contour in contours:
    print("Contour detected!")
    # here we are ignoring first counter because
    # findcontour function detects whole image as shape
    # if i == 0:
    #     i = 1
    #     continue
    
    # hull = cv2.convexHull(contour)

    #cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(
        contour, 0.04 * cv2.arcLength(contour, True), True)

    area = cv2.contourArea(contour)
    print(len(approx))
    print(area)
    # if area > 1:

    shape, x, y, w, h = find_shape(approx)
    cv2.putText(orig, shape, (x+30, y+150), cv2.FONT_HERSHEY_COMPLEX, .7, (255, 0, 255), 1)
    
    # if len(shape) > 0:
    contour_list.append(contour)

cv2.drawContours(orig, contour_list, -1, (255, 0, 255), 1)

cv2.imwrite('samples/image.png',orig)

# displaying the image after drawing contours
# cv2.imshow('shapes', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()