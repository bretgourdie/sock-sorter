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
        print(
            "Sort time for {}: {} seconds ({} to {})"
            .format(
                className,
                (endTime - startTime).total_seconds(),
                startTime,
                endTime
            )
        )

    def timedSort(self, sockPile):
        copiedSockPile = list(sockPile)
        start = datetime.now()
        sortedPile = self.sort(copiedSockPile)
        end = datetime.now()
        self.reportDuration(start, end)
        return sortedPile
