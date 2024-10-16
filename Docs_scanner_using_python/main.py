import cv2
import numpy as np
import mapper

image = cv2.imread("test.jpg")
image = cv2.resize(image,(1300,880))
orig = image.copy()

#here we gray the image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Title-gray",gray)


#here we blur the image using gaussian blur system
blurred = cv2.GaussianBlur(gray,(5,5),0)
#cv2.imshow("GaussianBlur",blurred)


#here is the edge detection system
edged = cv2.Canny(blurred,30,50)
#cv2.imshow("Canny",edged)

image, contours = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"Total number of contours found: {len(contours)}")

valid_contours = []
for i, c in enumerate(contours):
    print(f"Examining contour {i}")
    
    # Check if the contour has any points
    if len(c) == 0:
        print(f"Contour {i} is empty")
        continue
    
    # Try to calculate the area
    try:
        area = cv2.contourArea(c)
        print(f"Contour {i} area: {area}")
        
        # Check if the area is valid
        if area > 10000:  # Adjust this threshold as needed
            valid_contours.append((area, c))
        else:
            print(f"Contour {i} has too small area")
    except cv2.error as e:
        print(f"Error calculating area for contour {i}: {e}")

print(f"Number of valid contours found: {len(valid_contours)}")
contours = sorted(valid_contours, key=lambda x: x[0], reverse=True)

if len(contours) > 0:
    # Get the largest contour
    _, largest_contour = contours[0]
    
    # Approximate the polygon
    p = cv2.arcLength(largest_contour,True)
    approx = cv2.approxPolyDP(largest_contour,0.02*p,True)
    
    # Check if it's a quadrilateral
    if len(approx) == 4:
        target = approx
        print("Found a quadrilateral contour")
        
        # Apply perspective transform
        approx = mapper.mapp(target)
        pts= np.float32([[0,0],[800,0],[800,800],[0,800]])
        op = cv2.getPerspectiveTransform(approx,pts)
        dst = cv2.warpPerspective(orig,op,(800,800))
        cv2.imshow("Scanned final",dst)
    else:
        print(f"Found contour with {len(approx)} sides")
else:
    print("No valid contours found")

cv2.waitKey(0)
cv2.destroyAllWindows()