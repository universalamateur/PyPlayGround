#!/usr/bin/env python3

import os
from PIL import Image


"""process the supplier images. You will be using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:
Size: Change image resolution from 3000x2000 to 600x400 pixel
Format: Change image format from .TIFF to .JPEG
Note: The raw images from images subdirectory contains alpha transparency layers.
So, it is better to first convert RGBA 4-channel format to RGB 3-channel format before processing the images. 
Use convert("RGB") method for converting RGBA to RGB image."""

def main():
    source = os.path.join(os.path.expanduser("~"), "supplier-data", "images")
    print("Handling in: {} ".format(source))
    for root, directories, files in os.walk(source, topdown=False):
        for name in files:
            filename=os.path.join(root, name)
            print("Source: {}".format(filename))
            f, ending_original_file = os.path.splitext(name)
            if ending_original_file == ".tiff":
                target=os.path.join(source, (f+ ".jpeg"))
                print("Target: {}".format(target))
                try:
                    with Image.open(filename) as im:
                        out = im.convert("RGB")
                        out.resize((600,400)).save(target, "JPEG")
                except OSError:
                    print("cannot convert", filename)
            else:
                print(f"File not a grphic: {filename}")


if __name__ == "__main__":
    main()