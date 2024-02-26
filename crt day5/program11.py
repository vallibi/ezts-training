class ece:
    def section1(self,name,rollno):
        self.name=name
        self.rollno=rollno
        print(name,rollno)
    def section2(self,n,age,rno):
        self.n=n
        self.age=age
        self.rno=rno
        print(n,age,rno)
obj=ece()
obj.section1("valli","401")
obj.section2("vallibi",19,401)
