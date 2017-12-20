import SockEnums, SockPileGenerator
from Sock import Sock
from SelectionSort import SelectionSort

class SockSorter():

    def getSortingMethod(self):
        return SelectionSort()

    def getNumberOfSocks(self):
        return 10000

    def getTemplateSock(self):
        return Sock(None, SockEnums.Length.Ankle, SockEnums.Material.Cotton, SockEnums.Pattern.Plain, SockEnums.Size.Medium)

    def printMatches(self):
        return False

    def run(self):
        sockPileGenerator = SockPileGenerator.SockPileGenerator()

        templateSock = self.getTemplateSock()
        numberOfSocks = self.getNumberOfSocks()

        pile = sockPileGenerator.generatePile(numberOfSocks, templateSock)

        sorter = self.getSortingMethod()

        sortedPile = sorter.timedSort(pile)

        if self.printMatches():
            for pair in sortedPile:
                print("Pair: {}<->{}".format(pair[0], pair[1]))

if __name__ == "__main__":
    app = SockSorter()
    app.run()
