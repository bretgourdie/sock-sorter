class Sock:

    def __init__(self, color=None, length=None, material=None, pattern=None, size=None):
        self.color = color
        self.length = length
        self.material = material
        self.pattern = pattern
        self.size = size

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

