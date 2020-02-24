import numpy as np 
import cv2 
from matplotlib import pyplot as plt 
  
img1 = cv2.imread('/home/wajih/Documents/M2/sift/slice007_2.bmp') 
img2 = cv2.imread('/home/wajih/Documents/M2/sift/slice009_1.bmp') 
     
gray1= cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY) 
gray2= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)                            

gray1= cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY) 
gray2= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) 
plt.imshow(gray1) 
plt.show() 
plt.imshow(gray2) 
plt.show()                                                              

sift = cv2.xfeatures2d.SIFT_create()                                    

kp1 = sift.detect(gray1,None)                                           

kp2 = sift.detect(gray2,None)                                           

imgg1 = cv2.drawKeypoints(gray1,kp1,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)                                                     


imgg2 = cv2.drawKeypoints(gray2,kp2,None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)                                                    

cv2.imwrite('sift_keypointsessai1.jpg',imgg1)                          
#Out[10]: True

cv2.imwrite('sift_keypointsessai2.jpg',imgg2)                          
#True

plt.imshow(imgg1) 
plt.show() 
plt.imshow(imgg2) 
plt.show()  
######## 
#/home/wajih/sift_keypointsessai1.jpg
#/home/wajih/sift_keypointsessai2.jpg


# create a BFMatcher object which will match up the SIFT features
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

matches = bf.match(imgg1, imgg2)

# Sort the matches in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# draw the top N matches
N_MATCHES = 100

match_img = cv2.drawMatches(
    img1, kp1,
    img2, kp2,
    matches[:N_MATCHES], img2.copy(), flags=0)

plt.figure(figsize=(12,6))
plt.imshow(match_img);




