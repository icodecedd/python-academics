import hands_on_activity_1

number = int(input('Input: '))

def addNumbers(number):
    Sm = 0
    for i in range(number):
        Sm += i+1
    return Sm
def ave(Sm):
    avg = 0
    avg = Sm/number
    return avg

print('Output:')
print('     Sum:', addNumbers(number))
print('     Average: ', ave(addNumbers(number)))

if number < ave(addNumbers(number)):
    print('     Dwarf')
else:
    print('     Not Dwarf')