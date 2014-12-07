import f2n

myimage = f2n.fromfits("20131203_m06-0848+50_1053.fit")

# We crop the FITS image (xmin, xmax, ymin, ymax).
myimage.crop(70, 170, 60, 160)
# The image is now 100 x 100 pixels.

myimage.setzscale(4500, "ex")
# z2 = "ex" means extrema -> maximum in this case.
myimage.makepilimage("lin", negative = False)
# We can choose to make a negative image.

myimage.showcutoffs(redblue = True)
# Pixels below z1 will be blue, above z2 will be red.

# We upsample (= "zoom" without interpolation) the pixels.
myimage.upsample(5)
# The image is now 500 x 500

# We draw some labels and circles.
# myimage.drawstarsfile("stars.cat", r=3, colour=(255, 0,0))
# Note that all the coordinates are those from the original image !
# Of course, the function drawstars allows you to the same
# without any catalog file.

# Same for drawing a rectangle...
myimage.drawrectangle(118, 149, 137, 155, colour=(0,255,0), label="Empty region")

myimage.writetitle("Hello World !", colour=(200, 200, 0))
myimage.writeinfo(["This is a demo", "of some possibilities",
    "of f2n.py"], colour=(255,100,0))

myimage.tonet("2_single.png")