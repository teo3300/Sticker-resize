# accepted extentions

ext=['png','jpg','webp','jfif']

def getSystem():
    import platform
    system = platform.system().lower()
    return system
    pass

sysOS = getSystem()

#######################################

def createdir(path):
    if sysOS == "linux":
        command = "mkdir "
    elif sysOS == "windows":
        command = "md "
    else:
        print("ERROR: unknown system: '"+sysOS+"'")
        exit()
    import os
    from os import system
    dr = command + path
    print('"'+ path +'" directory created')
    os.system(dr)

#######################################

def cls():
    if sysOS == "linux":
        command = "clear"
    elif sysOS == "windows":
        command = "cls"
    else:
        print("ERROR: unknown system: '"+sysOS+"'")
        exit()
    import os
    from os import system
    os.system(command)
    pass

#######################################

def checkModule(moduleName):
    if sysOS == "linux":
        command = "sudo pip3.7 install "+moduleName#+" > /dev/null"
    elif sysOS == "windows":
        command = "python -m pip install "+ moduleName+ " --user"
    else:
        print("ERROR: unknown system: '"+sysOS+"'")
        exit()
    import os
    from os import system
    os.system(command)
    pass

#######################################

def SA_resize_stickers(file, out):

    img = Image.open('./input/' + file)

    W,H = img.size
    
    if W > H:
        w = 512
        h = H * 512 / W
    else:
        h = 512
        w = W * 512/H
    img = img.resize((int(w), int(h)), PIL.Image.ANTIALIAS)
    new_image = './resized/resized-' + file + '-re' + out
    img.save(new_image, quality=85)
    return new_image
    pass

#######################################

try:
    import PIL
except ImportError:
    checkModule("Pillow")
    import PIL
from PIL import Image

#######################################
# Program sarts here #

import os
import sys


cwd = './input'
i=1
if( not os.path.isdir('./resized')):
    createdir("resized")
if( not os.path.isdir('./input')):
    createdir("input")

if not os.listdir(cwd):
    print("WARNING: no input images, put your images inside the \"input\" folder before selecting the output format")

out=input("\nSelect the output format:\n[1]\tpng\n[2]\twebp (default)\n\n\n")
cls()

if out == "1":
    out = ".png"
else:
    out = ".webp"

fold = os.listdir(cwd)
images = []

for file in fold:
    if file.split('.')[-1].lower() in ext:
        images.append(file)
l=len(images)
    
if not images:
    input("\nERROR: no input image\npress ENTER to exit ")
    exit()
for image in images:
    print("Resizing {:5d} of {:5d}: {}".format(i,l,image))
    SA_resize_stickers(image, out)
    i=i+1
input("\n" + str(l) + " file(s) converted\npress ENTER to exit ")
