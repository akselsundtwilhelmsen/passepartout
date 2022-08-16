from PIL import Image, ImageColor
import argparse

#parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--image', type=str, required=True)
parser.add_argument('--border', type=str, required=True)
parser.add_argument('--color', type=str, required=False)
parser.add_argument('--weighted', type=str, required=False)
args = parser.parse_args()
inp_img = args.image

#determine if color argument is hex or text
if len(args.color) == 6:
    if args.color[0] != '#':
        args.color = '#' + args.color

#open image
img = Image.open(f'{inp_img}')

#determine if border argument is px or %
thickness = 0
if args.border[-1] == '%':
    thickness = int(float(args.border[0:-1]) * 0.01 * float(img.size[0]))
elif args.border[-1] == 'p':
    thickness = int(args.border[0:-1])

#make borders
width = int(img.size[0]) + (2 * thickness)
height = int(img.size[1]) + (2 * thickness)

if args.weighted == 'y':
    height += 2 * thickness

#create the new image with border
img_new = Image.new('RGB', (width, height), color=ImageColor.getcolor(f'{args.color}', 'RGB'))
img_new.paste(img, (thickness, thickness))

#add a "_p" before the new file suffix
for count, letter in enumerate(inp_img[::-1]):
    if letter == '.':
        img_new_name = f'{inp_img[0:len(inp_img)-count-1]}_p.{inp_img[len(inp_img)-count:len(inp_img)]}'
        break

#save the new image
img_new.save(img_new_name)
