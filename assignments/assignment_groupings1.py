import os
class Student:
    def __init__(self, studNum, studName):
        self.studNum = studNum
        self.studName = studName

    class Subject:
        def __init__(self, student, subjCode, subjDesc, numUnits, midGrade, finGrade):
            self.student = student
            self.subjCode = subjCode
            self.subjDesc = subjDesc
            self.numUnits = numUnits
            self.midGrade = midGrade
            self.finGrade = finGrade
            self.aveGrade = 0
            self.remarks = ""

        def computeAve(self):
            self.aveGrade = (self.midGrade + self.finGrade) / 2
            if self.aveGrade <= 3.12:
                self.remarks = "Passed"
            else:
                self.remarks = "Failed"

        def saveFile(self):
            with open("student.txt", "a") as files:
                files.write(f"{self.student.studNum}|{self.student.studName}|"
                            f"{self.subjCode}|{self.subjDesc}|{self.numUnits}|"
                            f"{self.midGrade}|{self.finGrade}|{self.aveGrade:.2f}|{self.remarks}\n")

def inputStudentInfo(dataType, prompt):
    while True:
        try:
            userInput = input(prompt)

            if dataType == "string":
                if userInput.strip(): return userInput
                else: raise ValueError("Input cannot be empty.")

            elif dataType == "int":
                num = int(userInput)
                if num < 1: raise ValueError("Number must be 1 or greater.")
                return num

            elif dataType == "float":
                num = float(userInput)
                if num < 1: raise ValueError("Number must be 1.0 or greater.")
                return num

            else: raise TypeError("Unsupported data type.")

        except ValueError as e: print("Invalid input. Error:", e)
        except TypeError as e: print("Invalid type. Error:", e)
        except Exception as e: print("Unexpected error occurred:", e)

def addStudent():
    studNum = inputStudentInfo("int", "Enter student number: ")
    studName = inputStudentInfo("string", "Enter student name: ")

    answer = 'y'; counter = 0
    while answer == 'y' and counter < 7:
        subjCode = inputStudentInfo("string", "Enter subject code: ")
        subjDesc = inputStudentInfo("string", "Enter subject description: ")
        numUnits = inputStudentInfo("int", "Enter number of units: ")

        while True:
            midGrade = inputStudentInfo("float", "Enter midterm grade: ")
            if 1.0 <= midGrade <= 5.0: break
            else: print("Grade must be between 1.0 and 5.0.")

        while True:
            finGrade = inputStudentInfo("float", "Enter finals grade: ")
            if 1.0 <= finGrade <= 5.0: break
            else: print("Grade must be between 1.0 and 5.0.")

        student = Student(studNum, studName)
        subject = Student.Subject(student, subjCode, subjDesc, numUnits, midGrade, finGrade)
        subject.computeAve()
        subject.saveFile()

        answer = input("Do you want to add more? [y/n]: ").lower()
        counter+=1
    print("Student record added successfully.")

def editStudent():
    subjCode = ""; subjDesc = ""
    numUnits = 0; midGrade = 0
    finGrade = 0; aveGrade = 0
    remarks = ""; answer = 'y'

    files = open("student.txt", "r")
    temp = open("temp.txt", "w")
    compStudNum = inputStudentInfo("int", "Enter student number: ")

    studentRecords = files.readlines()
    files.close()

    subjectsCode = [line.split("|")[2].strip().lower() for line in studentRecords if
                int(line.split("|")[0]) == compStudNum]

    if not subjectsCode:
        print("Student number not found. Please try again.")
        return

    print("Edit Student Info:")
    studName = inputStudentInfo("string", "Enter new student name: ")

    while answer == 'y':
        subjCode = inputStudentInfo("string", "Enter subject code to edit: ").lower()

        if subjCode in subjectsCode:
            subjDesc = inputStudentInfo("string", "Enter subject description: ")
            numUnits = inputStudentInfo("int", "Enter number of units: ")

            while True:
                midGrade = inputStudentInfo("float", "Enter midterm grade: ")
                if 1.0 <= midGrade <= 5.0: break
                print("Grade must be between 1.0 and 5.0.")

            while True:
                finGrade = inputStudentInfo("float", "Enter finals grade: ")
                if 1.0 <= finGrade <= 5.0: break
                print("Grade must be between 1.0 and 5.0.")

            aveGrade = (midGrade + finGrade) / 2
            remarks = "Passed" if aveGrade <= 3.12 else "Failed"
        else:
            print("Invalid Subject Code. Please enter a valid subject.")

        answer = input("Do you want to edit another subject? [y/n]: ").lower()

    for line in studentRecords:
        index = line.split("|")
        if int(index[0]) == compStudNum:

            index[1] = studName

            if index[2].strip().lower() == subjCode:
                subjCode = subjCode.upper()
                subjDesc = subjDesc.title()
                temp.write(f"{compStudNum}|{studName}|{subjCode}|{subjDesc}|{numUnits}|{midGrade}|{finGrade}|{aveGrade:.2f}|{remarks}\n")
            else: temp.write("|".join(index))
        else: temp.write(line)

    temp.close()
    os.remove("student.txt")
    os.rename("temp.txt", "student.txt")

    print("Student record updated successfully.")

