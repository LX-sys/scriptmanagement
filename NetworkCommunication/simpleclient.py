
"""
一个示例客户端。在运行之前先运行 simpleserv.py.
"""

from twisted.internet import protocol, reactor

# 客户端协议
class EchoClient(protocol.Protocol):
    """连接后，发送一条消息，然后打印结果."""

    # 建立连接时调用
    def connectionMade(self):
        self.transport.write(b"hello, world!")

    # 每当接收到数据时调用
    def dataReceived(self, data):
        "收到任何数据后，立即将其写回"
        print("Server said:", data)
        self.transport.loseConnection()

    # 当连接关闭时调用
    def connectionLost(self, reason):
        print("连接丢失")


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    # 当连接开始时调用
    def startedConnecting(self, connector):
        pass

    # 当连接失败时调用
    def clientConnectionFailed(self, connector, reason):
        print("连接失败 - 再见！")
        reactor.stop()


    # 当已建立的连接丢失时调用
    def clientConnectionLost(self, connector, reason):
        print("连接丢失 - 再见！")
        reactor.stop()


# t将协议连接到在端口 8000 上运行的服务器
def main():
    f = EchoFactory()
    reactor.connectTCP("localhost", 8000, f)
    reactor.run()


if __name__ == "__main__":
    main()
