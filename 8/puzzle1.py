#!/usr/local/bin/python

IMGX = 25
IMGY = 6
RES = IMGX * IMGY

filepath = 'input'
with open(filepath) as fp:
    image = fp.readline().strip()

pos = 0
lowest=RES
target=[]
layer = image[pos:pos+RES]
while(layer):
    freq = [0] * 10
    for n in layer:
        v = int(n)
        freq[v] = freq[v] + 1
    if freq[0] < lowest:
        lowest = freq[0]
        target = freq
        print(f"New target layer {target}")
    pos += RES
    layer = image[pos:pos+RES]    

print(target)
print(target[1] * target[2])