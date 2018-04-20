b= int(input('ingrese la base: '))
p=int(input ('ingrese la potencia: '))
f=int(input('ingrese el modulo: '))
x=1
mod= 1
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
# x= x*n*(m) and n= n*n*(m)
#numero = int(input('Introduce el número a convertir a binario: '))
#print("Mira esta es la base: "+ b +" "+ "y esta es su potencia: "+ x)
#print(binarizar(b))
# print(binarizar(p))
# print(binarizar(f))
k = int(binarizar(b))
n = int(binarizar(p))
m = int(binarizar(f))

for i in range(0,1):
    if n==1:
        int(mod = x*n)
    else:
        res = int(mod * mod)
print (res)
