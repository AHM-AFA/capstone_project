import os
from PIL import Image

#Change into the directory that contains the images and list all the Image names
def change_dir():

    os.chdir("Images") 
    print(os.getcwd())
    return os.listdir()

#Process all images in the directory and change their format
def process_img(images_names):

    for file in images_names:
        
        #Try except block is written to ensure if the code tried reading a non image file it will skip it and open the next image
        try:
            with Image.open(file) as changed_img:
                img = changed_img.rotate(-90)
                img_width = int(img.size[0] * 0.30)
                img_height = int(img.size[1] * 0.42)
                img.resize((img_width,img_height)).convert("RGB").save(change_exten(file))
        except(IOError, SyntaxError):
            continue


#Change file format from .png to .jpeg
def change_exten(file):
    name, ext = os.path.splitext(file)
    #Check if a file is in a format other than jpeg or jpg

    if ext != ".jpg" and ext != ".jpeg":
        return "Edited Images/"+name+".jpeg"    
    else:
        return "Edited Images/"+file
        


process_img(change_dir())