import os
import sys
import cv2
import numpy as np

def reconstruction(*args):
	final_output = average_face
	for k in range(0,args[0]):
		weight = np.dot(imVector, eigenVectors[k])
		final_output = final_output + eigenFaces[k] * weight
	disp(im, final_output)
    
def disp(x, y):
	final_output = np.hstack((x,y))	
	final_output = cv2.resize(final_output, (0,0), fx=4, fy=4)
	cv2.imshow("Result", final_output)

if __name__ == '__main__':
	model = "pca_parameters.yml"
	print("The Model is being Read from pca_parameters.yml", flush=True)
	file = cv2.FileStorage(model, cv2.FILE_STORAGE_READ)
	mean = file.getNode("mean").mat()
	eigenVectors = file.getNode("eigenVectors").mat()
	sz = file.getNode("size").mat()
	sz = (int(sz[0,0]), int(sz[1,0]), int(sz[2,0]))
	number_of_eigen_faces = eigenVectors.shape[0]
	print("Reading Finished.")
	average_face = mean.reshape(sz)
	eigenFaces = [] 
	
  for eigenVector in eigenVectors:
		eigenFace = eigenVector.reshape(sz)
		eigenFaces.append(eigenFace) 
	
  image_file = "test/000223.jpg"
	print("Test Image is being read and vectorized!");
	im = cv2.imread(image_file)
	im = np.float32(im)/255.0
	imVector = im.flatten() - mean; 
	print("Process Finished. Check the output window for final results.");
	final_output = average_face
	cv2.namedWindow("Result", cv2.WINDOW_AUTOSIZE)
	cv2.createTrackbar( "No. of EigenFaces", "Result", 0, number_of_eigen_faces, reconstruction)
	disp(im, final_output)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
