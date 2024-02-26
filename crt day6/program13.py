from abc import ABC
class shape(ABC):
    def print(self):
        print("i am a normal method defined imside the abstract class "shape")
    def calculate_are(self):
        pass
class rectangle(shape):
    length=5
    breadth=3
    def calculate_area(self):
        return self.leength*self.breadth
    rec=rectangle()
