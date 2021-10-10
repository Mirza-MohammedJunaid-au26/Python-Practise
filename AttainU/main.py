class Teachers:

    Teacher_Login = []
    Teacher_Details = []
    Teacher_ID = 1
    H_J_Bhabha = []

    def __init__(self):
        print()
        print()
        print("!!! Welcome Teachers !!!")
        print()
        print("1. Login")
        print("2. SignUp")
        print("3. Exit")
        LS_Input = int(input("Enter :"))

        if LS_Input == 1:
            self.Teachers_login()
        elif LS_Input == 2:
            self.Teachers_signup()
        elif LS_Input == 3:
            Welcome()
        else:
            print("!!! Valid Input !!!")
            Welcome()

    def Teachers_login(self):
        print()
        print("!!! LOGIN !!!")
        print()
        print("Gmail :", end="")
        self.Teacher_GMail = input()
        print("Password :", end="")
        self.Teacher_Password = input()

        for i in range(1, len(self.Teacher_Login)):
            if self.Teacher_GMail == self.Teacher_Login[i]:
                if self.Teacher_Password == self.Teacher_Login[i+1]:
                    print()
                    print("!!! Login Successfully !!!")
                    self.Teacher_Dashboard()
                else:
                    print()
                    print("!!! Enter Valid Password !!!")
                    self.__init__()

    def Teachers_signup(self):
        print()
        print("!!! SIGN UP !!!")
        print()
        print("Gmail :", end="")
        Teacher_GMail = input("")
        print("Password :", end="")
        Teacher_Password = input("")
        self.Teacher_Login.append(self.Teacher_ID)
        self.Teacher_Login.append(Teacher_GMail)
        self.Teacher_Login.append(Teacher_Password)
        print("!!! Account Created Successfully !!!")
        print(self.Teacher_Details)
        print(self.Teacher_Login)
        self.Teachers_login()

    def Teacher_Dashboard(self):
        print()
        id_index = self.Teacher_Login.index(self.Teacher_GMail)
        print("ID :", self.Teacher_Login[id_index-1])
        print("1. Register")
        print("2. Lecture Assign")
        print("3. Edit Your Details")
        print("4. Logout")
        dashboard_inp = int(input("Enter :"))
        if dashboard_inp == 1:
            self.Teacher_Register()
        if dashboard_inp == 2:
            self.Lecture_Assign()
        elif dashboard_inp == 3:
            self.EditDetails()
        elif dashboard_inp == 4:
            Teachers.Teacher_ID = Teachers.Teacher_ID+1
            Welcome()

    def Teacher_Register(self):
        print()
        print("!!! Register !!!")
        Teacher_Name = input("Name :")
        Teacher_Experience = int(input("Experience (In Years) :"))
        Teacher_Location = input("Location :")
        Teacher_Subject = input("Subject :")
        self.Teacher_Details.append(self.Teacher_ID)
        self.Teacher_Details.append(Teacher_Name)
        self.Teacher_Details.append(Teacher_Experience)
        self.Teacher_Details.append(Teacher_Location)
        self.Teacher_Details.append(Teacher_Subject)
        print("!!! Register Successfully !!!")
        print(self.Teacher_Details)
        print(self.Teacher_Login)
        self.Teacher_Dashboard()

    def Lecture_Assign(self):
        print("!!! Lecture Timing is 9-11 !!!")
        lecture_assign_ID = int(input("Enter your ID:"))
        id_index = self.Teacher_Details.index(lecture_assign_ID)
        teacher_details_name = self.Teacher_Details[id_index+1]
        lecture_assign = Admin.lecture.get(teacher_details_name)
        self.H_J_Bhabha.append(lecture_assign)
        print("Lecture :",lecture_assign)
        self.Teacher_Dashboard()        

    def EditDetails(self):
        print()
        id_inp = int(input("Enter ID :"))
        teacher_index = self.Teacher_Details.index(id_inp)
        print("ID :", self.Teacher_Details[teacher_index])
        print("1. Name :", self.Teacher_Details[teacher_index+1])
        print("2. Experience :", self.Teacher_Details[teacher_index+2])
        print("3. Location :", self.Teacher_Details[teacher_index+3])
        print("4. Subject :", self.Teacher_Details[teacher_index+4])
        edit_inp = int(input("Enter :"))

        if edit_inp == 1:
            new_name = input("Name :")
            self.Teacher_Details[teacher_index+1] = new_name
            print("!!! Name Updated Successfully !!!")
            self.Teacher_Dashboard()
        elif edit_inp == 2:
            new_Experience = int(input("Experience :"))
            self.Teacher_Details[teacher_index+2] = new_Experience
            print("Experience Updated Successfully")
            self.Teacher_Dashboard()
        elif edit_inp == 3:
            new_Location = input("Location :")
            self.Teacher_Details[teacher_index+3] = new_Location
            print("Location Updated Successfully")
            self.Teacher_Dashboard()
        elif edit_inp == 4:
            new_Subject = input("Subject :")
            self.Teacher_Details[teacher_index+4] = new_Subject
            print("Subject Updated Successfully")
            self.Teacher_Dashboard()
        else:
            print("!!! Enter Valid Option !!!")
            self.EditDetails()


