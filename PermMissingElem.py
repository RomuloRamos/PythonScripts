def solution(A):

    intCouter = 1
    intIndex = 0
    intList1 = A[:]
    bFind = True
    bLoopControl = False
    while bFind:
        for intValue in intList1:
            print("intIndex: ", intIndex)
            print("intCouter: ", intCouter)
            print("intValue: ", intValue)
           
            if(intIndex == 0):
                bLoopControl = True
                print("bLoopControl = ", bLoopControl)
            
            if(intCouter == intValue):
                print("Achado o valor: ", intCouter)
                intCouter = intCouter + 1
                intList1.pop(intIndex)
                print("intList1 = ", intList1)
                bLoopControl = False
                print("bLoopControl = ", bLoopControl)
                print("len(intList1) = ", len(intList1))
            
            if (intIndex < (len(intList1)-1)):
                intIndex = intIndex+1
            else:    
                intIndex = 0

        if((len(intList1) == 0) or (bLoopControl == True)):
            print("\nintList = ", intList1)
            print("Length = ", len(intList1))
            print("bLoopControl = ", bLoopControl)
            bFind = False

    return intCouter   

print("Teste de algoritmo\n Chamando o método solution()\n")
A = [1,2,3,-5]
print("\nParâmentros: A= ", A)
returnedVaule = solution(A)
print("Retorno: ",returnedVaule)

A = [1,-2,3,4]
print("\nParâmentros: A= ", A)
returnedVaule = solution(A)
print("Retorno: ",returnedVaule)

A = [-2,3,4]
print("\nParâmentros: A= ", A)
returnedVaule = solution(A)
print("Retorno: ",returnedVaule)