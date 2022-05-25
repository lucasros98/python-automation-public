from PIL import Image
import sys

def main():
        filename = sys.argv[1]
       # qoute = sys.argv[2]
        print(filename)
       
        image = Image.open(filename)

        width, height = image.size   # Get dimensions
        
        new_width = 1080
        new_height = 1920

        aspectRatio = width / height
        newAspectRatio = new_width / new_height

        if(aspectRatio > 0):
            left = (width - height*newAspectRatio)/2 
            top = 0
            right = (width + height*newAspectRatio)/2
            bottom = height
            box = (left, top, right, bottom)
        else:
            left = (width - new_width)/2
            top = (height - new_height)/2
            right = (width + new_width)/2
            bottom = (height + new_height)/2
            box = (left, top, right, bottom)
        
        crop = image.crop(box)
              
        new_size = (1080,1920)

        cropped_image = crop.resize(new_size, Image.ANTIALIAS)

        path = "./{}.jpg".format("instastory")
        cropped_image.save(path,quality=90)


main()
