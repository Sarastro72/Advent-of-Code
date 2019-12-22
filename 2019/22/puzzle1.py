import collections
import re
import sys

class Deck:
    def __init__(self, size):
        self.size = size
        self.deck = collections.deque(range(size))

    def dealNewDeck(self):
        self.deck.reverse()

    def cut(self, n):
        self.deck.rotate(-n)

    def deal(self, n):
        target = [-1] * self.size
        for i in range(0, self.size * n, n):
            target[i % self.size] = self.deck.popleft()
        self.deck = collections.deque(target)

    def __str__(self):
        return " ".join([str(c) for c in self.deck])

    def toList(self):
        return list(self.deck)

pattern = re.compile(r"([a-z\s]+)(-?\d+)?")
deck = Deck(10007)
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        print(line)
        (cmd, val) = pattern.match(line).groups()
        if (cmd.startswith("cut")):
            deck.cut(int(val))
        elif(cmd.startswith("deal with")):
            deck.deal(int(val))
        elif (cmd.startswith("deal into")):
            deck.dealNewDeck()

print(deck.toList().index(2019))
