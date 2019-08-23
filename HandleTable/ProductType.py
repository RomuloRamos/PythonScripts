

class Product:

    def __init__(self, intPos, strName, strType, strValue ):
        self.intPos = intPos
        self.strName = strName
        self.strType = strType
        self.floatValue = float(strValue.replace(",","."))

class ProductQueue:
#     def __init__(self, Product):
#         self.Queue.append(Product)
#         self.QueueHiValue.append(Product.intPos)
# #        if (Product.strType not in )
#         self.QueuePossibleTypes.append(Product.strType)
    Queue = []    

    def addProduct(self, Product):    
        self.Queue.append(Product)