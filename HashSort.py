from SortingMethod import SortingMethod
from Sock import Sock

class HashSort(SortingMethod):
    
    def sort(self, sockPile):
        sortedPile = []

        dPile = {}

        for sock in sockPile:
            if sock.color not in dPile:
                dPile[sock.color] = []
            dPile[sock.color].append(sock)

        for color in dPile:
            coloredSockPile = dPile[color]

            while len(coloredSockPile) > 0:
                leftSock = coloredSockPile.pop(0)

                rightSock = Sock()
                while leftSock != rightSock:
                    rightSock = sockPile.pop(0)

                    if leftSock != rightSock:
                        sockPile.append(rightSock)

                sortedPile.append((leftSock, rightSock))

        return sortedPile

