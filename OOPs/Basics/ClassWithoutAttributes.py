class Hello:


    @staticmethod  # Decorator
    def printHello():
        print("Hello")

    def printHiii(self):
        print("Hiiiii")

Hello.printHello()
obj = Hello()
obj.printHiii()