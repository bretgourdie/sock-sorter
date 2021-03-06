from Sock import Sock
from copy import copy
import inspect, SockTraits, random

class Basket:

    def getRandomTrait(self, propertyName):
        for name, obj in inspect.getmembers(SockTraits):
            if inspect.isclass(obj) and propertyName.title() == name:
                return random.choice(list(obj))

    def generateSock(self, templateSock):
        sock = Sock()

        for property, value in vars(templateSock).items():
            setattr(sock, property, value or self.getRandomTrait(property))

        return sock

    def dumpPile(self, numberOfSocks, templateSock):
        sockPile = []

        isEvenNumberOfSocks = numberOfSocks % 2 == 0
        if not isEvenNumberOfSocks:
            numberOfSocks -= 1

        for sock in range(numberOfSocks // 2): # always generate pairs
            sockDesign = self.generateSock(templateSock)
            leftSock = copy(sockDesign)
            rightSock = copy(sockDesign)

            sockPile.append(leftSock)
            sockPile.append(rightSock)

        random.shuffle(sockPile)

        return sockPile

