f = open("image.ppm", "w")

f.write("P3 \n600 600 \n255 \n") #header, 500x500 and largest val color

x = 600
i = 0
while (i < 600):
    r = (i * 2) % 255
    b = (i * 3) % 255
    g = (i * 5) % 255
    if (x > 400):
        r = x % 255
    elif (x > 200):
        b = x % 255
    else:
        g = x % 255
    row = (str(r) + " " + str(b) + " " + str(g) + " ") * 600 + "\n"
    f.write(row)
    i += 1
    x -= 1
f.close()
