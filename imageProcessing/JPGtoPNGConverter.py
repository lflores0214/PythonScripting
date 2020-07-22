import sys
import os
from PIL import Image

# with sys grab first and second argument "pokedex/, new/ "

# check if /new exists, if not create it

# loop through Pokedex,
# convert images to PNG
# save to the new folder


folder = os.path.dirname(sys.argv[1])
new_folder = os.path.dirname(sys.argv[2])


if not os.path.isdir(f"./{new_folder}"):
    os.mkdir(f"./{new_folder}")

for image in os.listdir(folder):
    new_img = Image.open(f"{folder}/{image}")
    img_name = os.path.splitext(image)[0]
    new_img.save(f"{new_folder}/{img_name}.png", "png")

print("All jpg images converted to png")
