# import packages
import cv2
import numpy as np
import random


# nasumicne boje
background_colour = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
dots_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

# maksimalan broj tacaka na najduzoj stranici
max_dots = 120

# crno bela slika
original_image = cv2.imread('slika.png', 0)

# dimenzije
original_image_height, original_image_width = original_image.shape

# smanjimo dimenzije na broj tacaka
if original_image_height == max(original_image_height,original_image_width):
    downsized_image = cv2.resize(original_image,(int(original_image_width*(max_dots/original_image_height)),max_dots))
else:
    downsized_image = cv2.resize(original_image,(max_dots,int(original_image_height*(max_dots/original_image_width))))

# smanjene dimenzije
downsized_image_height, downsized_image_width = downsized_image.shape

# velicina slike
multiplier = 50

# nova slika = smanjena slika * povecanje (zbog tacaka)
blank_img_height = downsized_image_height * multiplier
blank_img_width = downsized_image_width * multiplier

# set the padding value so the dots start in frame (rather than being off the edge
padding = int(multiplier/2)

# nova slika dobija boju pozadine
#                     broj redova i kolona,                   boja pozadine,      int (0,255)
blank_image = np.full(((blank_img_height),(blank_img_width),3), background_colour,dtype=np.uint8)

# ide redom i crta tacke na pozadini
for y in range(0,downsized_image_height):
    for x in range(0,downsized_image_width): #                                                                poluprecnik odredjuje jacina sivog piksela
        cv2.circle(blank_image, (((x*multiplier)+padding),((y*multiplier)+padding)), int((0.6 * multiplier) * ((255-downsized_image[y][x])/255)), dots_colour, -1)
#                  slika,      kordinate centra,                                    poluprecnik tacke,                                          boja,         oboji

# sacuva sliku
cv2.imwrite('s1.png',blank_image)

################################################           DRUGA

background_colour2 = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
dots_colour2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

blank_image = np.full(((blank_img_height),(blank_img_width),3), background_colour2,dtype=np.uint8)

for y in range(0,downsized_image_height):
    for x in range(0,downsized_image_width):
        cv2.circle(blank_image,(((x*multiplier)+padding),((y*multiplier)+padding)), int((0.6 * multiplier) * ((255-downsized_image[y][x])/255)), dots_colour2, -1)

cv2.imwrite('s2.png',blank_image)
 
################################################# TRECA

background_colour3 = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
dots_colour3 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

blank_image = np.full(((blank_img_height),(blank_img_width),3), background_colour3,dtype=np.uint8)

for y in range(0,downsized_image_height):
    for x in range(0,downsized_image_width):
        cv2.circle(blank_image,(((x*multiplier)+padding),((y*multiplier)+padding)), int((0.6 * multiplier) * ((255-downsized_image[y][x])/255)), dots_colour3, -1)

cv2.imwrite('s3.png',blank_image)
 
############################################### CETVRTA

background_colour4 = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
dots_colour4 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

blank_image = np.full(((blank_img_height),(blank_img_width),3), background_colour4,dtype=np.uint8)

for y in range(0,downsized_image_height):
    for x in range(0,downsized_image_width):
        cv2.circle(blank_image,(((x*multiplier)+padding),((y*multiplier)+padding)), int((0.6 * multiplier) * ((255-downsized_image[y][x])/255)), dots_colour4, -1)

cv2.imwrite('s4.png',blank_image)
 
# spoji slike
img1 = cv2.imread('s1.png') 
img2 = cv2.imread('s2.png')
img3 = cv2.imread('s3.png') 
img4 = cv2.imread('s4.png')

im_v1 = cv2.vconcat([img1, img2]) 
im_v2 = cv2.vconcat([img3, img4]) 
im_h = cv2.hconcat([im_v1, im_v2]) 
  
cv2.imwrite('slike.png',im_h)
