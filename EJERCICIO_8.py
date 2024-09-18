#NUMERO INSANO 
n=int(input("Ingrese la cantidad de rondas a jugar:"))
for _ in range (n):
    a,b,c=map(int,input().split())
    if a==b:
        print("Luisin")
    elif a==c:
        print("Sami")
    elif b==c:
        print("Herland")