#quick and dirty gif-making script
import imageio
import sys
import os

def create_gif(input_directory, output_directory, output_name=None):    
    images = []   

    for f in os.scandir(input_directory):
        images.append(imageio.imread(input_directory + f.name))
    if output_name is None:
        imageio.mimsave(output_directory + 'output.gif', images)
        print("Image saved as " + output_directory + "output.gif")
    else:
        imageio.mimsave(output_directory + output_name, images)
        print("Image saved as " + output_directory + output_name)
    
    
#main parse script
# arg[1] is input-directory
# arg[2] is output-directory
# arg[3] is output_name 

if __name__ == "__main__":
    if len(sys.argv) == 3:
        create_gif(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        create_gif(sys.argv[1], sys.argv[2], sys.argv[3])
    else:        
        print("Usage: python3 create_gif.py input_directory output_directory output_name(optional)")
