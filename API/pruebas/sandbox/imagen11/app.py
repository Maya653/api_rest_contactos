from PIL import Image
im = Image.open("radio.jpg")

print(im.format, im.size, im.mode)

box = (100, 100, 400, 400)
region = im.crop(box)
region.save ("recorte.jpg")

r, g, b = im.split()
im = Image.merge("RGB", (b, g, r))
region.save("cambio.jpg")

out = im.rotate(45)
out.save("giro.jpg")