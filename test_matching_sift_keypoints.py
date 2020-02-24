import numpy as np
import cv2
from matplotlib import pyplot as plt
	
MIN_MATCH_COUNT = 10
    
img1 = cv2.imread('/home/wajih/Documents/M2/sift/slice009_1.bmp')        
img2 = cv2.imread('/home/wajih/Documents/M2/sift/slice007_2.bmp')          
# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()
    
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
    
#FLANN_INDEX_KDTREE = 0
#index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
#search_params = dict(checks = 50)
    
#flann = cv2.FlannBasedMatcher(index_params, search_params)
#d = des1.shape   
#print(d) 
#d = des2.shape   
#print(d) 
#matches = flann.knnMatch(des1,des2,k=2)
#matches = flann.knnMatch(np.asarray(des1,np.float32),np.asarray(des2,np.float32),2)    
# store all the good matches as per Lowe's ratio test.
#good = []
#for m,n in matches:
#	if m.distance < 0.7*n.distance:
#        	good.append(m)

bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
matches = bf.match(kp1, kp2)
