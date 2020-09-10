def e_cuadratica(n):
    r=1
    while n>0:
        r=r+(1/factorial(n))
        n=n-1
    return r

def factorial(n):
    f=1
    while n>0:
        f=f*n
        n=n-1
    return f

def e_lineal(n):
    r=1
    f=1
    while n>0:
        f=f*n
        r=r+(1/f)
        n=n-1
    return r
