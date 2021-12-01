# Finding set of faces when combined results in face of person A
This repository contains the code for the python project on “Finding set of faces when combined results in face of person A". 
- We start by defining function reconstruction to recontruct face using mean face and EigenFaces. 
- Then we define function disp to display the final output window with original image on left and re-constructed image on right. 
- Then we start the main program by printing the collage of input/test images.
- After that we chose any specific image and printed the Mean face and show the resulting eigen faces for that image. ![Output1](https://user-images.githubusercontent.com/61888364/144326594-3083dd44-003c-468c-bcc8-eaaa5faa8ed0.PNG)

- Then, we read our trained model from pcaparameters.yml
- We create a structure of eigenVectors where eigen_face[i][j] = j-th eigen face of i-th image. As shown in image below : 

![Output2](https://user-images.githubusercontent.com/61888364/144326381-e631a083-ac33-4c29-b278-1b6ec0508db5.PNG)

- We start it by printing the eigenVectors stored in an array, read eigen faces and finally read and process the chosen test image.
- The result gets displayed in new window as described in the video below. It has a scroll bar for increasing or decreasing the number of eigen faces used for reconstruction. 
- By trying all combinations, we can dynamically see the best reconstructed image. The reconstructed image on the right dynamically changes with respect to the number of eigen faces chosen on scroll bar.

## Output Window :
https://user-images.githubusercontent.com/61888364/144326239-ee2a6e46-55ad-44cc-80ab-81f6305dc75d.mp4
