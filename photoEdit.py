from PIL import Image # operations used from PIL (Python Imaging Library)
import PIL.ImageOps

# ________________________image Ops_____________________________

im = Image.open('car.jpg') # our input image.

# adjusting RGBs
out=im.convert("RGB", (
    0.412453, 0.357580, 0.180423, 0,
    0.212671, 0.715160, 0.072169, 0,
    0.019334, 0.119193, 0.950227, 0 ))
out.save("Image2.jpg")
print("Adjusted RGBs")

# mirroing the image
out2 = im.transpose(Image.FLIP_LEFT_RIGHT)
out2.save("Image3.jpg")
print("Image Mirrored")

# gray image
out3= im.convert("1")
out3.save("Image4.jpg")
print("Gray Scaled")

# color inversted
out4 = PIL.ImageOps.invert(im)
out4.save("Image5.jpg")
print("Color Inverted")

# blending 2 images. the original and the mirrored.
out5=Image.blend(im, out2, 0.5)
out5.save("Image6.jpg")
print("Merged Success")


# save the images to be used in the collage funsction
listofimages=['car.jpg', 'Image2.jpg', 'Image3.jpg', 'Image4.jpg', 'Image5.jpg', 'Image6.jpg']

# compile all the image into one image
def create_collage(width, height, listofimages):
    cols = 2
    rows = 3
    thumbnail_width = width//cols
    thumbnail_height = height//rows
    size = thumbnail_width, thumbnail_height
    new_im = Image.new('RGB', (width, height))
    ims = []
    for p in listofimages:
        im = Image.open(p)
        im.thumbnail(size)
        ims.append(im)
    i = 0
    x = 0
    y = 0
    for col in range(cols): # printing col first
        for row in range(rows):
            print('image', i, x, y) # printing image positions
            new_im.paste(ims[i], (x, y))
            i += 1
            y += thumbnail_height
        x += thumbnail_width # moving to the next col
        y = 0

    new_im.save("Collage.jpg")

# calling the fucntion. passing the width hight and the list of images
create_collage(400, 450, listofimages)