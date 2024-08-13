students_data=[
    {
        "Name":"Ali",
        "Fether's Name":"Muhammad Tahir",
        "Roll No":2,
        
    },
    {
        "Name":"Ali Tahir",
        "Fether's Name":"Muhammad Tahir",
        "Roll No":5,
        
    },
]

options=[
    "Add new student","Update student's data","Delete student's data","View student's data","Exit"
]

def show_students_data(students_data):
    for student_no,student in enumerate(students_data):
      print(student_no+1,end=".")
      for key_name,data in student.items():
          print(f"{key_name} : {data}",end=" , ")
      print()
    
# show_students_data(students_data)

def play_with_data(option):
    while True:
      if option in ["1"]:
       add_more_student_data()
      elif option in ["2"]:
        update_student_data()
      elif option in ["3"]:
        delete_student_data()
      elif option in ["4"]:
          show_students_data(students_data)
      elif option == "5":
          user_selection=input("Are you sure you want to exit? (y for yes/n or  no) ")
          select_yes_no(user_selection) 
      else:
          print("Select the correct option")
          break
   
      
      
          
        





def add_more_student_data():
     name=  input("Enter Name of student ")
     father_name=  input("Enter father's name of student ")
     roll_no=  input("Enter Roll No of student ")
     data={
          "name":name,
          "Father Name":father_name,
          "Roll No":roll_no,
      }
     students_data.append(data)
     print("students",students_data)
     show_options(options)

def update_student_data():
    show_students_data(students_data)
    student_no=  int(input("Select Student's number "))-1
    if 0< student_no <=len(students_data):
        if students_data:
            for keys in students_data[0]:
                print(keys)
            key= input("Which thing want to updtade ").capitalize()
            new_data=input(f"Write new {key} of student ")
            students_data[student_no][key]=new_data
            print("students",students_data)
    else:
        print("Choose correct student  number")
    show_options(options)
                
def delete_student_data():
    show_students_data(students_data)
    try:
        student_no = int(input("Select the student number you want to delete: ")) - 1
        if 0 <= student_no < len(students_data):
            del students_data[student_no]
            print("Deleted student data successfully.")
            show_students_data(students_data)
        else:
            print("Invalid student number. Please select a correct number.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
    show_options(options)
        
        
def show_options(options):
    for key, opt in enumerate(options):
        print(f"{key+1} : {opt}")
    select_option=input("Select option which want to performs ") 
    play_with_data(select_option)   
        
def select_yes_no(user_seletion):
  while True:  
     user_seletion=input("Do you want to perform more operations y for yes and n for no").lower()
     if user_seletion in ["y","yes"]:
        show_options(options)
     elif user_seletion in ["n","no"]:
        break
     else:
        print("Invalid data")
     
    
show_options(options)