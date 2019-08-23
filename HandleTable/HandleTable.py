import csv

print("Script de manipulacao da tabela de precos")
input()

#handleFile = open('TA_PRECO_MEDICAMENTO.csv','r')
#try:
#    readingFile = csv.reader(handleFile)
#    for linha in readingFile:
#        print(linha)
#finally:
#    handleFile.close()

print(open('TA_PRECO_MEDICAMENTO.csv','r',encoding="utf8").read())

input()    