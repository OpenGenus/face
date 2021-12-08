import os
import sys
import cv2
import numpy as np
import argparse

def readImage(path):
	print("Sample Images are being read from : " + path, flush=True)
	images = []
	for filepath in sorted(os.listdir(path)):
		extension = os.path.splitext(filepath)[1]
		if extension in [".jpg", ".jpeg"]:
			path_of_image = os.path.join(path, filepath)
			im = cv2.imread(path_of_image)
			if im is None :
				print("Error : {} Image can not be processed ".format(path_of_image))
			else :
				im = np.float32(im)/255.0
				images.append(im)
				imFlip = cv2.flip(im, 1);
				images.append(imFlip)
	number_of_images = len(images) / 2
	if number_of_images == 0 :
		print("ERROR : EMPTY FOLDER!")
		sys.exit(0)
	return images

def matrix(images):
	print("Data Matrix is being created", flush=True)
	number_of_images = len(images)
	sz = images[0].shape
	data = np.zeros((number_of_images, sz[0] * sz[1] * sz[2]), dtype=np.float32)
	for k in range(0, number_of_images):
		image = images[k].flatten()
		data[k,:] = image
	return data

def training():
	images = readImage(directory_name)
	sz = images[0].shape
	data = matrix(images)
	print("Principle Component Analysis Calculation under progress! ", flush=True)
	mean, eigenVectors = cv2.PCACompute(data, mean=None)
	print ("Calculations Completed!")
	filename = "pca_parameters.yml"
	file = cv2.FileStorage(filename, cv2.FILE_STORAGE_WRITE)
	file.write("mean", mean)
	file.write("eigenVectors", eigenVectors)
	file.write("size", sz)
	file.release()
	print("Values written in pca_parameters.yml successfully!")
