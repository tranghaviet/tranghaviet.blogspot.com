import abc

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print('Circle class')

class Square(Shape):
    def draw(self):
        print('Square class')

class ShapeFactory:
    # use dictionary technical for java enum like
    # variables declare here is class's variable
    __shape = {}

    def __init__(self):
    ##    self.foo is class's property
        # TODO: check if instance initialized then return old instead create new one
        self.__shape['CIRCLE'] = Circle()
        self.__shape['SQUARE'] = Square()

    @staticmethod
    def getShape(self, shape):
        shape = shape.upper()

        if shape == 'CIRCLE':
            return Circle()
        elif shape == 'SQUARE':
            return Square()
        else:
            return None

s = ShapeFactory()
s.getShape('Circle').draw()
s.getShape('Square').draw()

s.setFoo()

a = ShapeFactory()
print(a.foo)
