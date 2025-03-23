from PIL import Image

image = Image.new('RGBA', (49, 49))
pixels = [[list(image.getpixel((x, y))) for x in range(image.width)] for y in range(image.height)]

for row in pixels:
    print(row)
