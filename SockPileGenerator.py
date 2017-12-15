from Sock import Sock
from copy import copy
import inspect, SockEnums, random

class SockPileGenerator:

    def __init__(self):
        1 + 1

    def getRandomEnum(self, propertyName):
        for name, obj in inspect.getmembers(SockEnums):
            if inspect.isclass(obj) and propertyName.title() == name:
                return random.choice(list(obj))

    def generateSock(self, templateSock):
        sock = Sock()

        for property, value in vars(templateSock).items():
            setattr(sock, property, value or self.getRandomEnum(property))

        return sock

    def generatePile(self, numberOfSocks, templateSock):
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

        return sockPile

