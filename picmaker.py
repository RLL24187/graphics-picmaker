f = open("image.ppm", "w")

f.write("P3 \n600 600 \n255 \n") #header, 500x500 and largest val color

x = 0
y = 0
r = 1
b = 127
g = 255
while (y < 600):
    while (x < 600):
        if (x == 0 and y == 0 or (y != 0 and (x == y or x % y == 0))):
            r = 255
            b = 255
            g = 255
        else:
            r = (r + 1) % 256
            b = (b + 3) % 256
            g = (g + 5) % 256
        f.write(str(r) + " " + str(b) + " " + str(g) + " ")
        x += 1
    f.write("\n")
    y += 1
    x = 0
f.close()
