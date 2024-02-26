#implementation of class and objects using oops
class student:
    def __init__(self,name,age,sec):
        self.name=name                 #init=constructor -- a method which executes when an objects is created  
        self.age=age                   #oops--- doesnt need to write entire code just initialize an object
        self.sec=sec
        print(name,age,sec)
obj=student("vallibi","19","ece-a")
obj1=student("valli","23","ece-1")
        
