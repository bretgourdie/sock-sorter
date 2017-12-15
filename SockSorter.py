import Sock, SockEnums, SockPileGenerator

class SockSorter():
    sockPileGenerator = SockPileGenerator()

    templateSock = Sock(
        None,
        Length.Ankle,
        Material.Cotton,
        Pattern.Plain,
        Size.Medium)

    pile = sockPileGenerator.generatePile(10, templateSock)

    for sock in pile:
        print(sock)

if __name__ == "__main__":
    app = SockSorter()
    app.run()
