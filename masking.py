from SimpleCV import Image,Color
img = Image("lena.jpg")
mask = img.createBinaryMask(color1=(130,125,100),color2=Color.BLACK)
mask = mask.morphClose()
result = img - mask.invert()
result.show()