def viewStudent():
    files = open("student.txt", "r")
    studentRecords = files.readlines()
    files.close()
    print("\n[A] View All Students")
    print("[B] View Students by Student Number")
    answer = input("\nEnter your choice: ").upper()
    while answer not in ["A", "B"]:
        answer = input("Please enter a valid choice: ").upper()

    if answer == "A":
        print("\nAll Student Records:\n")
        for line in studentRecords:
            index = line.split("|")
            print(f"Student Number: {index[0]}\nStudent Name: {index[1]}\nSubject Code: {index[2]}\nSubject Description: {index[3]}"
                  f"\nNumber of Units: {index[4]}\nMidterm Grade: {index[5]}\nFinals Grade: {index[6]}\nAverage Grade: {index[7]}"
                  f"\nRemarks: {index[8]}")
    elif answer == "B":
        while True:
            studNum = inputStudentInfo("int", "Enter student number: ")
            found = any(int(line.split("|")[0]) == studNum for line in studentRecords)
            if found: break
            else: print("Student number not found. Please try again.")

        print(f"Student Records for Student {studNum}:")
        for line in studentRecords:
            index = line.split("|")
            if int(index[0]) == studNum:
                print(f"Student Number: {index[0]}\nStudent Name: {index[1]}\nSubject Code: {index[2]}\nSubject Description: {index[3]}"
                      f"\nNumber of Units: {index[4]}\nMidterm Grade: {index[5]}\nFinals Grade: {index[6]}\nAverage Grade: {index[7]}"
                      f"\nRemarks: {index[8]}")
    else: print("Invalid choice. Please try again.")

def deleteStudent():
    while True:
        files = open("student.txt", "r")
        studentRecords = files.readlines()
        files.close()

        studNum = inputStudentInfo("int", "Enter student number: ")
        found = any(int(line.split("|")[0]) == studNum for line in studentRecords)

        if found: break
        else: print("Student number not found. Please try again.")

    answer = input(f"Are you sure you want to delete student {studNum}? [y/n]: ").lower()

    if answer != 'y':
        print("Deletion cancelled."); return

    temp = open("temp.txt", "w")
    for line in studentRecords:
        index = line.split("|")
        if int(index[0]) != studNum:
            temp.write(line)
    temp.close()
    os.remove("student.txt")
    os.rename("temp.txt", "student.txt")

    print(f"Student {studNum} and their records have been deleted successfully.")

def main():
    print("\nStudent Management System")
    print("[A] Add Student")
    print("[E] Edit Student")
    print("[V] View Students")
    print("[D] Delete Student")
    print("[X] Exit")

    choice = input("\nEnter your choice: ").upper()
    while choice not in ["A", "E", "V", "D", "X"]:
        choice = input("Enter your choice: ").upper()

    if choice == "A":
        print("\nAdd Student")
        addStudent()
    elif choice == "E":
        print("\nEdit Student")
        editStudent()
    elif choice == "V":
        viewStudent()
    elif choice == "D":
        print("\nDelete Student")
        deleteStudent()
    elif choice == "X":
        print("\nExiting the Program... Thank you for using Student Management System!..")
    else:
        print("Invalid choice. Please try again.")

main()