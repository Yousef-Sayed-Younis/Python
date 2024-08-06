import cv2
import numpy as np

# Importing img 
# img = cv2.imread("C:/Users/Yousef Sayed/Desktop/Coding/Python/New/Resources/photo.png")

# kernal = np.ones((5,5), np.uint8)

# Showing the img
# cv2.imshow("Output", img)
# cv2.waitKey()

# Importing video
# vid = cv2.VideoCapture("Path")

# Showing video in loop "because vid. is made of lot of images"
# while True: # The loop that show vid.
#     success, img = vid.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord("q"): # To close vid.
#         break


# Importing webcam
# cam = cv2.VideoCapture(0)
# cam.set(3,640) # Define the Width which his id = 3
# cam.set(4,480) # Define the Height which his id = 4
# cam.set(10,100) # Define the Brightness which his id = 10

# while True: # The loop that show vid.
#     success, img = cam.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord("q"): # To close vid.
#         break


# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Make the image Gray
# imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) # Make the image Blur and the countity of blur in (,) and sigmax after it
# imgCanny = cv2.Canny(img, 200, 200) # Make the image Black Lines and its quality
# imgDilation = cv2.dilate(imgCanny, kernal, iterations=1) # Make the image dialte or more wider
# imgEroded = cv2.erode(imgDilation, kernal, iterations=1) # Make the image eroded

# cv2.imshow("Gray img", imgGray)
# cv2.imshow("Blur img", imgBlur)
# cv2.imshow("Canny img", imgCanny)
# cv2.imshow("Dilation img", imgDilation)
# cv2.imshow("Eroded img", imgEroded)
# cv2.waitKey()


# Resizing And Cropping
# print(img.shape) # Image size

# imgResize = cv2.resize(img, (300,200)) # Resizing image Width and Height
# imgCropped = img[0:200, 200:500] # Cropping image Height and Width

# cv2.imshow("Image", img)
# cv2.imshow("Image Resized", imgResize)
# cv2.imshow("Image Cropped", imgCropped)
# cv2.waitKey()



# Shapes And Texts
# img = np.zeros((512, 512, 3), np.uint8)
# # img[:] = 0,0,255 # Color the image

# cv2.line(img, (0,0),(512, img.shape[0]),(0,0,255), 3) # Make Line in img start from(), to(), itsColor(), itsThickness
# cv2.rectangle(img, (0,0), (250,350), (255,0,0), cv2.FILLED) # Make rectangle
# cv2.circle(img, (400,50), 30, (0,255,0), 5) # Make circle
# cv2.putText(img, "Hehe", (300,100), cv2.FONT_HERSHEY_COMPLEX, 1, (250,25,200), 2) # Make Text

# cv2.imshow("image", img)
# cv2.waitKey()



# Warp Prespective
# img = cv2.imread("C:/Users/Yousef Sayed/Desktop/Coding/Python/New/Resources/cards.jpg")

# print(img.shape)
# width, height = 170,297
# pts1 = np.float32([[214,15],[287,62],[148,128],[223,170]]) # Rotates clockwise
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# cv2.imshow("Image", img)
# cv2.imshow("Output", imgOutput)
# cv2.waitKey()



# Joining Images
# We can not join more than 3 images or 2 img with different type(gray,black,BGR) but there is a function(stackImages) can solve that
# img = cv2.imread("C:/Users/Yousef Sayed/Desktop/Coding/Python/New/Resources/photo.png")

# horImg = np.hstack((img, img))
# verImg = np.vstack((img, img))

# cv2.imshow("Horizontal", horImg)
# cv2.imshow("Vertical", verImg)
# cv2.waitKey()



# Color Detection
# def empty(x):
#     pass

# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars", 640,240)
# cv2.createTrackbar("Hue Min", "TrackBars", 90, 179, empty)
# cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
# cv2.createTrackbar("Sat Min", "TrackBars", 221, 255, empty)
# cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
# cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
# cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
# img = cv2.imread("C:/Users/Yousef Sayed/Desktop/Coding/Python/New/Resources/photo.png")

# while True:
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     hMin = cv2.getTrackbarPos("Hue Min", "TrackBars")
#     hMax = cv2.getTrackbarPos("Hue Max", "TrackBars")
#     sMin = cv2.getTrackbarPos("Sat Min", "TrackBars")
#     sMax = cv2.getTrackbarPos("Sat Max", "TrackBars")
#     vMin = cv2.getTrackbarPos("Val Min", "TrackBars")
#     vMax = cv2.getTrackbarPos("Val Max", "TrackBars")

#     lower = np.array([hMin, sMin, vMin])
#     upper = np.array([hMax, sMax, vMax])
#     mask = cv2.inRange(imgHSV, lower, upper)
#     imgResult = cv2.bitwise_and(img, img, mask=mask)

# # We can Join all by Fun.(stackImages)
#     cv2.imshow("Img", img)
#     cv2.imshow("HSV", imgHSV)
#     cv2.imshow("Mask", mask)
#     cv2.imshow("Result", imgResult)
#     cv2.waitKey(1)



# Contours / Shape Detection
# def getContours(img):
#     contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         print(area)
#         if area > 500:
#             cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3)
#             peri = cv2.arcLength(cnt, True)
#             # print(peri)
#             approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
#             print(len(approx))
#             objCor = len(approx)
#             x, y, w, h = cv2.boundingRect(approx)
            
#             if objCor == 3: objectType = "Tri" # For Tringle
#             elif objCor == 4:
#                 aspRatio = w/float(h)
#                 if aspRatio > 0.95 and aspRatio < 1.05: objectType = "Sqr"
#                 else: objectType = "Rec"
#             elif objCor > 4: objectType = "Circ"
#             else: objectType = "None"

#             cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0,255,0), 2)
#             cv2.putText(imgContour, objectType, 
#             (x+(w//2)-15, y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)

# img = cv2.imread("C:/Users/Yousef Sayed/Desktop/Coding/Python/New/Resources/shapes.png")
# imgContour = img.copy()

# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
# imgCanny = cv2.Canny(imgBlur, 50, 50)
# imgBlanck = np.zeros_like(img)
# getContours(imgCanny)


# cv2.imshow("Original", img)
# cv2.imshow("Gray", imgGray)
# cv2.imshow("Blur", imgBlur)
# cv2.imshow("Canny", imgCanny)
# cv2.imshow("Blanck", imgBlanck)
# cv2.imshow("Contour", imgContour)
# cv2.waitKey()



# Face Detection
faceCascade = cv2.CascadeClassifier("C:/Users/Yousef Sayed/Desktop/Coding/Python/New/Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("C:/Users/Yousef Sayed/Desktop/Coding/Python/New/Resources/girl.jpg")
imgResized = cv2.resize(img, (800,700))
imgGray = cv2.cvtColor(imgResized, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(imgResized, (x, y), (x+w, y+h), (255,0,0), 2)

cv2.imshow("Image", imgResized)
cv2.waitKey()

