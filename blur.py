from PIL import Image, ImageFilter
before = Image.open("download.jpg")
after = before.filter(ImageFilter.BLUR)
after.save("out.jpg")
