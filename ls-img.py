from PIL import Image
from colors import color
import glob
import shutil



types = ["*.jpg", "*.png", "*.bmp", "*.jpeg"]
files = []
for k in types:
	for m in glob.glob(k):
		files.append(m)

basewidth = 32
for l in files:
	print("\n\n" + str(l))
	img = Image.open(str(l))
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.ANTIALIAS)
	img = img.convert('RGB')
	width, height = img.size

	for i in range(1, height, 2):
		line = ''
		for j in range(1, basewidth):
			try:
				ra, ga, ba = img.getpixel((j, i))
				rb, gb, bb = img.getpixel((j, i+1))
			except IndexError:
				quit()
			line += color('\u2584', fg=(rb, gb, bb), bg=(ra, ga, ba))
		print(line)