class Student():
    Student_Login = []
    Student_Details = []
    Student_ID = 1

    def __init__(self):
        print()
        print("!!! Welcome Students !!!")
        print()
        print("1. Login")
        print("2. SignUp")
        print("3. Exit")
        LS_Input = int(input("Enter :"))

        if LS_Input == 1:
            self.Students_login()
        elif LS_Input == 2:
            self.Students_signup()
        elif LS_Input == 3:
            Welcome()
        else:
            print("!!! Valid Input !!!")
            Welcome()

    def Students_login(self):
        print()
        print("!!! LOGIN !!!")
        print()
        print("Gmail :", end="")
        self.Student_GMail = input()
        print("Password :", end="")
        self.Student_Password = input()

        for i in range(1, len(self.Student_Login)):
            if self.Student_GMail == self.Student_Login[i]:
                if self.Student_Password == self.Student_Login[i+1]:
                    print()
                    print("!!! Login Successfully !!!")
                    self.Student_Dashboard()
                else:
                    print()
                    print("!!! Enter Valid Password !!!")
                    self.__init__()

    def Students_signup(self):
        print()
        print("!!! SIGN UP !!!")
        print()
        print("Gmail :", end="")
        Student_GMail = input("")
        print("Password :", end="")
        Student_Password = input("")
        self.Student_Login.append(self.Student_ID)
        self.Student_Login.append(Student_GMail)
        self.Student_Login.append(Student_Password)
        print("!!! Account Created Successfully !!!")
        print(self.Student_Details)
        print(self.Student_Login)
        self.Students_login()

    def Student_Dashboard(self):
        print()
        id_index = self.Student_Login.index(self.Student_GMail)
        print("ID :", self.Student_Login[id_index-1])
        print("1. Register")
        print("2. Lecture Assign")
        print("3. Edit Your Details")
        print("4. Logout")
        dashboard_inp = int(input("Enter :"))
        if dashboard_inp == 1:
            self.Student_Register()
        if dashboard_inp == 2:
            self.Lecture_Assign()
        elif dashboard_inp == 3:
            self.EditDetails()
        elif dashboard_inp == 4:
            Student.Student_ID = Student.Student_ID + 1
            Welcome()

    def Student_Register(self):
        print()
        print("!!! Register !!!")
        Student_Name = input("Name :")
        Student_Experience = int(input("Experience (In Years) :"))
        Student_Location = input("Location :")
        Student_phone = input("Phone Number :")
        self.Student_Details.append(self.Student_ID)
        self.Student_Details.append(Student_Name)
        self.Student_Details.append(Student_Experience)
        self.Student_Details.append(Student_Location)
        self.Student_Details.append(Student_phone)
        print("!!! Register Successfully !!!")
        print(self.Student_Details)
        print(self.Student_Login)
        self.Student_Dashboard()


    def Lecture_Assign(self):
        print("1. H J Bhabha")
        print("2. Exit")
        batch = int(input("Enter :"))

        if batch == 1:
            if len(Teachers.H_J_Bhabha) == 0:
                print("No Lectures")
                self.Student_Dashboard()
            else:
                print(Teachers.H_J_Bhabha[0],end="")
                print(Teachers.H_J_Bhabha[1],end="")
        else:
            self.Student_Dashboard()


    def EditDetails(self):
        print()
        id_inp = int(input("Enter ID :"))
        student_index = self.Student_Details.index(id_inp)
        print("ID :", self.Student_Details[student_index])
        print("1. Name :", self.Student_Details[student_index+1])
        print("2. Experience :", self.Student_Details[student_index+2])
        print("3. Location :", self.Student_Details[student_index+3])
        print("4. Subject :", self.Student_Details[student_index+4])
        edit_inp = int(input("Enter :"))

        if edit_inp == 1:
            new_name = input("Name :")
            self.Teacher_Details[student_index+1] = new_name
            print("!!! Name Updated Successfully !!!")
            self.Teacher_Dashboard()
        elif edit_inp == 2:
            new_Experience = int(input("Experience :"))
            self.Teacher_Details[student_index+2] = new_Experience
            print("Experience Updated Successfully")
            self.Teacher_Dashboard()
        elif edit_inp == 3:
            new_Location = input("Location :")
            self.Teacher_Details[student_index+3] = new_Location
            print("Location Updated Successfully")
            self.Teacher_Dashboard()
        elif edit_inp == 4:
            new_Subject = input("Subject :")
            self.Teacher_Details[student_index+4] = new_Subject
            print("Subject Updated Successfully")
            self.Teacher_Dashboard()
        else:
            print("!!! Enter Valid Option !!!")
            self.EditDetails()







