# input number 1 and number 2 and return its value
def inputNumber():
    while True:

        num1 = int(input("Number 1: "))
        if num1 < 0:
            exit()
        else:
            num2 = int(input("Number 2: "))
            if num2 < 0:
                exit()

        return num1, num2

# compute Russian Multiplication and return the sum
def computeNumber(number1, number2):
    finalNum = number1
    result1 = []
    result2 = []
    sumArray = []

    sum = 0
    result1.append(number1)
    result2.append(number2)

    while number1 > 1:
        temp1 = number1//2
        number1 = number1//2
        result1.append(temp1)
        temp2 = number2*2
        number2 = number2*2
        result2.append(temp2)
        indexRange = range(0, len(result1))
        if temp1 % 2 != 0:
            sumArray.append(int(temp2))
    else:
        for i in range(len(sumArray)):
            sum += sumArray[i]
        print("Outputs")
        print("First Number          Second Number")
        indexRange = range(0, len(result1))
        for num in indexRange:
            print(f"{result1[num]:7}                   {result2[num]}")
    sumArray = " + ".join(map(str, sumArray))

    return f"{sumArray} = {sum}"

# compute Greatest Common Divisor and return the GCD
def computeGCD(number1, number2):
    finalNum = number1
    finalGCD = 0
    print(f"GCD({number1},{number2})")
    while True:
        if finalNum != 0:
            result = number1 % number2
            m = number2
            n = result
            number1 = m
            number2 = n
            print(f"GCD({m},{n})")
            finalNum = n
            finalGCD = m

        else:
            break
    return finalGCD

#COMPUTE BOTH number GCF
def GCF(num1,num2):
    num1factor = []
    num2factor = []
    greatest = 0
    string = ""
    for i in range(1,num1+1):
        if num1%i == 0:
            string += str(i) + " "
            num1factor.append(i)
    print("\nFirst Number: " + string)
    string = ""
    for i in range(1, num2+1):
        if num2 % i == 0:
            string += str(i) + " "
            num2factor.append(i)
    print("Second Number: "
          "" + string)
    if num1>num2:
        limit = num1
    else:
        limit = num2
    for i in range(1,limit+1):
        if num1%i == 0:
            if num2%i == 0:
                greatest = i
    print(f"\nGCF: {greatest}")

# function calls-

number1, number2 = inputNumber()
sum = computeNumber(number1, number2)
print(f"\nProduct: {sum}")
finalGCD = computeGCD(number1, number2)
print(f"GCD: {finalGCD}")
GCF(number1,number2);
