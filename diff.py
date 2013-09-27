from SimpleCV import Image
import numpy as np

diff = Image("lena.jpg")

matrix = diff.getNumpy()
flat = matrix.flatten()

num_change = np.count_nonzero(flat)
percent_change = float(num_change) / float(len(flat))
if percent_change > 0.1:
	print "miss match"
