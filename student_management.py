students = {}


def add_student():
    roll = input("Enter roll number:")
    name = input("Enter student name:")
    marks = input("Enter Marks:")
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found")
    else:
        for roll, info in students.items():
            print("roll:", roll)
            print("Name:", info["name"])
            print("marks:", info["marks"])

def delete_student():
    roll = input("Enter roll number to delete:")
    if roll in students:
        del students[roll]
        print("student deleted")
    else:
        print("student not found")

while True:
    print("\n student management system")
    print("1.Add student ")
    print("2.View students")
    print("3.Delete student")
    print("4.Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Program closed")
        break
    else:
        print("Invalid choice")
                             
                             
                        
                    
                
                
                
    
        
                
                
                