import inspect 

class SockPileGenerator:

    def generatePile(numberOfSocks, templateSock):
        sockPile = []

        isEvenNumberOfSocks = numberOfSocks % 2 == 0
        if not isEvenNumberOfSocks:
            numberOfSocks -= 1

        for sock in range(numberOfSocks / 2):
            sockDesign = generateSock(templateSock)
            leftSock = copy(sockDesign)
            rightSock = copy(sockDesign)

            sockPile.append(leftSock)
            sockPile.append(rightSock)

        return sockPile
    
    def generateSock(templateSock):
        sock = Sock()

        for property, value in vars(templateSock).iteritems():
            setattr(sock, value or getRandomEnum(property))

        return sock

    def getRandomEnum(propertyName):
        for name, obj in inspect.getmembers(SockEnums):
            if inspect.isclass(obj) and propertyName.title() == name:
                return random.choice(list(obj))