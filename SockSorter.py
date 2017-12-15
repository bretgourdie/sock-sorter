import Sock, SockEnums, SockPileGenerator

class SockSorter():
    sockPileGenerator = SockPileGenerator()

    templateSock = Sock()
    templateSock.length = Length.Ankle
    templateSock.material = Material.Cotton
    templateSock.pattern = Pattern.Plain
    templateSock.size = Size.Medium

    pile = sockPileGenerator.generatePile(10, templateSock)

    for sock in pile:
        print(sock)

if __name__ == "__main__":
    app = SockSorter()
    app.run()
