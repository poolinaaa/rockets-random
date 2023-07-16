import random
from math import sqrt, pow

class Rocket:
    '''Class which creates a rocket
    '''
    nextId = 1

    def __init__(self, speedY, speedX=0, currentHeight = 0, x = 0):
        self.currentHeight = currentHeight
        self.speedY = speedY
        self.x = x
        self.speedX = speedX
        height = random.randint(0,10)
        self.currentHeight = self.currentHeight + height
        self.id = Rocket.nextId
        Rocket.nextId += 1

    def move(self):
        self.currentHeight += self.speedY
        self.x += self.speedX
    
    def __str__(self):
        return 'Current height after start is:'+ str(self.currentHeight) + ', x position:' + str(self.x)

    def distanceFromRocket(self, rocket):
        distance = sqrt(pow(abs(self.currentHeight - rocket.currentHeight),2) + pow(abs(self.x - rocket.x),2) )
        return 'Distance between rockets: ' + str(distance)


class BoardOfRockets():
    '''Class which is a set of rockets
    '''
    
    def __init__(self, amountOfRockets = 5):
        self.airport = [Rocket(random.randint(1,5),random.randint(1,5)) for _ in range(amountOfRockets)]

    def goUpOnlyByOne(self):
        for _ in range(10):
            index = random.randint(0,len(self.airport)-1)
            self.airport[index].move()

        for i in range(len(self.airport)):
            print(self.airport[i])

    def __getitem__(self,key):
        return self.airport[key]

    def __setitem__(self,key,value):
        self.airport[key].currentHeight = value

    @staticmethod
    def distanceBetweenRockets(rocket1 : Rocket, rocket2 : Rocket) -> float:
        diffHeight = rocket1.currentHeight - rocket2.currentHeight
        diffX = rocket1.x - rocket2.x
        return sqrt(diffHeight ** 2 + diffX ** 2)

    def __len__(self):
        return len(self.airport)






