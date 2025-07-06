# Function Sample 1
#---------------------------------------------
# def info(age, name):
#     print("name", name)
#     print("age", age)
#
# info(name = "ely", age = 18)

# Function Sample 2
#---------------------------------------------
# def main():
#  num = (int)(input('enter a no.: '))
#  factorial(num)
# def factorial(no):
#  fact = 1
#  i = no
#  while(i > 1):
#  fact *= i
#  i = i - 1
#  print('factorial: ', fact)
# #main()

# Function Sample 3
#---------------------------------------------
# lst = [1,2,3,4,5]
# def output(mylist):
#     for i in mylist:
#         print(i)
#
# def out(listing):
#     for i in listing:
#         print(i)
#
# output(lst)
# out(lst)

# Function Sample 4
#---------------------------------------------
# grades = [0,0,0,0,0,0]
# def inputs():
#     name = input('enter a name: ')
#     for i in range(0,6):
#         g = float(input('enter a grade: '))
#         grades.append(g)
#     ave = average(grades)
#     print('average: ', ave)
#     remarks(ave)
#
# def average(grd):
#     sum = 0
#     for i in grades:
#         sum += i
#     ave = sum / 6
#     return ave
#
#
# def remarks(ave):
#     if ave <= 3.12:
#         rem = 'Passed'
#     else:
#         rem = 'Failed'
#     print('Remarks:', rem)
#
# inputs() # function call for inputs()

# Lambda Function Sample 1
#---------------------------------------------
# x=5; y=10
# sum = lambda x, y: x+y; print(sum(x,y))
# diff = lambda x, y: x-y
# z = sum(x, y)
# print(z)
# print("difference: ", diff(x, y))

# Lambda Function Sample 2
#---------------------------------------------
# num1 = int(input('First No.: '))
# num2 = int(input('Second No.: '))
# sum = lambda num1, num2: num1+num2; print(num1); print(num2)
# diff = lambda num1, num2: num1-num2
# prod = lambda num1, num2: num1*num2
# quo = lambda num1, num2: num1/num2
# mod = lambda num1, num2: num1%num2
# div = lambda num1, num2: num1//num2
# expo = lambda num1, num2: num1**num2; print(num1, num2)
#
# print("Sum: ", sum(num1, num2))
# print("Difference: ", diff(num1, num2))
# print("Product: ", prod(num1, num2))
# print("Quotient: ", quo(num1, num2))
# print("Remainder: ", mod(num1, num2))
# print("Whole Number in Quotient: ", div(num1, num2))
# print("Exponent: ", expo(num1, num2))

