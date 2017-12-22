import SockTraits, sys
from Basket import Basket
from Sock import Sock
from SelectionSort import SelectionSort
from HashSort import HashSort
from SortingMethod import SortingMethod

class SockSorter():

    def getTemplateSock(self):
        return Sock(
            None,
            SockTraits.Length.Ankle,
            SockTraits.Material.Cotton,
            SockTraits.Pattern.Plain,
            SockTraits.Size.Medium
        )

    def printMatches(self):
        return False

    def run(self, strNumSocks):
        basket = Basket()

        templateSock = self.getTemplateSock()
        numberOfSocks = int(strNumSocks)

        basePile = basket.dumpPile(numberOfSocks, templateSock)

        for sortingMethod in SortingMethod.getAllMethods():
            sorter = sortingMethod()

            pileToSort = list(basePile)

            sortedPile = sorter.timedSort(pileToSort)

            if self.printMatches():
                for pair in sortedPile:
                    print("Pair: {}<->{}".format(pair[0], pair[1]))


if __name__ == "__main__":
    minNumberOfArguments = 1
    if len(sys.argv) > minNumberOfArguments:
        app = SockSorter()
        app.run(sys.argv[minNumberOfArguments])
    else:
        print(
            "Received {}/{} required argument(s). Program will exit now."
            .format(
                len(sys.argv) - 1,
                minNumberOfArguments
            )
        )

