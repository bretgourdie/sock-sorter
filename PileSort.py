from SortingMethod import SortingMethod
from Sock import Sock
from collections import defaultdict

class PileSort(SortingMethod):
    
    def sort(self, sockPile):
        sortedPile = []

        dColorPiles = {}

        # Generate color piles
        for sock in sockPile:
            if sock.color not in dColorPiles:
                dColorPiles[sock.color] = []
            dColorPiles[sock.color].append(sock)

        # Match in each pile
        for color in dColorPiles:
            coloredSockPile = dColorPiles[color]

            while len(coloredSockPile) > 0:
                leftSock = coloredSockPile.pop(0)

                rightSock = Sock()
                while leftSock != rightSock:
                    rightSock = coloredSockPile.pop(0)

                    if leftSock != rightSock:
                        coloredSockPile.append(rightSock)

                sortedPile.append((leftSock, rightSock))

        return sortedPile

