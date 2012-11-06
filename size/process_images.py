import Image
import os

DIR = "BABY1_DANCE1"
OUT = "out"
SIZE = (128, 128)

for image in os.listdir(DIR):
    if not image.endswith("png"):
        continue
    f = os.path.join(DIR, image)
    im = Image.open(f)
    size = SIZE
    im.thumbnail(size, Image.ANTIALIAS)
    newpath = os.path.join(OUT, image)
    im.save(newpath)
    print "%s is processed" % image
