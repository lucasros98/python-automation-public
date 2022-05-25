# Python script for formating and resizing images and move them to the Desktop folder
# This script can be run by MacOS Automator, and linked to a specific folder
# It saves time when you publishing blog content, that need an optimized image.
from PIL import Image
import sys
import os

def main():
        filename = sys.argv[1]        
        image = Image.open(filename)

        #Image dimensions
        width, height = image.size
        new_width = 1200
        new_height = 700

        #Aspect ratios
        aspectRatio = width / height
        newAspectRatio = new_width / new_height

        #If the image is vertical
        if(aspectRatio > newAspectRatio):
            left = (width - height*newAspectRatio)/2 
            top = 0
            right = (width + height*newAspectRatio)/2
            bottom = height
        #for horiztional images
        else:
            left = (width - new_width)/2
            top = (height - new_height)/2
            right = (width + new_width)/2
            bottom = (height + new_height)/2

        #the crop box
        box = (left, top, right, bottom)

        #crop image
        crop = image.crop(box)
        new_size = (new_width,new_height)
        cropped_image = crop.resize(new_size, Image.ANTIALIAS)

        #remove old file
        os.remove(filename)
        path = "./Desktop/{}.jpg".format("epic_file")
        cropped_image.save(path,quality=85)

main()
