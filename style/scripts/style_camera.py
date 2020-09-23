#! /usr/bin/env python3

import cv2
net = cv2.dnn.readNetFromTorch('./src/style/model/the_scream.t7')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV);

cap = cv2.VideoCapture(0)

cv2.namedWindow('Styled image', cv2.WINDOW_NORMAL)
h = 200
w = 300
	
while cv2.waitKey(1) < 0:
	hasFrame, frame = cap.read()
    #if not hasFrame:
       # cv2.waitKey()
       # break
	blob = cv2.dnn.blobFromImage(frame, 1.0, (w, h), (103.939, 116.779, 123.680), swapRB=False, crop=False)
	net.setInput(blob)
	out = net.forward()
	out = out.reshape(3, out.shape[2], out.shape[3])
	out[0] += 103.939
	out[1] += 116.779
	out[2] += 123.68
	out /= 255
	out = out.transpose(1, 2, 0)
	cv2.imshow('Styled image' , out)
