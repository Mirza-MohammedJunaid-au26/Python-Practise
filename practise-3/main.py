# Inheritance

class A:
    def show(self,name,age):
        print("Base Class Name :",name)
        print("Base Class Age :",age)

class B(A):
    def show(self, name, age,std):
        print("Derived Class Name :",name)
        print("Derived Class Age :",age)
        print("Derived Class Age :",std)

obj = B()
obj.show("Junaid",12)