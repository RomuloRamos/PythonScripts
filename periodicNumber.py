def solution(n):
    d = [0] * 30
    print("d = ", d)
    l = 0
    while (n > 0):
        d[l] = n % 2
        print("d[l] = ",d[l])
        print("n = ",n)
        n //= 2
        print("n = ",n)
        l += 1
        print("l = ",l,"\n\n\n")
    for p in range(1, 1+l):
        print("\nd[] = ",d)
        print("range(1, 1 + l) = ",range(1, l))    
        print("p = ",p)
        ok = True
        for i in range((l+1) - (p+1)):
            print("i = ",i)
            print("d[i] = ",d[i])
            print("d[i + p] = ",d[i + p])
            if ((d[i] != d[i + p]) and (d[i] == 0)):
                print("ok = False")
                print("p = ",p)
                ok = False
                break
        if ok:
            return p
                
    return -1

print("Teste do algoritimo!!!\n")
n = 34952    
print("Para n = ",n,",solution return = ",solution(n))
n = 34953    
print("Para n = ",n,",solution return = ",solution(n))
n = 34954    
print("Para n = ",n,",solution return = ",solution(n))
n = 60075   
print("Para n = ",n,",solution return = ",solution(n))