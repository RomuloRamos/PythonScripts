class Product:

    def __init__(self, intPos, strName, strType, strValue ):
        self.intPos = intPos
        self.strName = strName
        self.strType = strType
        self.floatValue = float(strValue.replace(",","."))

class ProductQueue:
#    Queue = []
    floatMaxPriceValue = 0
    floatMinPriceValue = 0    
    intMaxPricePosition = []
    intMinPricePosition = []
    intSameSubstancePosition = []
    strArrayPossibleTypes = []

    def addProduct(self, Product):
        # self.Queue.append(Product)
        #  O produto com o maior preço de fábrica sem impostos 
        if(Product.floatValue > self.floatMaxPriceValue):
            self.floatMaxPriceValue = Product.floatValue
            self.intMaxPricePosition.clear() 
            self.intMaxPricePosition.append(Product.intPos)
        elif(Product.floatValue == self.floatMaxPriceValue):
            self.intMaxPricePosition.append(Product.intPos)
        # O genérico mais barato
        if (Product.strType == "Genérico"):
            if((self.floatMinPriceValue > Product.floatValue) or (len(self.intMinPricePosition) == 0)):
                self.floatMinPriceValue = Product.floatValue
                self.intMinPricePosition.clear()
                self.intMinPricePosition.append(Product.intPos)
            elif(self.floatMinPriceValue == Product.floatValue):
                self.intMinPricePosition.append(Product.intPos)
        #Os tipos possíveis de remédio
        if(Product.strType not in self.strArrayPossibleTypes):
            self.strArrayPossibleTypes.append(Product.strType)

# Print on console the medicines information 
    def printMedicines(self):
        print("O tipos de remédios são: ", self.strArrayPossibleTypes)
        print("Os genéricos mais baratos são: ", self.intMinPricePosition)
        print("Os remédios mais caros são: ", self.intMaxPricePosition)
#Return the position of element with max price     
    def getMaxPricePosition(self):
        return self.intMaxPricePosition
#Return the position of element with minumum price
    def getMinPricePosition(self):
        return self.intMinPricePosition    
        
