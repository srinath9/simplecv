from SimpleCV import Image
img = Image('lena.jpg')

corners = [(0, 0), (480, 0), (336, 237), (147, 237)]
warped = img.warp(corners)

bgcolor = warped.getPixel(240, 115)
dist = warped.colorDistance(bgcolor)
blobs = dist.invert().findBlobs()
paper = blobs[-1].crop()

toyBlobs = paper.invert().findBlobs()
toy = toyBlobs[-1].crop()
paperSize = paper.width
toySize = toy.width
print float(toySize) / float(paperSize) * 8.5
