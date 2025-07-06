

class Product:

    def __init__(self, productNumber, productName, productQuantity):
        self.productNumber = productNumber
        self.productName = productName
        self.productQuantity = productQuantity

    def putProductRecord(self):
        records = open("product.txt", "a")
        productRecord = f"{self.productNumber},{self.productName},{self.productQuantity}\n"
        records.write(productRecord)

def getlast(pathfile):
    last_line = 0
    file = open(pathfile, "r")
    for line in file:
        last_line = line
    file.close()
    return last_line

def addProductRecord():
    ans = 'y'
    print("\n\t\tINPUT PRODUCT RECORD")
    while ans == 'y':
        print()
        while True:
            prodNum = input("Product Number:\t\t")
            if not prodNum.isdigit():
                print("Product Number must not contain any char")
                continue
            elif int(prodNum) < 1:
                print("Product Number must not be less than 1 ")
                continue
            prodNum = int(prodNum)
            break

        while True:
            prodNa = input("Product Name:\t\t")
            if prodNa == "":
                print("Product Name must not be empty.")
                continue
            prodNa = prodNa.title(); break

        while True:
            prodQuan = input("Initial Quantity:\t")
            if not prodQuan.isdigit():
                print("Quantity must not contain any char")
                continue
            elif int(prodNum) < 1:
                print("Initial Quantity must not 0 or negative")
                continue
            prodQuan = int(prodQuan)
            if prodQuan <= 0:
                print("Quantity must be greater than 0")
                continue
            else: break

        saveRecord = Product(prodNum, prodNa, prodQuan)
        saveRecord.putProductRecord()

        ans = input("Do you want to add more? [y/n]: ").lower()
        while ans not in ['y', 'n']:
            print("Error: \'y\' and \'n\' only")
            ans = input("Do you want to add more? [y/n]: ").lower()

def showAllProducts():
    records = open("product.txt", "r")
    print("\n\t\tALL PRODUCT RECORDS\n")
    for record in records:
        row = record.split(',')
        print(f"Product Number:\t\t{row[0]}\nProduct Name:\t\t{row[1]}\nQuantity:\t\t\t{row[2]}")
    records.close()

def search():
    print("\n\t\tSEARCH PRODUCT")
    counter = 0
    while True:
        num = input("Product Number: ")
        file = open("product.txt", "r")
        lastLine = getlast("product.txt")
        for line in file:
            fields = line.split(",")
            if num == fields[0]:
                print("Product Found")
                counter += 1
                while True:
                    ans = input("Purchase or Sell? (p/s): ")
                    if ans.lower == 'p' or ans.lower == 's':
                        break
                    else:
                        print("Only p and s")
                if ans.lower == 'p':
                     while True:
                         quan  = input("Quantity")
                         if int(quan) < 1:
                             print("Input must more than 0")
                         elif int(quan) > int(fields[2]):
                             print("Not enough quantity")
                         else:
                             break
                     file2 = open("product.txt", "r")
                     for line1 in file2:
                         fields1 = line.split(",")
                         if num == fields[0]:
                             prod = f"{num},{fields1[1]}, {int(fields1[2]) - int(quan)}"
                             print(prod)
                         else:
                             print(line1)
                elif ans.lower == 's':
                    while True:
                        quan = input("Quantity")
                        if int(quan) < 1:
                            print("Input must more than 0")
                        elif int(quan) > int(fields[2]):
                            print("Not enough quantity")
                        else:
                            break
                    file2 = open("product.txt", "r")
                    for line1 in file2:
                        fields1 = line.split(",")
                        if num == fields[0]:
                            prod = f"{num},{fields1[1]}, {int(fields1[2]) + int(quan)}"
                            print(prod)
                        else:
                            print(line1)

                # break
            elif line == lastLine:
                print("Record not Found")
        if counter > 0:
            break

# addProductRecord()
# showAllProducts()
# search()