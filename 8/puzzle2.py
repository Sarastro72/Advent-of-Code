#!/usr/local/bin/python

IMGX = 25
IMGY = 6
RES = IMGX * IMGY

def printImage(image):
    for y in range(IMGY):
        start = y * IMGX
        end = start + IMGX
        line = ""
        for i in image[start:end]:
            line += i
        line = line.replace("0", " ")
        line = line.replace("1", "█")
        line = line.replace("2", " ")
        print(line)


filepath = 'input'
with open(filepath) as fp:
    data = fp.readline().strip()

pos = 0
image = ["2"] * RES
layer = list(data[pos:pos+RES])
while(layer):
    printImage(layer)
    print("")
    for i in range(RES):
        if image[i] == "2":
            image[i] = layer[i]
    pos += RES
    layer = list(data[pos:pos+RES])

printImage(image)