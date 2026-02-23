from PIL import Image
imgname = input("image: ")
gunsInput = input("guns.lol or namemc (guns/namemc): ")
with Image.open(imgname) as img:
    if gunsInput == "guns":
        for y in range(3):
            for x in range(12):
                # print((img.size[0], img.size[1], x+1, y+1))

                area = (
                    ((img.size[0]/12)*(x+1))-img.size[0]/12,
                    ((img.size[1]/3)*(y+1))-img.size[1]/3,
                    ((img.size[0]/12)*(x+2))-img.size[0]/12,
                    ((img.size[1]/3)*(y+2))-img.size[1]/3
                        )

                # print(area)

                region = img.crop(area)

                region.save(str(y+1)+"U"+str(x+1)+".jpg", "JPEG")

        # x: img.size[0] y: img.size[1] x= /12 y= /3
    else:
        baseSkin = Image.open("base_skin.png")
        for y in range(3):
            for x in range(9):
                if x == 0 and y == 0: continue
                # print((img.size[0], img.size[1], x+1, y+1))

                area = (
                    ((img.size[0] / 9) * (x + 1)) - img.size[0] / 9,
                    ((img.size[1] / 3) * (y + 1)) - img.size[1] / 3,
                    ((img.size[0] / 9) * (x + 2)) - img.size[0] / 9,
                    ((img.size[1] / 3) * (y + 2)) - img.size[1] / 3
                )

                # print(area)

                region = img.crop(area)

                newSkin = baseSkin.copy()
                newSkin.paste(region, (8, 8, 16, 16))

                newSkin.save(str(y + 1) + "U" + str(x + 1) + ".png", "PNG")