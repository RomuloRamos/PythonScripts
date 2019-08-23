def solution(A, B):

    if((A<0) or (B<0) or (A>999999999) or ((B>999999999))):
        return -1
    strA = str(A)
    strB = str(B)

    print("strA = ", strA)
    print("strB = ", strB)

    return strB.find(strA)

print("RETORNO: ",solution(50,100000))
print("RETORNO: ",solution(1000000001,100000))
print("RETORNO: ",solution(50,1000000001))
print("RETORNO: ",solution(-2,100000))
print("RETORNO: ",solution(10,-100000))

print("RETORNO: ",solution(10,100000))
print("RETORNO: ",solution(0,100000))
print("RETORNO: ",solution(10,1100))
print("RETORNO: ",solution(10,22100000))
print("RETORNO: ",solution(10,333100000))
print("RETORNO: ",solution(10,444010000))
