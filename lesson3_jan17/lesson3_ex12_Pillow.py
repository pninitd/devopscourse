from PIL import Image

img = Image.new('RGB', (60, 30), color=(73, 109, 137))
img.save('my_image.png')
