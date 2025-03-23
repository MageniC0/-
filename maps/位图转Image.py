from PIL import Image

pixels = [[[0, 0, 0, 0] for i in range(49)] for j in range(49)]
image = Image.frombytes('RGBA', (49, 49), bytes([channel for row in pixels for pixel in row for channel in pixel]))
image.save("maps/test2.png")