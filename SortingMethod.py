import abc
from datetime import datetime

class SortingMethod(abc.ABC):
    def getAllMethods():
        return SortingMethod.__subclasses__()

    @abc.abstractmethod
    def sort(self, sockPile):
        pass

    def reportDuration(self, startTime, endTime):
        className = self.__class__.__name__
        print("Sort time for {}: {} to {}; {}".format(className, startTime, endTime, (endTime - startTime).total_seconds()))

    def timedSort(self, sockPile):
        start = datetime.now()
        sortedPile = self.sort(sockPile)
        end = datetime.now()
        self.reportDuration(start, end)
        return sortedPile
