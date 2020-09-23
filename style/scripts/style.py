#! /usr/bin/env python3

import cv2
models = [
    'starry_night.t7',
    'the_wave.t7',
    'the_scream.t7',
    'composition_vii.t7',
]
nets = []
for i in range(len(models)):
    net = cv2.dnn.readNetFromTorch('./src/style/model/' + models[i])
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV);
    nets.append(net)

#cap = cv2.VideoCapture(0)

cv2.namedWindow('Styled image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Sample')
simage = cv2.imread('./src/style/photo/Sample.PNG')
cv2.imshow('Sample' , simage)
image = cv2.imread('./src/style/photo/test.jpg')
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(image, 1.0, (w, h), (103.939, 116.779, 123.680), swapRB=False, crop=False)
for i in range(len(nets)):
	net=nets[i]
	net.setInput(blob)
	out = net.forward()
	out = out.reshape(3, out.shape[2], out.shape[3])
	out[0] += 103.939
	out[1] += 116.779
	out[2] += 123.68
	out /= 255
	out = out.transpose(1, 2, 0)
	cv2.imshow('Styled image %d' %i, out)
cv2.waitKey(0)
