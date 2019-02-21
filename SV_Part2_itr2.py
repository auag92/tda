"""
Created on Mon Feb 18 00:32:26 2019

@author: SV
"""

import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from ripser import ripser

fnames = ["beetle-2.gif", "apple-5.gif", "butterfly-1.gif",
          "cup-1.gif", "crown-18.gif", "device1-3.gif",
          "device6-14.gif", "pocket-5.gif", "jar-13.gif",
          "spring-18.gif"]

Image1= plt.imread("images/bottle-10.gif")
Image2= plt.imread("images/apple-5.gif")
Image3= plt.imread("images/cellular_phone-4.gif")
Image4= plt.imread("images/cup-1.gif")
Image5= plt.imread("images/bottle-04.gif")
Image6= plt.imread("images/classic-6.gif")
Image7= plt.imread("images/classic-8.gif")
Image8= plt.imread("images/classic-7.gif")
Image9= plt.imread("images/classic-9.gif")
Image10= plt.imread("images/classic-12.gif")

Img1= Image1
Img2= Image2
Img3= Image3
Img4= Image4
Img5= Image5
Img6= Image6
Img7= Image7
Img8= Image8
Img9= Image9
Img10= Image10


from skimage.filters import roberts, sobel, scharr, prewitt

image = Img1
edge_sobel1 = sobel(image)
plt.imshow(edge_sobel1, cmap=plt.cm.gray)
plt.show()

image = Img2
edge_sobel2 = sobel(image)
plt.imshow(edge_sobel2, cmap=plt.cm.gray)
plt.show()

image = Img3
edge_sobel3 = sobel(image)
plt.imshow(edge_sobel3, cmap=plt.cm.gray)
plt.show()

image = Img4
edge_sobel4 = sobel(image)
plt.imshow(edge_sobel4, cmap=plt.cm.gray)
plt.show()

image = Img5
edge_sobel5 = sobel(image)
plt.imshow(edge_sobel5, cmap=plt.cm.gray)
plt.show()

image = Img6
edge_sobel6 = sobel(image)
plt.imshow(edge_sobel6, cmap=plt.cm.gray)
plt.show()

image = Img7
edge_sobel7 = sobel(image)
plt.imshow(edge_sobel7, cmap=plt.cm.gray)
plt.show()

image = Img8
edge_sobel8 = sobel(image)
plt.imshow(edge_sobel8, cmap=plt.cm.gray)
plt.show()

image = Img9
edge_sobel9 = sobel(image)
plt.imshow(edge_sobel9, cmap=plt.cm.gray)
plt.show()

image = Img10
edge_sobel10 = sobel(image)
plt.imshow(edge_sobel10, cmap=plt.cm.gray)
plt.show()


[x,y]= np.where(edge_sobel10)
np.savetxt('Img10.txt',np.c_[x,y])
[x,y]= np.where(edge_sobel9)
np.savetxt('Img9.txt',np.c_[x,y])
[x,y]= np.where(edge_sobel8)
np.savetxt('Img8.txt',np.c_[x,y])
[x,y]= np.where(edge_sobel7)
np.savetxt('Img7.txt',np.c_[x,y])
[x,y]= np.where(edge_sobel6)
np.savetxt('Img6.txt',np.c_[x,y])
[x,y]= np.where(edge_sobel5)
np.savetxt('Img5.txt',np.c_[x,y])
[x,y]= np.where(edge_sobel4)
np.savetxt('Img4.txt',np.c_[x,y])
[x,y]= np.where(edge_sobel3)
np.savetxt('Img3.txt',np.c_[x,y])
[x,y]= np.where(edge_sobel2)
np.savetxt('Img2.txt',np.c_[x,y])
[x,y]= np.where(edge_sobel1)
np.savetxt('Img1.txt',np.c_[x,y])

Img1= np.loadtxt("Img1.txt")
Img2= np.loadtxt("Img2.txt")
Img3= np.loadtxt("Img3.txt")
Img4= np.loadtxt("Img4.txt")
Img5= np.loadtxt("Img5.txt")
Img6= np.loadtxt("Img6.txt")
Img7= np.loadtxt("Img7.txt")
Img8= np.loadtxt("Img8.txt")
Img9= np.loadtxt("Img9.txt")
Img10= np.loadtxt("Img10.txt")

Image1_R= ripser(Img1, maxdim=0)['dgms']
Image2_R= ripser(Img2, maxdim=0)['dgms']
Image3_R= ripser(Img3, maxdim=0)['dgms']
Image4_R= ripser(Img4, maxdim=0)['dgms']
Image5_R= ripser(Img5, maxdim=0)['dgms']
Image6_R= ripser(Img6, maxdim=0)['dgms']
Image7_R= ripser(Img7, maxdim=0)['dgms']
Image8_R= ripser(Img8, maxdim=0)['dgms']
Image9_R= ripser(Img9, maxdim=0)['dgms']
Image10_R= ripser(Img10, maxdim=0)['dgms']


np.savetxt('Img1_R.npy',Image1_R)
np.savetxt('Img2_R.npy',Image2_R)
np.savetxt('Img3_R.npy',Image3_R)
np.savetxt('Img4_R.npy',Image4_R)
np.savetxt('Img5_R.npy',Image5_R)
np.savetxt('Img6_R.npy',Image6_R)
np.savetxt('Img7_R.npy',Image7_R)
np.savetxt('Img8_R.npy',Image8_R)
np.savetxt('Img9_R.npy',Image9_R)
np.savetxt('Img10_R.npy',Image10_R)
