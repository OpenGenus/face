# Finding set of faces when combined results in face of person A
This repository contains the code for the python project on [“Finding set of faces when combined results in face of person A"](https://iq.opengenus.org/project-on-reconstructing-face/). <br>

**The project has been published as a [pip package](https://pypi.org/project/face-recons/0.0.1/) and can be installed by running ```pip install face-recons==0.0.1``` in terminal.**
<br>

**After successfully installing the package, user can enter python interpreter and enter ```from face_recons import main```. Following it they will enter the Default Mode of the application.**

**The default mode of the application is interactive mode which is user friendly. The other mode is Command Line Interface.**

## Default Mode (Interactive Mode): 
The detailed Flow of Code for our Interactive or Default Mode is below :

![flow_chart](https://user-images.githubusercontent.com/61888364/144736192-361c955c-8b2c-4f47-b6cd-1ce5ac78360e.png)

- We start the application by opening the python interpreter and typing the command :  ```from face_recons import main```
- The following 5 options are shown in the terminal. Then we would enter the number of the command of our choice between 1-5. : 
![image](https://user-images.githubusercontent.com/61888364/144733110-9caf58c2-0590-4ec6-ad54-ebae83dd9516.png)

- If we enter 1, the directory for training dataset is asked. Then the model starts to train & following output is generated : <br>
![image](https://user-images.githubusercontent.com/61888364/145155249-5ded11e3-9860-4f55-8a8e-512bed106870.png)

- If we enter 2, then the full file path to test directory is asked. Then the collage of input/test images are printed as output on terminal: <br>
![option2](https://user-images.githubusercontent.com/61888364/145155791-39ec58ae-1eef-4bab-9bbc-214617b63282.png)
  - Output Window : <break>
![image](https://user-images.githubusercontent.com/61888364/144733058-e0e21775-4821-4720-8e7a-640c2c9544f8.png)
- If we enter 3, then the mean face and first five eigen faces get printed on the output window one by one.
![image](https://user-images.githubusercontent.com/61888364/144732502-c1d58c7e-dde1-4262-9a46-db8a173d6caa.png)
  - The mean face is displayed on the output window.
![image](https://user-images.githubusercontent.com/61888364/144732992-b3d399ae-5206-4aa3-b374-f8bb26084eaa.png)
  - Then, all the five eigen faces will be displayed on the output window one by one. 

![image](https://user-images.githubusercontent.com/61888364/144732545-f885df83-889d-4f41-92fb-cf452f91d497.png)

- If we enter 4, then the trained model is read from pca_parameters.yml. 
  - Then the eigen vectors held in a structure of eigenVectors where eigen_face[i][j] = j-th eigen face of i-th image are displayed on the terminal as shown below.
  - Then we enter the name of folder with image in format: directory/image_name.jpg. The image will be read and vectorized. After that the final results get displayed in new window. The final output window with original image on left and re-constructed image on right as described in the video below. 
  - It has a slider for increasing or decreasing the number of eigen faces used for reconstruction. By trying all combinations, we can dynamically see the best reconstructed image. 
  - The reconstructed image dynamically changes with respect to the number of eigen faces chosen on slider.
  - The percentage of Eigen Faces used for reconstructing output image is dynamically printed on the terminal as we move the slider. <br>
![image](https://user-images.githubusercontent.com/61888364/145156635-ee8d89f8-f1b3-4ab9-b631-abab8787266a.png)

  - ### **Output Window :**
https://user-images.githubusercontent.com/61888364/144326239-ee2a6e46-55ad-44cc-80ab-81f6305dc75d.mp4
 
- Finally to exit the terminal we must enter 5. If we enter any other value than 1 to 5 then "invalid mode" output will be displayed.

## Mode 1 (Command Line Interface)
If we wish to use the Command Line Interface, we can do so by typing the following command :
  ```
  python main.py --mode 1 --input directory/image.jpg --dataset directory
  ```
**We can enter mode = 1 for CLI mode, the directory/image.jpg for the Test Image and the directory for the Training Dataset.**

- In the below example, we entered test/300000.jpg for Test Image and  sample2 for Training Dataset. 
- The model is trained from the pca_parameters.yml and the Test Image is reconstructed. 
- The percentage of Eigen Faces used to reconstruct the output image is dynamically printed on terminal as we slide the slider.

![CLI](https://user-images.githubusercontent.com/61888364/145159037-71a3d602-510c-418d-be9c-af3617968d27.png)
  
- Same Output Window of Reconstructed Image is displayed in CLI mode as seen in Interactive Mode.
