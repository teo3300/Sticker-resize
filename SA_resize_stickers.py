def getSystem():
    import platform
    system = platform.system().lower()
    print("System found: '"+system+"'")
    return system
    pass
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

out=input("selezionare il formato di uscita:\n(1) png\n(2) webp\n\n\n")

cls()

if out == "1":
    out = ".png"
elif out == "2":
    out = ".webp"

cwd = './input/'
i=1
t = len(os.listdir(cwd))
for file in os.listdir(cwd):
    print("Resizing {:3d} of {:3d}: {}".format(i,t,file))
    SA_resize_stickers(file, out)
    i=i+1
