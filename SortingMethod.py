import abc
from datetime import datetime

class SortingMethod(abc.ABC):
    @abc.abstractmethod
    def sort(self, sockPile):
        pass

    def reportDuration(self, startTime, endTime):
        print("Sort time: {} to {}; {}".format(startTime, endTime, (endTime - startTime).total_seconds()))

    def timedSort(self, sockPile):
        start = datetime.now()
        sortedPile = self.sort(sockPile)
        end = datetime.now()
        self.reportDuration(start, end)
        return sortedPile
