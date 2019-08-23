import csv
import ProductType

print("Script de manipulacao da tabela de precos")
input()

handleFile = open('TA_PRECO_MEDICAMENTO.csv','r', encoding='utf-8-sig')

MyQueue = ProductType.ProductQueue()

try:
    readingFile = csv.reader(handleFile, delimiter = ';')
    counter = 0 
    for linha in readingFile:
#        print(linha)
        if counter == 0:
            strPFsI = linha.index('PF Sem Impostos')
            strProductType = linha.index('TIPO DE PRODUTO (STATUS DO PRODUTO)')
            strPriceScheme = linha.index('REGIME DE PREÇO')

            print('strPFsI = ',strPFsI)
            print('strProductType = ',strProductType)
            print('strPriceScheme = ',strPriceScheme)
        else:
            print('Nome: ', )
            MyProduct = ProductType.Product(counter,linha[0],linha[strProductType],linha[strPFsI])
            MyQueue.addProduct(MyProduct)
            print(MyQueue.Queue)
#            print('PF sem Impostos = ',type(linha[strPFsI]))
#            print('Tipo de Produto = ',linha[strProductType], type(linha[strProductType]) )
#            print('Regime de Preço = ',linha[strPriceScheme])
        counter = counter+1    

        input()
finally:
    handleFile.close()

#print(open('TA_PRECO_MEDICAMENTO.csv','r',encoding="utf8").read())

input()    