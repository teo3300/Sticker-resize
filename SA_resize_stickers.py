def getSystem():
    import platform
    system = platform.system().lower()
    return system
    pass

#######################################

def createdir(path):
    systemOS = getSystem()
    if systemOS == "linux":
        command = "mkdir "
    elif systemOS == "windows":
        command = "md "
    else:
        print("ERROR: unknown system: '"+systemOS+"'")
        exit()
    import os
    from os import system
    dr = command + path
    print('"'+ path +'" directory created')
    os.system(dr)

#######################################

def cls():
    systemOS = getSystem()
    if systemOS == "linux":
        command = "clear"
    elif systemOS == "windows":
        command = "cls"
    else:
        print("ERROR: unknown system: '"+systemOS+"'")
        exit()
    import os
    from os import system
    os.system(command)
    pass

#######################################

def checkModule(moduleName):
    systemOS = getSystem()
    if systemOS == "linux":
        command = "sudo pip3.7 install "+moduleName#+" > /dev/null"
    elif systemOS == "windows":
        command = "python -m pip install "+ moduleName+ " --user"
    else:
        print("ERROR: unknown system: '"+systemOS+"'")
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

out=input("\nPut your images inside the \"input\" folder and select the output format:\n[1]\tpng\n[2]\twebp\n\n\n")
cls()

if out == "1":
    out = ".png"
elif out == "2":
    out = ".webp"

fold = os.listdir(cwd)
l = len(fold)
for file in fold:
    print("Resizing {:4d} of {:4d}: {}".format(i,l,file))
    SA_resize_stickers(file, out)
    i=i+1
