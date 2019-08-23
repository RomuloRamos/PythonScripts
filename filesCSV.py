import csv

print("O modulo csv permite lidar com tabelas")
print("desse tipo de uma maneira bastante simples")

input() #Qualquer entrada do usuário, somente para criar uma pausa
myFile = open('tabela.csv', 'w') #Cria um arquivo e abre no modo Write
try:
    writer = csv.writer(myFile) #Instancia um objeto writer da classe/modulo csv
    writer.writerow( ('Nome','Idade','Sexo') ) #Adiciona o header da Tabela
    writer.writerow( ('Romulo','29','Masculino') ) #Insere linha de valores
    writer.writerow( ('Carlayne','23','Feminino') ) #Insere linha de valores
    writer.writerow( ('Mariana','23','Feminino') ) #Insere linha de valores
finally:
    myFile.close() #Fecha o arquivo criado

print(open('tabela.csv','r').read()) #Abre, lê e printa o arquivo anteriormente criado

input() #Qualquer entrada do usuário, somente para criar uma pausa

myFile = open('tabela.csv','r')
try:
    leitor = csv.reader(myFile)
    for linha in leitor:
        print(linha)
finally:
    myFile.close()

input()

myFile = open('tabela.csv','a')#Abre o arquivo no modo Append para acrescentar mais informação
try:
    writer = csv.writer(myFile)
    writer.writerow( ('Sara','23','Feminino') ) #Complementa a tabela inserindo novas linhas
    writer.writerow( ('Ingrid','20','Feminino') ) #Complementa a tabela inserindo novas linhas
finally:
    myFile.close()

input()

myFile = open('tabela.csv','r')
try:
    leitor = csv.reader(myFile)
    for linha in leitor:
        print(linha)
finally:
    myFile.close()

input()