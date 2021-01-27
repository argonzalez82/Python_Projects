import cv2               #loads ML library for images
#import numpy as np       
from PIL import Image    #loads Image library
    

# required if you use Google Colab / Im using a local file
#from google.colab.patches import cv2_imshow
#from google.colab import files

#Path to photofile(/home/CentOS_Laptop/Pictures/photos4editing/2_Dogs_1kid.jpg)

#load the image into python
imported_img = Image.open('/home/CentOS_Laptop/Pictures/photos4editing/2_Dogs_1Kid.jpg')

#imported_img.format  #quick test to verify .jpg import 



