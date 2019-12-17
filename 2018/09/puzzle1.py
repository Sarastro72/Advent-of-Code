#!/usr/local/bin/python3
from collections import deque

PLAYERS=473
MARBLES=7090400

circle=deque([0])
score=[0] * (PLAYERS)

for marble in range(1, MARBLES+1):
    if (marble % 23 == 0):
        circle.rotate(7)
        score[marble % PLAYERS] += marble + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(marble)

    #print(f"{marble} – {circle}")

print(f"Highscore {max(score)}")