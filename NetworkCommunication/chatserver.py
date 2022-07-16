
# from twisted.internet.protocol import Factory
# from twisted.internet.endpoints import TCP4ServerEndpoint
# from twisted.internet import reactor

from twisted.internet.protocol import Protocol


class Echo(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write("Welcome! There are currently %d open connections.\n" %(self.factory.numProtocols,))

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1

    def dataReceived(self, data):
        self.transport.write(data)


class QOTD(Protocol):

    def connectionMade(self):
        self.transport.write(b"hello")
        self.transport.loseConnection()