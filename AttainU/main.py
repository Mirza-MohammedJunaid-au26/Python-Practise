class Teachers:

    Teacher_Login = {}

    def __init__(self):
        print()
        print("!!! Welcome Teachers !!!")
        print()
        print("1. Login")
        print("2. SignUp")
        print("3. Exit")
        LS_Input = int(input("Enter :"))

        if LS_Input==1:
            self.Teachers_login()
        elif LS_Input==2:
            self.Teachers_signup()
        elif LS_Input==3:
            Welcome()
        else:
            print("!!! Valid Input !!!")
            Welcome()
    
    def Teachers_login(self):
        print("Gmail :",end="")
        Teacher_GMail = input("")
        print(Teacher_GMail)
        print("Password :",end="")
        Teacher_Password = input("")
        print(Teacher_Password)

    def Teachers_signup(self):
        pass

class Student:
    
    def __init__(self):
        print("Student")

    def Students_login(self):
        pass

    def Students_signup(self):
        pass

def Welcome():
    print("!!! Welcome to Attain U !!!")
    print("1. Teacher")
    print("2. Student")
    TS_inp = int(input("Enter :"))

    if TS_inp==1:
        Teacher_obj = Teachers() 
    elif TS_inp==2:
        Student_obj = Student()

Welcome() 