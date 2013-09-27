from SimpleCV import Image,Camera,time
import numpy as np

cam =Camera()
img = cam.getImage()
img.show(3)
time.sleep(5)
img.save("file.png")