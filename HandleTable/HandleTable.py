# Este é um script simples com o objetivo de filtrar elementos de uma planilha
# e retornar informações no terminal e em um arquivo de saída.

# Para mais informações: romulo.ramos@gee.inatel.br

import csv
import ProductHandle

# Class with basical struct to handle the csc file
class HandleTable:
    queueToSave = [] #List to elements to be saved on outputFile
    listNames = [] #List with name of elements to be counted as diferent on outputFile
    floatValueSum = 0 #Variable to count the medicines values sum
    MyQueue = ProductHandle.ProductQueue() #      
# Insert a ner element to be save on outputFile
    def outputFileAppend(self, strNewLine):
        self.queueToSave.append(strNewLine)

    def outputFileGenerate(self): 
        outputFile = open('output.csv', 'w', encoding='utf-8-sig',newline="")        
        try:
            self.queueToSave.sort()
            
            outputWriter = csv.writer(outputFile, delimiter=';')
            for line in self.queueToSave:
                outputWriter.writerow((line))
                self.listNames.append(line[0])  
            self.listNames = list(set(self.listNames))
        finally:
            outputFile.close()            

    def getQuantDiferentTypes(self):
        return len(self.listNames)

    def outputConsole(self):    
        handleFile = open('TA_PRECO_MEDICAMENTO.csv','r', encoding='utf-8-sig')
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

    handleFile = open('TA_PRECO_MEDICAMENTO.csv','r', encoding='utf-8-sig')
    handleTable = HandleTable()
    try:
        readingFile = csv.reader(handleFile, delimiter = ';')
        counter = 0 
        for line in readingFile:
    #        print(line)
            if counter == 0:
                print(line)
                strPFsI = line.index('PF Sem Impostos')
                strProductType = line.index('TIPO DE PRODUTO (STATUS DO PRODUTO)')
                strPriceScheme = line.index('REGIME DE PREÇO')
                strComerc2018 = line.index('COMERCIALIZAÇÃO 2018')
                strTarja = line.index('TARJA')
                strSubstance = line.index('PRODUTO')


                print('strPFsI = ',strPFsI)
                print('strProductType = ',strProductType)
                print('strPriceScheme = ',strPriceScheme)
                print('strComerc2018 =  ',strComerc2018)
                print('strSubstance =  ',strSubstance)
        
            else:
                MyProduct = ProductHandle.Product(counter,line[0],line[strProductType],line[strPFsI])
                handleTable.MyQueue.addProduct(MyProduct)
                if ((line[strComerc2018] == "Sim") and (line[strTarja] == "Tarja Vermelha")
                and (float(line[strPFsI].replace(",",".")) < 100)):
                    handleTable.sumValueMedicines(float(line[strPFsI].replace(",",".")))
                    handleTable.outputFileAppend(line)

            counter = counter+1  
    finally:
        handleFile.close()  

    handleTable.outputFileGenerate()   
    handleTable.outputConsole()

if __name__ == "__main__":
    main()
 