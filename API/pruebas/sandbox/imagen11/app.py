from PIL import Image
im = Image.open("imagen2.jpg")
im.show()

print(im.format, im.size, im.mode)