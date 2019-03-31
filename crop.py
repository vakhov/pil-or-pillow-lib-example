from PIL import Image

pil_im = Image.open('example.jpg')

box = (100, 100, 400, 400)
region = pil_im.crop(box)

region = region.transpose(Image.ROTATE_180)
pil_im.paste(region, box)
pil_im.save('crop.jpg')
