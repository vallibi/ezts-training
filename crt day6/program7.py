#creating 5 classes using single inheritance
class training:
    def __init__(self):
        print("this is class training")
class ece1(training):
    def __init__(self):                 #super-it is used to call the constructor
        super().__init__()
        print("this is class ece1")
class ece2:
    def __init__(self):
        print("this is class ece2")
class ece3(ece2):
    def __init__(self):
        super().__init__()
        print("this is class ece3")
class ece4:
    def __init__(self):
        print("this is class ece4")
a=ece1()
b=ece3()
c=ece4()
    
    
