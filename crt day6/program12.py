#polymorphism-one code behaves in 2 methods
#method overloading -it will done only in single class(same class different methods)
'''class A:
    def hi(self):
        print("hi")
    def hi(self,data):      #runtime- overriding #compile-overloading
        print("hello")
a=A()
a.hi(4)'''

#method overriding(different class in same methods)
class A:
    def hi(self):
        print("hi")
    def hi(self,data):
        print("hello")
class B:
    def hi(self,data):
        print("hi")
a=A()
b=B()
a.hi(4)
b.hi(5)
