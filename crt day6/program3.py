#write a python program to print fact of given no. using class and methods and recursion?
class f:
    def __init__(self,data):
        self.data=data
        print(self.find_fact())
    def find_fact(self):
        return self.fact(self.data)
    def fact(self,n):
        if n<1:
            return 1
        else:
            return n*self.fact(n-1)
obj=f(int(input()))


  
