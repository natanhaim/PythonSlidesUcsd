from PIL import Image
from PIL import ImageFilter

im = Image.open("nature.jpg") # load image
s = int(raw_input("enter smoothness: "))
if s < 0 or s > 10:
	print "smoothness must be in range [0, 10]"
	exit()

for i in range(s):
	print "processing: " + str(i + 1) + " of " + str(s)
	im = im.filter(ImageFilter.MedianFilter(5))
print "finished!"

imOutName = "nature" + str(s) + ".jpg"
im.save(imOutName, "JPEG")
im.show()
