
dictionary1 = {}
askAgain = 'Yes'
number = 0
totalNumber = 0
while askAgain == 'Yes' or askAgain == 'yes':

    # input
    salesNum = int(input("Salesman Number: "))
    salesName = input("Salesman Name: ")
    qt1 = float(input("First Quarter: "))
    qt2 = float(input("Second Quarter: "))
    qt3 = float(input("Third Quarter: "))
    qt4 = float(input("Fourth Quarter: "))
    askAgain = input("New Record: ")

    # process
    totSales = qt1 + qt2 + qt3 + qt4
    totalComm = totSales * .20
    dictionary1.update({
        f'Salesman Number{number}': salesNum,
        f'Salesman Name{number}': salesName,
        f'Total Sales{number}': totSales,
        f'Total Commission{number}': totalComm
    })
    dictionary1.update(dictionary1)
    number += 1

totalNumber = number
# output
for number in range(totalNumber):
    print(f"\nSalesman Number: {dictionary1.get(f'Salesman Number{number}')}")
    print(f"Salesman Name: {dictionary1.get(f'Salesman Name{number}')}")
    print(f"Total Sales: {dictionary1.get(f'Total Sales{number}')}")
    print(f"Total Commission: {dictionary1.get(f'Total Commission{number}')}")
    print()