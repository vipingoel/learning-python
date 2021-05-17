
class BaseTest:
    # def __init__(self):
    #     print("Base init")
    
    # def f(self, n):
    #     print("base f", n)
    #     self.g()
        
    def g(self):
        print("base g")
    
    __g = g


class Base2Test:
    """ I am Base 2 """
    
    def __init__(self):
        print("Base2 init")
    
    def f(self, n):
        print("base2 f", n)
        self.g()
        
    def g(self):
        print("base2 g")


class ChildTest(BaseTest, Base2Test):
    def __init__(self):
        super().__init__()
        print("Child init")

    def f(self, n):
        super().f(n)
        print("child f", n)

    def g(self):
        print("child g")

if __name__ == "__main__":
    b = BaseTest()
    print("b.g()", b.g())
    print("b.g.__func__(b)", b.g.__func__(b))
    print("b.g.__self__(b)", b.g.__self__.g())
    # b.f(2)
    # b = ChildTest()
    # b.f(4)

    # print(issubclass(BaseTest, ChildTest))
