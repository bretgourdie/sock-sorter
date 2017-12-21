import SockEnums
from Basket import Basket
from Sock import Sock
from SelectionSort import SelectionSort
from HashSort import HashSort

class SockSorter():

    def getSortingMethod(self):
        #return SelectionSort()
        return HashSort()

    def getNumberOfSocks(self):
        return 10000

    def getTemplateSock(self):
        return Sock(None, SockEnums.Length.Ankle, SockEnums.Material.Cotton, SockEnums.Pattern.Plain, SockEnums.Size.Medium)

    def printMatches(self):
        return False

    def run(self):
        basket = Basket()

        templateSock = self.getTemplateSock()
        numberOfSocks = self.getNumberOfSocks()

        pile = basket.dumpPile(numberOfSocks, templateSock)

        sorter = self.getSortingMethod()

        sortedPile = sorter.timedSort(pile)

        if self.printMatches():
            for pair in sortedPile:
                print("Pair: {}<->{}".format(pair[0], pair[1]))

if __name__ == "__main__":
    app = SockSorter()
    app.run()
