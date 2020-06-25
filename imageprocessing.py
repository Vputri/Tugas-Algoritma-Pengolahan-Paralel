import skimage.io as io
from skimage.color import rgb2gray 
img = io.imread('./index.jpeg')
img_grayscale = rgb2gray(img)
show_grayscale = io.imshow(img_grayscale)
io.show()
