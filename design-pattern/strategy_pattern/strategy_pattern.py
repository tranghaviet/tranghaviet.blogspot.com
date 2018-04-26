import abc

class GoAlgorithm(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def go(self):
        pass

class GoByDrivingAlgorithm(GoAlgorithm):
    def go(self):
        print('I am driving.')

class GoByFlyingFast(GoAlgorithm):
    def go(self):
        print('I am flying fast.')

class Vehicle:
    def __init__(self):
        self.go_algorithm = None

    def set_algorithm(self, algorithm):
        self.go_algorithm = algorithm

    def go(self):
        self.go_algorithm.go()

class StreetRacer(Vehicle):
    def __init__(self):
        self.set_algorithm(GoByDrivingAlgorithm())

class Helicoper(Vehicle):
    def __init__(self):
        self.set_algorithm(GoByFlyingFast())

class FormulaOne(Vehicle):
    def __init__(self):
        self.set_algorithm(GoByDrivingAlgorithm())

class Jet(Vehicle):
    def __init__(self):
        self.set_algorithm(GoByFlyingFast())

vehicle = StreetRacer()
vehicle.go()

vehicle = Helicoper()
vehicle.go()
