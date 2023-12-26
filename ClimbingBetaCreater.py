import cv2
import matplotlib.pyplot as plt

climbColor = input("Enter color of the climb: ")

# Load the image in BGR format
raw = cv2.imread('C:/Users/londo/Documents/github/coDing/Climbing/climbing.jpg')

# Convert BGR to RGB
image = cv2.cvtColor(raw, cv2.COLOR_BGR2RGB)

# lightOrange = (1, 190, 200)
lightOrange = (1,170,150)
darkOrange = (18, 255, 255)

lightBlue = (200, 200, 200)
lightYellow = (255, 255, 255)

# Convert the image to grayscale
imageGray = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)

# Threshold the grayscale image to obtain a mask for white color
_, tagMask = cv2.threshold(imageGray, 235, 255, cv2.THRESH_BINARY)

hsvImage = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# tagMask = cv2.inRange(hsvImage, lightBlue, lightYellow)
holdMask = cv2.inRange(hsvImage, lightOrange, darkOrange)
combined_mask = cv2.bitwise_or(tagMask, holdMask)

result = cv2.bitwise_and(image, image, mask=combined_mask)
plt.imshow(result)
plt.show()

