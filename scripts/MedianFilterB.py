from PIL import Image
from PIL import ImageFilter

im = Image.open("nature.jpg") # load image
s = int(raw_input("enter smoothness: "))
r = int(raw_input("select filter: "))
if (s < 0 or s > 10) or (r < 0 or r > 1):
	print "smoothness must be in range [0, 10]"
	print "filter should be in range [0, 1]"
	exit()

for i in range(s):
	print "processing: " + str(i + 1) + " of " + str(s)
	if r == 0:
		im = im.filter(ImageFilter.MedianFilter(5))
	elif r == 1:
		im = im.filter(ImageFilter.GaussianBlur(5))
print "finished!"

imOutName = "nature" + str(s) + "_" + str(r) + ".jpg"
im.save(imOutName, "JPEG")
im.show()
