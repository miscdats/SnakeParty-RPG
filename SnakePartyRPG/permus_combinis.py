import itertools
from itertools import product
from itertools import permutations
from itertools import combinations
import string


# Task 1

print("Task 1\n")

faces = {"ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
diamonds = set(map('-'.join, itertools.product("d", faces)))
hearts = set(map('-'.join, itertools.product("h", faces)))
clubs = set(map('-'.join, itertools.product("c", faces)))
spades = set(map('-'.join, itertools.product("s", faces)))
deck = diamonds.union(hearts).union(clubs).union(spades)

print("Diamonds: ", diamonds)
print("Hearts: ", hearts)
print("Clubs: ", clubs)
print("Spades: ", spades)
print("Deck of cards: ", deck)

# Task 2

print("\nTask 2\n")

numPairsSpCb = len(spades)**1 * len(clubs)**1
numTrios = len(diamonds)**1 * len(spades)**1 * len(hearts)**1
numAllSuits = len(diamonds)**1 * len(spades)**1 * len(hearts)**1 * len(clubs)**1
print("Number of Spade & Club pairs: ", str(numPairsSpCb))
print("Number of Diamond & Spade & Heart trios: ", str(numTrios))
print("Number of quartets with one of each suit: ", str(numAllSuits))

# Task 3

print("\nTask 3\n")

triosFaceSpades = set(permutations(list(sorted(spades))[-4:-1]))
countTrios = set(permutations(triosFaceSpades, 2))
heartsFaces = set(permutations(list(sorted(hearts))[-4:-1]))
spadesHeartsFaces = triosFaceSpades.union(heartsFaces)
countSH = len(set(permutations(spadesHeartsFaces, 2)))
print(countTrios)
print("Number of Spade Face pairs: " + str(len(countTrios)))
print("Number of Spades and Hearts union pairs: " + str(countSH))

# Task 4

print("\nTask 4\n")

countStraightFlushH = 0
straightFlushH = list(combinations(deck, 5))
for card in straightFlushH[0]:
    face = card[0][0]
    if face in card[0:4]:
        countStraightFlushH += 1

print(straightFlushH)
print("Straight Flushes: " + str(countStraightFlushH))
