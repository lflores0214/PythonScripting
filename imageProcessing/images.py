from PIL import Image, ImageFilter, ImageOps

# img = Image.open('./images/pikachu.jpg')

# flitered_image = img.filter(ImageFilter.BLUR)

# converted_img = img.convert("L")

# crooked = flitered_image.rotate(90)

# cropped = ImageOps.crop(img, 20)

# cropped.save('cropped.png', 'png')

# crooked.save('crooked.png', 'png')

# flitered_image.save("blur.png", 'png')

# converted_img.save('grey.png', 'png')

img = Image.open('./images/astro.jpg')

img.thumbnail((400,400))

img.save('thumbnail.jpg')


