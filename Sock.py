class Sock:

    color = None
    length = None
    material = None
    pattern = None
    size = None

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

