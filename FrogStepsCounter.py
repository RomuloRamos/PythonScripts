def solution(X,Y,D):

    intStartPoint = X
    intStep = D
    intTarget = Y

    intDistance = (intTarget-intStartPoint)
    if ((intDistance % intStep) == 0):
        return int(intDistance/intStep)
    else:
         return int((intDistance/intStep)+1)



print("Teste de algoritmo\n Chamando o método solution()\n")
X = 10
Y = 85
D = 30
print("Parâmentros: X=%d , Y=%d, D=%d", X, Y, D)
returnedVaule = solution(X,Y,D)
print("Retorno: ",returnedVaule)
