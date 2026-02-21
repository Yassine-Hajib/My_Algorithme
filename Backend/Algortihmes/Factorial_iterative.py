def iterativeFactoriel(n):
    if n==0 :
        return 1
    i=1
    res=1
    for i in range(1,n+1):
        res= res*i
    return res