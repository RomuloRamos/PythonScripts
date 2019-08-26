import csv
import ProductHandle


print("programa de teste")

produto1 = ProductHandle.Product(1,"remerio1","Genérico","100,00")
produto2 = ProductHandle.Product(2,"remerio2","Genérico","200,00")
produto3 = ProductHandle.Product(3,"remerio3","Genérico","300,00")
produto4 = ProductHandle.Product(4,"remerio4","naogenerico","100,00")
produto5 = ProductHandle.Product(5,"remerio5","Genérico","200,00")
produto6 = ProductHandle.Product(6,"remerio6","naogenerico","300,00")
produto7 = ProductHandle.Product(19,"remerio7","Genérico","100,00")

myQueue = ProductHandle.ProductQueue()

myQueue.addProduct(produto1)
myQueue.addProduct(produto2)
myQueue.addProduct(produto3)
myQueue.addProduct(produto4)
myQueue.addProduct(produto5)
myQueue.addProduct(produto6)
myQueue.addProduct(produto7)

produto = myQueue.getProduct(0)
print(produto.intPos, produto.strName, produto.strType, produto.floatValue)
produto = myQueue.getProduct(1)
print(produto.intPos, produto.strName, produto.strType, produto.floatValue)
produto = myQueue.getProduct(2)
print(produto.intPos, produto.strName, produto.strType, produto.floatValue)

myQueue.printMedicines()