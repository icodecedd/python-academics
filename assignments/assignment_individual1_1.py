class Product:

    def __init__(self, prodNum, prodName, inQuantity, price):
        self.prodNum = prodNum
        self.prodName = prodName
        self.inQuantity = inQuantity
        self.price = price

    def writeFile(self):
        files = open("ProductInventory.txt", "a")
        fileFormat = f"{self.prodNum},{self.prodName},{self.inQuantity},{self.price}\n"
        files.write(fileFormat)
