#downsamples the covers into 128x128 and then moves the image into ./training_data
#this is because my GPU is poo and i don't know if it can handle 512x512 images
#this may change if i get a better GPU or computer or something :)

import os
import random
import PIL
from PIL import Image

raw_directory = r'./raw_data/'
output_directory = r'./training_data/train/'

IMAGE_SIZE = 128, 128

for f in os.scandir(raw_directory):
    #open image in PIL
    img = Image.open(raw_directory + f.name)
    print("Opened {}".format(f.name))
    img = img.resize(IMAGE_SIZE, resample=Image.BILINEAR)
    print("Resized {}".format(raw_directory + f.name))
    img.save(output_directory + f.name)
    print("Saved {}".format(f.name))

print("Finished Conversion")