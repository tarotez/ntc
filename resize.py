from PIL import Image
img = Image.open('orig.jpg',)
img = img.resize((32, 32), Image.ANTIALIAS)
img.save('new.jpg', 'JPEG', quality = 100, optimize = True)
