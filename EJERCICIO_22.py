def serie_sube_y_baja(n):
    t=5; p=1; s=1;
    for i in range(1,n):
        t=t-s
        p=p+1
        if p == 5:
            s= s*(-1)
            p=1
    return t
def fibonacci(n):
    a=-1; b=1; t2=a+b;    
    for i in range(1,n):
        a=b
        b=t2
        t2=a+b
    return t2
n,x=map(int,input().split())
print(x**serie_sube_y_baja(n)," " ,fibonacci(n),"!")
        
    