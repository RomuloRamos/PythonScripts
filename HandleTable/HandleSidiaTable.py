# Este é um script simples com o objetivo de filtrar elementos de uma planilha
# e retornar informações no terminal e em um arquivo de saída.

# Para mais informações: romulo.ramos@gee.inatel.br

import csv
import ModelHandle
import codecs

# Class with basical struct to handle the csc file
class HandleTable:
    queueToSave = [] #List to elements to be saved on outputFile
    listNames = [] #List with name of elements to be counted as diferent on outputFile
    floatValueSum = 0 #Variable to count the medicines values sum
    MyQueue = ModelHandle.ProductQueue() #      
          

    def getQuantDiferentTypes(self):
        return len(self.listNames)

    def outputConsole(self):    
        handleFile = open('ImsModels.csv','r')
        try:
            self.MyQueue.printMedicines()
            readingFile = csv.reader(handleFile, delimiter = ';')
            counter = 0
            intMaxPricePosition = self.MyQueue.getMaxPricePosition()
            intMinPricePosition = self.MyQueue.getMinPricePosition()
            for line in  readingFile:    
                for positions in intMaxPricePosition:
                    if (positions == counter):
                        print("Medicamento com maior preço: ")
                        print(line)
                for positions in intMinPricePosition:
                    if (positions == counter):
                        print("Medicamento Genérico com menor preço:")
                        print(line)
                
                counter = counter+1        
        finally:
            handleFile.close()
        print("Quantidade de produtos diferentes em outputFile: ",self.getQuantDiferentTypes())
    
    def sumValueMedicines(self, floatValue):
        self.floatValueSum = self.floatValueSum + floatValue 

    def getsumValueMedicines(self):
        return self.floatValueSum      

def main():
    print("Script de manipulacao da tabela de precos")
    input()

    handleFile = codecs.open('ImsModels.csv','Ur', encoding='utf-16')
    handleTable = HandleTable()
    try:
        readingFile = csv.reader(handleFile, delimiter = ';')
        counter = 0 
        intCountryPos = 0
        intSkuPos = 0
        intVoLTEPos = 0
        for line in readingFile:
            # print(line)
            if counter == 0:
                print(line)
                intCountryPos = line.index("Peru")
            elif counter == 1:
                print(line)
                intSkuPos = line.index("SAM")
            
            else:
                if ((line[intSkuPos] == "VERDADEIRO") or (line[intSkuPos+1] == "VERDADEIRO")):
                    print(line[0], ' / ',  line[1])

            counter = counter+1  

        print('intCountryPos = ',intCountryPos)
        print('intSkuPos = ',intSkuPos)



    finally:
        handleFile.close()  

if __name__ == "__main__":
    main()
 