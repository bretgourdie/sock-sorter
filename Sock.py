class Sock:

    self.color = None
    self.length = None
    self.material = None
    self.pattern = None
    self.size = None

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

