
# input
number = int(input("Input: "))
while number < 1:
    print("Output: Invalid")
    number = int(input("Input: "))

# initialization of variables
result = 1
first = 1
sequence = [result, first]

# process
if number > 1:
    while result <= number:
        temp = result
        result += first
        sequence.append(result)
        first = temp
elif number == 1:
    print("Output: (1, 1)")

# output
if number > 1:
    finalSequence = tuple(sequence)
    print(f"Output: {finalSequence[0:-1]}")

