import Sock, SockEnums, SockPileGenerator

class SockSorter():
    sockPileGenerator = SockPileGenerator.SockPileGenerator()

    templateSock = Sock.Sock(None, SockEnums.Length.Ankle, SockEnums.Material.Cotton, SockEnums.Pattern.Plain, SockEnums.Size.Medium)

    pile = sockPileGenerator.generatePile(10, templateSock)

    for sock in pile:
        print(sock)

if __name__ == "__main__":
    app = SockSorter()
    app.run()
