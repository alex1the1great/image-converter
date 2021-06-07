import sys
import os
from PIL import Image

_, image_folder, output_folder = sys.argv
cwd = os.getcwd()

# If output folder not exist create one.
if not os.path.exists(f'./{output_folder}'):
    parent_dir = cwd
    path = os.path.join(parent_dir, output_folder)
    os.mkdir(path)

path_to_input_folder = os.path.join(cwd, image_folder)
for single_file in os.listdir(path_to_input_folder):
    filename = single_file.split('.')[0]
    new_filename = 'new_' + filename + '.png'

    # convert to png
    open_single_file = os.path.join(path_to_input_folder, single_file)
    absolute_path_new_file = os.path.join(cwd, output_folder, new_filename)
    img = Image.open(open_single_file)
    img.save(absolute_path_new_file, 'png')
