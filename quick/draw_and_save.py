from PIL import Image, ImageDraw

# size of image
canvas = (400, 300)

# scale ration
scale = 5
thumb = canvas[0]/scale, canvas[1]/scale

# rectangles (width, height, left position, top position)
frames = [(50, 50, 5, 5), (60, 60, 100, 50), (100, 100, 205, 120)]

# init canvas
im = Image.new('RGBA', canvas, (255, 255, 255, 255))
draw = ImageDraw.Draw(im)

# draw rectangles
for frame in frames:
    x1, y1 = frame[2], frame[3]
    x2, y2 = frame[2] + frame[0], frame[3] + frame[1]
    draw.rectangle([x1, y1, x2, y2], outline=(0, 0, 0, 255))

# make thumbnail
im.thumbnail(thumb)

# save image
im.save('im.png')
