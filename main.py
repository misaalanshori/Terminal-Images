from PIL import Image
from colors import color
import shutil

basewidth = shutil.get_terminal_size((140, 20))[0]
img = Image.open(str(input('Input File: ')))
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
