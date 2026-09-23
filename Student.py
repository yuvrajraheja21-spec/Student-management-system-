# ==========================================
#       STUDENT MANAGEMENT SYSTEM
#              Using OOP
# ==========================================


# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Child Class
class Student(Person):

    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks

    # Calculate percentage
    def percentage(self):
        total = sum(self.marks.values())
        return total / len(self.marks)

    # Calculate grade
    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    # Display student information
    def display(self):
        print("\n------------------------------")
        print("       STUDENT DETAILS")
        print("------------------------------")

        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Roll No    :", self.roll_no)

        print("\nMarks:")
        for subject, mark in self.marks.items():
            print(subject, ":", mark)

        print("\nPercentage :", round(self.percentage(), 2), "%")
        print("Grade      :", self.grade())


# Student Management Class
class StudentManagementSystem:

    def __init__(self):
        self.students = []

    # Add student
    def add_student(self):

        print("\n========== ADD STUDENT ==========")

        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        roll_no = input("Enter roll number: ")

        marks = {}

        marks["Python"] = float(input("Enter Python marks: "))
        marks["Maths"] = float(input("Enter Maths marks: "))
        marks["Web Technology"] = float(
            input("Enter Web Technology marks: ")
        )

        student = Student(
            name,
            age,
            roll_no,
            marks
        )

        self.students.append(student)

        print("\nStudent added successfully!")


    # Display all students
    def display_students(self):

        if len(self.students) == 0:
            print("\nNo students found.")
            return

        print("\n========== ALL STUDENTS ==========")

        for student in self.students:
            student.display()


    # Search student
    def search_student(self):

        roll_no = input("\nEnter roll number to search: ")

        for student in self.students:

            if student.roll_no == roll_no:
                student.display()
                return

        print("\nStudent not found.")


    # Update marks
    def update_marks(self):

        roll_no = input("\nEnter roll number: ")

        for student in self.students:

            if student.roll_no == roll_no:

                print("\nAvailable Subjects:")
                print("1. Python")
                print("2. Maths")
                print("3. Web Technology")

                subject_choice = input(
                    "Choose subject: "
                )

                if subject_choice == "1":
                    subject = "Python"

                elif subject_choice == "2":
                    subject = "Maths"

                elif subject_choice == "3":
                    subject = "Web Technology"

                else:
                    print("Invalid subject.")
                    return

                new_marks = float(
                    input("Enter new marks: ")
                )

                student.marks[subject] = new_marks

                print("\nMarks updated successfully!")

                return

        print("\nStudent not found.")


    # Delete student
    def delete_student(self):

        roll_no = input(
            "\nEnter roll number to delete: "
        )

        for student in self.students:

            if student.roll_no == roll_no:

                self.students.remove(student)

                print(
                    "\nStudent deleted successfully!"
                )

                return

        print("\nStudent not found.")


# ==========================================
#              MAIN PROGRAM
# ==========================================

def main():

    system = StudentManagementSystem()

    while True:

        print("\n")
        print("======================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("======================================")

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":
            system.add_student()

        elif choice == "2":
            system.display_students()

        elif choice == "3":
            system.search_student()

        elif choice == "4":
            system.update_marks()

        elif choice == "5":
            system.delete_student()

        elif choice == "6":
            print("\nThank you for using the program!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# Start program
if __name__ == "__main__":
    main()
