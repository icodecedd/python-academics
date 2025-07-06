# File Handling Sample 1
#---------------------------------------------
# name = "cedrick"
# age = 20
# value = name + "\t" + str(age) + "\n"
#
# file = open("sample.txt", "a") // "a" is used for appending
# file.write(value)
#
# for i in range(0, 3):
#     name = input("name: ")
#     age = int(input("age: "))
#     value = name + "\t" + str(age) + "\n"
#     file.write(value)
# file.close()
#
# file = open("sample.txt", "r") // "r" is used for reading
# lines = file.readlines() // read each line in the file txt
# for line in lines:
#     print(line)

# File Handling Sample 2
#---------------------------------------------
# import os
# file = open("example.txt", "r") # "r" is used for reading
# lines = file.readlines() # read each line in the file txt
# for line in lines:
#     print(line)
# file.close()
#
# os.rename("example.txt", "sample.txt") // rename the file <file to be renamed> , <filename>
# os.remove("record.txt") // remove the file txt
#
# file = open("sample.txt", "r")
# lines = file.readlines() # read each line in the file txt
# for line in lines:
#     print(line)
# file.close()

# File Handling Sample 3
#---------------------------------------------
import os

class Employee:
    def __init__(self, name, rate, hrs, gross):
        self.name = name
        self.rate = rate
        self.hrs = hrs
        self.gross = gross

    def write_file1(self):
        file = open("sEmployee.txt", "a")
        empRec = f"{self.name:10}\t{self.rate:10}\t{self.hrs:10}\t{self.gross:10}\n"
        file.write(empRec)

    def temp_write(self):
        temp = open("sTemporary.txt", "a")
        empRec = f"{self.name:10}\t{self.rate:10}\t{self.hrs:10}\t{self.gross:10}\n"
        temp.write(empRec)

    class GrossPay:
        def __init__(self, rate, hrs):
            self.rate = rate
            self.hrs = hrs

        def compute(self):
            return self.rate * self.hrs

def add_rec():
    ans = 'y'
    files = open("sEmployee.txt", "a")
    while ans == 'y':
        empName = input("employee name: ")
        empRate = float(input("rate per hour: "))
        empHour = int(input("hours worked: "))

        grossPay = Employee.GrossPay(empRate, empHour)
        empGross = grossPay.compute()
        employee = Employee(empName, empRate, empHour, empGross)
        employee.write_file1()
        ans = input("input again?[y/n]: ")
    files.close()

def disc_rec():
    print("\n\n")
    print(f"{'Name':10}\t\t{'Rate':10}\t{'Hours':10}\t{'Gross':10}")
    with open("sEmployee.txt", "r") as files:
        for file in files:
            print(file)

def edit_rec():
    edName = input("employee name to be edited: ")
    temp = open("sTemporary.txt", "a")
    files = open("sEmployee.txt", "r")
    for file in files:
        if file.find(edName) == 0:
            empName = input("employee name: ")
            empRate = float(input("rate per hour: "))
            empHour = int(input("hours worked: "))

            grossPay = Employee.GrossPay(empRate, empHour)
            empGross = grossPay.compute()
            employee = Employee(empName, empRate, empHour, empGross)
            employee.temp_write()
        else:
            temp.write(file)
    files.close()
    temp.close()
    os.remove("sEmployee.txt")
    os.rename("sTemporary.txt", "sEmployee.txt")

def del_rec():  
    delName = input("employee name to be edited: ")
    temp = open("sTemporary.txt", "a")
    files = open("sEmployee.txt", "r")
    for file in files:
        if file.find(delName) != 0:
            temp.write(file)
    files.close()
    temp.close()
    os.remove("sEmployee.txt")
    os.rename("sTemporary.txt", "sEmployee.txt")

def transaction():
    ans = 'Y'
    while ans == 'Y':
        print("[A]dd")
        print("[E]dit")
        print("[D]elete")
        print("D[I]splay")
        print("E[X]it")
        ans = input("choose your transaction: ")
        if ans == 'A':
            add_rec()
        elif ans == 'E':
            edit_rec()
        elif ans == 'D':
            del_rec()
        elif ans == 'I':
            disc_rec()
        else: print("End of Program!")

# function call
transaction()