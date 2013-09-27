from SimpleCV import Image
img = Image('lena.jpg')

noPegs = img.dilate(2)

filled = noPegs.erode(2)
allThree = img.sideBySide(noPegs.sideBySide(filled))
allThree.scale(.5).show()
