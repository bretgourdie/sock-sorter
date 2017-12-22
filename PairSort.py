from Sock import Sock
from SortingMethod import SortingMethod

class PairSort(SortingMethod):

    def sort(self, sockPile):
        
        sortedPile = []

        while len(sockPile) > 0:
            leftSock = sockPile.pop(0)

            rightSock = Sock()
            while leftSock != rightSock:
                rightSock = sockPile.pop(0)
                
                if leftSock != rightSock:
                    sockPile.append(rightSock)

            sortedPile.append((leftSock, rightSock))

        return sortedPile
