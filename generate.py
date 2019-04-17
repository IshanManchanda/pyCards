from os.path import join, dirname
from PIL import Image, ImageDraw, ImageFont


def main():
	# Load base image
	img, imgs = Image.open('base.png').convert("RGB"), []

	# Load fonts with predetermined font size
	f64 = ImageFont.truetype(join(dirname(__file__), 'font.otf'), 82)
	f56 = ImageFont.truetype(join(dirname(__file__), 'font.otf'), 72)

	coords_name = (386, 166)
	coords_title = (186, 1016)
	fill_color = (70, 79, 169)

	with open('temp.csv') as f:
		# [ name , title ]
		titles = [x.rstrip().split(',') for x in f.readlines()]

	for title in titles:
		a = img.copy()

		# Handle comma in title by merging all the subsequent values
		if len(title) > 2:
			title[1] = ",".join(title[1:])

		draw = ImageDraw.Draw(a)
		draw.text(coords_name, title[0], fill_color, font=f64)
		draw.text(coords_title, title[1], fill_color, font=f56)
		imgs.append(a)

		if len(title) > 2:
			# If title contains comma, save as: NAME.png
			a.save('out/%s.png' % title[0], 'PNG')
		else:
			# Else, save as: NAME - TITLE.png
			a.save('out/%s - %s.png' % (title[0], title[1]), 'PNG')

	# Save all images in a single pdf for easy printing
	imgs[0].save('out.pdf', save_all=True, append_images=imgs[1:])


if __name__ == '__main__':
	main()
