from PIL import Image

im = Image.open("qrdots.bmp")
out = Image.new("RGB", (29, 29), (255, 255, 255))

impx = im.load()
outpx = out.load()

for x in range(0, 169, 6):
    for y in range(0, 169, 6):
        if 0 in impx[x, y]:
            outpx[x//6, y//6] = (0, 0, 0)
        else:
            pass

out = out.resize((290, 290))

out.save("output.bmp")