#randomly select around 10000 images to keep in the final dataset

import os
import random
directory = r'./raw_data/'
for f in os.scandir(directory):

    #every image has an 1/8th chance to be removed.
    r = random.uniform(0, 8)
    if r > 1:
        #remove the file
        print("Removed {}".format(f.name))
        os.remove(directory + f.name)
    else:
        print("Kept {}".format(f.name))


