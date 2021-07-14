import os
import random
import PIL
from PIL import Image

raw_directory = r'./training_data/training/'
output_directory = r'./test_data/train/'

for f in os.scandir(raw_directory):
    #open image in PIL
    img = Image.open(raw_directory + f.name)
    print("Opened {}".format(f.name))
    r = random.uniform(0, 8)
    if r < 1:
        img.save(output_directory + f.name)        
        print("Saved {}".format(f.name))
    else:
        pass

print("Finished Conversion")