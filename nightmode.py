import PIL
from PIL import Image
import numpy as np

path = str(input('Enter path: '))
# path = 'D:/Projects/Night_Mode/8.jpg'
im = Image.open(path,mode = 'r') 
im = im.resize((400,400))
image = np.array(im, dtype=np.float64)
#RGB based

#to check if the object of interest is illuminated
image_crop = image[100:300,100:300]
if np.mean(image)<50 and np.mean(image_crop)<45:
  print('Night')
else:
  print('Day')


##Bright channel prior based
#w = 2
#image = image[:, :, :3] / 255
#M, N, _ = image.shape
## padding for channels
#padded = np.pad(image, ((int(w/2), int(w/2)), (int(w/2), int(w/2)), (0, 0)), 'edge')
#brightch = np.zeros((M, N))
#for i, j in np.ndindex(brightch.shape):
#  brightch[i, j] = np.max(padded[i:i + w, j:j + w, :]) # bright channel
#if np.mean(brightch)*255<40:
#  print('Night')
#else:
#  print('Day')