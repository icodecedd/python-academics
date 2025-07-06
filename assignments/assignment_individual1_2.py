from assignments.assignment_individual1_1 import Product
import os

def inputData():
    ans = 'y'
    files = open("ProductInventory.txt", "r")
    print("\n\t\t[CREATE NEW PRODUCT ENTRY]\n")
    while ans == 'y':
        while True:
            prodNum = input("Product Number: ")
            if not prodNum.isdigit(): continue
            found = False
            files.seek(0)
            for file in files:
                parts = file.split(',')
                if parts[0] == prodNum: found = True; break
            if found: continue
            prodNum = int(prodNum)
            break

        while True:
            prodNa = input("Product Name: ").lower()
            if prodNa == "": continue
            found = False
            files.seek(0)
            for file in files:
                parts = file.split(',')
                if parts[1].lower() == prodNa: found = True; break
            if found: continue
            prodNa = prodNa.title(); break

        while True:
            intQuan = input("Initial Quantity: ")
            if not intQuan.isdigit(): continue
            intQuan = int(intQuan)
            if intQuan <= 0: continue
            else: break

        while True:
            price = input("Price: ")
            try:
                price = float(price)
                if price <=0: continue
                else: break
            except ValueError: continue

        printFile = Product(prodNum, prodNa, intQuan, price)
        printFile.writeFile()

        ans = input("Input Again[Y/N]: ").lower()
    files.close()

def productTransaction():
    found = False
    temp = open("TemporaryInventory.txt", "w")
    files = open("ProductInventory.txt", "r")
    compProdNum = input("Product Number Search: ")
    while not compProdNum.isdigit():
        compProdNum = input("Product Number Search: ")

    for file in files:
        parts = file.split(',')
        if parts[0] == compProdNum:
            found = True
            print("Record Found")

            choice = input("Purchase or Sell: ").lower()
            while choice not in ("purchase", "sell"):
                choice = input("Purchase or Sell: ").lower()

            while True:
                quantity = input("Quantity: ")
                if not quantity.isdigit(): continue
                quantity = int(quantity)
                if quantity <=0: continue
                else: break

            if choice == "purchase":
                totalQuantity = int(parts[2]) + quantity
                print(f"Total Quantity: {totalQuantity}")
            else:
                if quantity > int(parts[2]):
                    print("Not Enough Stock!")
                    totalQuantity = int(parts[2])
                else:
                    totalQuantity = int(parts[2]) - quantity
                    totalPrice = float(parts[3].strip()) * quantity
                    print(f"Total Cost Sold: {totalPrice}")

            fileFormat = f"{parts[0]},{parts[1]},{totalQuantity},{parts[3]}"
            temp.write(fileFormat)
        else: temp.write(file)

    files.close(); temp.close()

    if not found:
        print("Record Not Found")
        productTransaction()
    else:
        os.remove("ProductInventory.txt")
        os.rename("TemporaryInventory.txt", "ProductInventory.txt")

def mainDashboard():
    print("\n\t\t[PRODUCT TRANSACTION]\n")
    print("\t\t\t[A]dd New")
    print("\t\t\t[F]ind Product")
    print("\t\t\t[E]xit")
    choice = input("\nEnter Choice: ").upper()

    if choice == 'A': inputData()
    elif choice == 'F':
        print("\n\t\t[SEARCH PRODUCT INVENTORY]\n")
        productTransaction()
    elif choice == 'E': print("Exiting the Program...")
    else: print("Invalid Choice!")

mainDashboard()