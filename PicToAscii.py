"""
Peter Demachkie
pdemachk@uscs.edu
https://github.com/PeterDemachkie
"""


from PIL import Image
import sys, os

img_file = str(sys.argv[1])

if len(sys.argv) != 2:
    raise ValueError("Usage: python ascii_to_jpg.py <filename>")
if img_file [-4:] != ".jpg":
    raise Exception("File Error: only .jpg filetypes allowed\n")
if not os.path.isfile(img_file):
    raise FileNotFoundError(f"{img_file} does not exist in the working directory")

SaveName = img_file[:-4] + 'Ascii.txt'

imgcolor = Image.open(img_file)
img = imgcolor.convert('L')
width, height = img.size

if width > 100:
    mult = (2 * round((width/100), 2))
    width = 100
    height = int(height/mult)
    img = img.resize((width, height))

format = []
for y in range(height):
    for x in range(width):
        color = img.getpixel((x, y))
        if color >= 205:
            format.append('@')
        if 205 > color >= 185:
            format.append('#')
        if 185 > color >= 150:
            format.append('*')
        if 150 > color >= 120:
            format.append(';')
        if 120 > color >= 90:
            format.append('.')
        if 90 > color:
            format.append(' ')
    format.append('\n')
final = ''.join(format)

File = open(SaveName, 'w')
for letter in final:
    File.write(letter)
File.close()

