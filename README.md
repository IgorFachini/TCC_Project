# TCC_Project
Image recognition for standalone robots. [TCC demo files](https://drive.google.com/drive/folders/1qEAn8uT8I_mubZsbaL5ZFzVQfkGnkjXY?usp=sharing)

# Usage
WITH PYTHON 3
> python server_socket.py <br>
> python client_socket.py


# IMPORTANT

To test this code, download the remaining [files](https://drive.google.com/drive/folders/1h2Adn51Qroy4c28bU-WqoYPwIjTeI3aW?usp=sharing).

Download the folder named "data" and put it in this repository.

## Significance of the folders and files

-- **Important** --

**data**             - (When Downloaded) Data folder contains, models, and images used in the code. <br>
**client_socket.py** - Client used to capture images.<br>
**server_socket.py** - Server used to compute received images from client.<br>
**requirements.txt** - List of libraries to run this project.<br>

-- **Not Important** -- 

**lab_test.py** - Experimental codes for testing.<br>
**client_http.py** - Experimental HTTP Client used to capture images.<br>
**server_http.py** - Experimental HTTP Server with end-point used to compute received images.<br>



## Training templates used

- [Cascade Classifier](https://docs.opencv.org/master/dc/d88/tutorial_traincascade.html)

[Automated Training for Cascade(Used to generate cascade model)](https://github.com/IgorFachini/Create-Custom-Haar-Cascade)

[Image Tool: photoscissors](https://online.photoscissors.com/)

- [Dlib HOG](http://blog.dlib.net/2014/02/dlib-186-released-make-your-own-object.html)

[Image tool by dlib: imglab](https://github.com/NaturalIntelligence/imglab)
