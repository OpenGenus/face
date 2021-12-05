# Finding set of faces when combined results in face of person A
This repository contains the code for the python project on “Finding set of faces when combined results in face of person A". 
- We start the application by opening the terminal in this folder and typing the command :  ```python main.py```
- The following 5 options are shown in the terminal. Then we would enter the number of the command of our choice between 1-5. : 
![image](https://user-images.githubusercontent.com/61888364/144733110-9caf58c2-0590-4ec6-ad54-ebae83dd9516.png)

- If we enter 1, then the model starts to train & following output is generated on the terminal : ![image](https://user-images.githubusercontent.com/61888364/144732121-b379c838-1e56-4a5f-a82e-6b2067fb9bdb.png)
- If we enter 2, then the collage of input/test images are printed on the output window. 
![image](https://user-images.githubusercontent.com/61888364/144732186-7c4011cf-36f1-4240-9463-73c37c2ca590.png) 
  - Output Window :
![image](https://user-images.githubusercontent.com/61888364/144733058-e0e21775-4821-4720-8e7a-640c2c9544f8.png)
- If we enter 3, then the mean face and first five eigen faces get printed on the output window one by one.
![image](https://user-images.githubusercontent.com/61888364/144732502-c1d58c7e-dde1-4262-9a46-db8a173d6caa.png)
  - The mean face is displayed on the output window.
![image](https://user-images.githubusercontent.com/61888364/144732992-b3d399ae-5206-4aa3-b374-f8bb26084eaa.png)
  - Then, all the five eigen faces will be displayed on the output window one by one. 

![image](https://user-images.githubusercontent.com/61888364/144732545-f885df83-889d-4f41-92fb-cf452f91d497.png)

- If we enter 4, then the trained model is read from pca_parameters.yml. 
  - Then the eigen vectors held in a structure of eigenVectors where eigen_face[i][j] = j-th eigen face of i-th image are displayed on the terminal as shown below.
  - Then we enter the name of image present in test folder in format: test/image_name.jpg. The image will be read and vectorized. After that the final results get displayed in new window. The final output window with original image on left and re-constructed image on right as described in the video below. 
  - It has a slider for increasing or decreasing the number of eigen faces used for reconstruction. By trying all combinations, we can dynamically see the best reconstructed image. 
  - The reconstructed image on the right dynamically changes with respect to the number of eigen faces chosen on slider.
![image](https://user-images.githubusercontent.com/61888364/144732336-c0efb3ad-28b6-4d88-90b5-cedc0cd67ba9.png)
  - ### **Output Window :**
https://user-images.githubusercontent.com/61888364/144326239-ee2a6e46-55ad-44cc-80ab-81f6305dc75d.mp4
 
- Finally to exit the terminal we must enter 5. If we enter any other value than 1 to 5 then "invalid mode" output will be displayed.
