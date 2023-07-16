from rakietyCwKlasy import BoardOfRockets, Rocket
import random
from math import sqrt,pow

airport = BoardOfRockets()
airport2 = BoardOfRockets()

print('airport 1')
airport.goUpOnlyByOne()

print('airport 2')
airport2.goUpOnlyByOne()

print(airport[2].distanceFromRocket(airport[3]))
print(BoardOfRockets.distanceBetweenRockets(airport[1],airport2[1]))

for rocket in range(len(airport)):
    print(airport[rocket].id)
