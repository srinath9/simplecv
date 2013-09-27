from SimpleCV import Image
img = Image('lena.jpg')
imgBin = img.binarize()

imgBin.erode().show()
