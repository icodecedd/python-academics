class Student:
    def __init__(self, studNum, studName, scores):
        self.studNum = studNum
        self.studName = studName
        self.scores = scores
        self.average = 0

    def __str__(self):
        return f"Name: {self.studName}, Scores: {self.scores}, Average: {self.average} Grade: {self.getGrade()}"

    def calculateAverage(self):
        self.average = sum(self.scores) / len(self.scores)

    def getGrade(self):
        if self.average >= 93:
            return "A"
        elif self.average >= 87:
            return "B"
        elif self.average >= 82:
            return "C"
        elif self.average >= 75:
            return "D"
        else:
            return "F"

def addStudent():
    studNum = input("Enter student number: ")
    studName = input("Enter student name: ")
    scores = []
    while True:
        for i in range(3):
            scores.append(int(input(f"Enter score for subject {i+1}: ")))

        if len(scores) == 3: break
        else: print("Invalid number of scores. Please try again.")
    student = Student(studNum, studName, scores)
    student.calculateAverage()
    with open ("student.txt", "a") as file:
        file.write(f"{studNum}, " + student.__str__() + "\n")

addStudent()