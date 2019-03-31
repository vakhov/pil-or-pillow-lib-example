from PIL import Image

pil_im = Image.open('example.jpg').convert('L').save('result.jpg')
