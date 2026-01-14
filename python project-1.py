                       #PHYTHON PROGECT-1
                
'''Mini project/Assignment Question
Project Title:Student Admission System
Prblem Statement:
You are asked to create a Student Admission SYstem for a school.The system
should allow the user to:
          1. View all students currently admitted.
          2. Add a new student with roll number,name,class,and section.
              *if the student with the same roll number already exists,show a
              messsage:"studentalready exists!Cannot add again."
          3. Search a student by roll number and display their details.
          4. Exit the system.
Requirements/Guidelines:
    #Use a dictionary to store student details with roll number as the key.
    #Use a loop to display the menu repeatedly until the user chooses to exit.
    #Use if-elif-else conditions to handle user choices.
    #For checking empty student list,use students=={}.
    #Display appropriate message for successful addition,search results,or
    invalid inputs.
    #Keep the program simple and use only basic python concepts:
    loops,conditionals,dictionaries, and strings.'''
    
    
    

print("STUDENT ADMISSION SYSTEM")

students={101:{'name':'Kavitha','class':'11','section':'A'},102:{'name':'Dharshini','class':'12','section':'B'},
          103:{'name':'Latha','class':'10','section':'A'},104:{'name':'Jagan','class':'9','section':'B'}}
while True:
    print("---menu---")
    print("1. show students")
    print("2. Add student")
    print("3. search student")
    print("4. Exit")
    ch=input("enter your choice:")
    if ch=="1":
        if students=={}:
            print("no students found")
        else:
            for roll,i in students.items():
                print("Roll No:",roll,"Name:",{i['name']},"class:",{i["class"]},"section:",{i["class"]})
    elif ch=="2":
        roll=int(input("EnterRoll No:"))
        if roll in students:
            print("student already exists!")
        else:
            name=input("Enter your name:")
            clas=input("Enter your class:")
            sec=input("enter your section:")
            New_student={"name":name,"class":clas,"section":sec}
            print("student added successfully")
    elif ch=="3":
         roll=int(input("Enter Roll no to search:"))
         if roll in students:
             print(students[roll])
         else:
             print("student not found")
    elif ch=="4":
        print("THANK YOU!EXITING...")
        break
    else:
        print("INVALID CHOICE,PLEASE TRY AGAIN")
    
    
            


