import csv

print("Script de manipulacao da tabela de precos")
input()

handleFile = open('TA_PRECO_MEDICAMENTO.csv','r', encoding='utf-8-sig')
try:
    readingFile = csv.reader(handleFile, delimiter = ';')
    for linha in readingFile:
        print(linha)
        print(linha[0])
        print(linha[1])
        input()
finally:
    handleFile.close()

#print(open('TA_PRECO_MEDICAMENTO.csv','r',encoding="utf8").read())

input()    