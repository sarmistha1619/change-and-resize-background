import cv2 as cv

red = 0
green = 255
blue = 0
alpha = 255

Image = cv.imread("img.jpg", cv.IMREAD_UNCHANGED)

t_mask = image[:,:,3]==0

Image[t_mask]=[blue, green, red, alpha]

print(Image.shape)

resized = cv.resize(Image, None, fx=0.1, fy=0.1)

cv.imshow('windows', resized)

cv.waitkey(0)