class Admin(Teachers,Student):
    lecture = {}
    
    def __init__(self):
        print()
        print("Gmail :",end="")
        admin_gmail = input()
        print("Password :",end="")
        admin_password = int(input())

        if admin_gmail=="admin" and admin_password==123:
            self.welcome_Admin()
        else:
            print("!!! Enter Valid Password !!!")


    def welcome_Admin(self):
        print()
        print("!!! Welcome Admin !!!")
        print("1. Add Lecture")
        print("2. Teacher Details")
        print("3. Student Details")
        print("4. Logout")
        admin_input = int(input("Enter :"))

        if admin_input == 1:
            self.add_lecture()
        elif admin_input == 2:
            self.Teacher_List()
        elif admin_input == 3:
            self.Student_List()
        elif admin_input == 4:
            Welcome()
        else:
            print("!!! Invalid Input !!!")


    def add_lecture(self):
        print()
        print("!!! Teacher Lists !!!")
        for i in range(0,len(self.Teacher_Details),5):
            print(self.Teacher_Details[i],". ",self.Teacher_Details[i+1])
        teacher_name = input("Enter Name :")
        lecture_name = input("Enter Lecture Subject :")
        self.lecture[teacher_name]=lecture_name
        print(self.lecture)
        self.welcome_Admin()
    
    def Teacher_List(self):
        print("Id          Name      Experience    Location        Subject")
        for i in range(0,len(Teachers.Teacher_Details)):
            print(Teachers.Teacher_Details[i],"         ",end="")
            if(i>0 and i%5==0):
                print()

        print("1. Exit")
        exit_inp = int(input("Enter :"))
        if exit_inp == 0:
            self.welcome_Admin()
    
    def Student_List(self):
        print("Id          Name      Experience    Location        Subject")
        for i in range(0,len(Student.Students_Details)):
            print(Student.Students_Details[i],"         ",end="")
            if(i>0 and i%4==0):
                print()
        self.welcome_Admin()



def Welcome():
    print("!!! Welcome to Attain U !!!")
    print("1. Teacher")
    print("2. Student")
    print("3. Admin")
    TS_inp = int(input("Enter :"))

    if TS_inp == 1:
        Teacher_obj = Teachers()
    elif TS_inp == 2:
        Student_obj = Student()
    elif TS_inp == 3:
        Admin_obj = Admin()
    else:
        print("!!! Enter Valid Option !!!")

Welcome()
