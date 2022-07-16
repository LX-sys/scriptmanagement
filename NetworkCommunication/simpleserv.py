
from twisted.internet import protocol, reactor


class Echo(protocol.Protocol):
    """这只是最简单的协议"""

    def dataReceived(self, data:bytes):
        data+=b"--lx"

        "收到任何数据后，立即将其写回"
        self.transport.write(data)


def main():
    """这在端口 8000 上运行协议"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000, factory)
    reactor.run()


if __name__ == "__main__":
    main()
