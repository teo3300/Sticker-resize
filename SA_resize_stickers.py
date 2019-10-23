def getSystem():
    import platform
    system = platform.system().lower()
    print("System found: '"+system+"'")
    return system
    pass

#######################################

def checkModule(moduleName):
    systemOS = getSystem()
    if systemOS == "linux":
        command = "sudo pip install "+moduleName#+" > /dev/null"
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

def SA_resize_stickers(file):
    try:
        import PIL
    except ImportError:
        checkModule("Pillow")
        import PIL
    from PIL import Image

    img = Image.open('./input/' + file)

    W,H = img.size
    
    if W > H:
        w = 512
        h = H * 512 / W
    else:
        h = 512
        w = W * 512/H
    img = img.resize((int(w), int(h)), PIL.Image.ANTIALIAS)
    new_image = './resized/resized-' + file + '.vbb.png'
    img.save(new_image, quality=85)
    return new_image
    pass

#######################################
# Program sarts here #

import os
import sys

cwd = './input/'
i=1
t = len(os.listdir(cwd))
for file in os.listdir(cwd):
    print("Resizing {:3d} of {:3d}: {}".format(1,t,file))
    SA_resize_stickers(file)
