##importing libraries#####
import cv2
import os
import matplotlib.pyplot as plt
path = "image.png" #your img path
img = cv2.imread(path) 
#clahe applying 
clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(1,1))
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
l, a, b = cv2.split(lab)  # split on 3 different channels
l2 = clahe.apply(l)  # apply CLAHE to the L-channel
lab = cv2.merge((l2,a,b))  # merge channels
img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR
#fig, ax = plt.subplots()
#ax.imshow(img2, cmap=plt.cm.gray)
cv2.imwrite('savingpathe/newimgname.jpg',img2)

