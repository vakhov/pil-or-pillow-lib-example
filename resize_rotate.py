from PIL import Image

pil_im = Image.open('example.jpg')

out = pil_im.resize((128, 128)).rotate(45)
out.save('resize_rotate.jpg')
