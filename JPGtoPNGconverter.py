import sys
import os
from PIL import Image

if not len(sys.argv) == 3:
    print('Es necesario ingresar origen y destino')
    exit()


images_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(images_folder):
    img = Image.open(f'{images_folder}{filename}')
    name_cleaned = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{name_cleaned}.png', 'png')


