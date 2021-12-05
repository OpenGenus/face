import os
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.image import imread
from PIL import Image as im
    
def print_test():
	dataset_path = 'test/'
	dataset_dir  = os.listdir(dataset_path)
	width  = 178
	height = 218
	test_image_names = dataset_dir
	testing_tensor   = np.ndarray(shape=(len(test_image_names), height*width), dtype=np.float64)
    
    # Print the test images
	print("Printed the Input Images. Check the output window for final results.\n")
	for i in range(len(test_image_names)):
		img = imread(dataset_path + test_image_names[i])
		plt.subplot(3,6,1+i)
		plt.title(test_image_names[i].split('.')[0][-2:]+test_image_names[i].split('.')[1])
		plt.imshow(img, cmap='gray')
		plt.subplots_adjust(right=1.000, top=1.000)
		plt.tick_params(labelleft='off', labelbottom='off', bottom='off',top='off',right='off',left='off', which='both')
	plt.show()
    
def print_eigen():  
	neutral = []
	for i in range(9):
		i+=1
		img = im.open(f'sample/00000{i}.jpg').convert('L')
		img = img.resize((58,49), im.ANTIALIAS)
		img2 = np.array(img).flatten() # vectorization
		neutral.append(img2)
	faces_matrix = np.vstack(neutral)
	mean_face = np.mean(faces_matrix, axis=0)
	plt.imshow(mean_face.reshape(49,58),cmap='gray'); 
	print('Printed Mean Face. Check the output window for final results.\n ')    
	plt.title('Mean Face')  
	plt.show()

    
    #print 5 eigen faces    
	faces_norm = faces_matrix - mean_face ### normalization
	faces_norm = faces_norm.T
	face_cov = np.cov(faces_norm)
	eigen_vecs, eigen_vals, _ = np.linalg.svd(faces_norm)


	for i in np.arange(5):
		img = eigen_vecs[:,i].reshape(49,58)
		plt.imshow(img, cmap='gray')
		print('Printed Eigen Face ',i+1,' on the output window\n ')
		plt.title('Eigen Face :')  
		plt.show()
    
def recons():
	def reconstruction(*args):
		final_output = average_face
		for k in range(0,args[0]):
			weight = np.dot(imVector, eigenVectors[k])
			final_output = final_output + eigen_face[k] * weight
		disp(im, final_output)
        
	def disp(x, y):
		final_output = np.hstack((x,y))	
		final_output = cv2.resize(final_output, (0,0), fx=3, fy=3)
		cv2.imshow("Result", final_output)
        
    # Read the model from pcaparameters.yml
	model = "pca_parameters.yml"
	print("The Model is being Read from pca_parameters.yml", flush=True)
	file = cv2.FileStorage(model, cv2.FILE_STORAGE_READ)
	mean = file.getNode("mean").mat()

	eigenVectors = file.getNode("eigenVectors").mat()
    
    # show eigen vectors
	print("Eigen Vectors  :")
	print(eigenVectors)
    
    # Read eigen faces
	sz = file.getNode("size").mat()
	sz = (int(sz[0,0]), int(sz[1,0]), int(sz[2,0]))
	number_of_eigen_faces = eigenVectors.shape[0]
	print("Reading Finished.")
	average_face = mean.reshape(sz)
    
	eigen_face = [] 
    
    #obtain eigenfaces 
	for eigenVector in eigenVectors:
		eigenFace = eigenVector.reshape(sz)
		eigen_face.append(eigenFace) 
    

	image_file = input('Enter the name of image present in test folder in format: test/image_name.jpg\n')
    # read test image & process it
	# example of image_file = "test/300000.jpg"
	print("Test Image is being read and vectorized!")
	eigen_vec=[]
	im = cv2.imread(image_file)
	im = np.float32(im)/255.0
	imVector = im.flatten() - mean;
	eigen_vec.append(imVector)
	print("Process Finished. Check the output window for final results.")
	final_output = average_face
	cv2.namedWindow("Result", cv2.WINDOW_AUTOSIZE)
	cv2.createTrackbar("EigenFaces", "Result", 0, number_of_eigen_faces, reconstruction)
	disp(im, final_output)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
