from PIL import Image

pil_im = Image.open('example.jpg')

pil_im.thumbnail((128, 128))
pil_im.save('thumbnail.jpg')
