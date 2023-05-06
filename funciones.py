
#creacion de funcion simple
#metodo para multiplicar
def multiplicacion(a,b):
    #multiplicacion
    print(f'la multiplicacion de {a}X{b} es igual a {a*b}')
    #comprobacion par
    print(f'Y este resultado es par: {par(a*b)}')
#evalua si un numero es par o impar
def par(a):
    #sentencia if = si % = residuo de divicion return mensaje
    if a % 2 == 0:
        return 'par'
    else:
        return 'Impar'

print('iniciar el software')
#llamado a la funcion
multiplicacion(3,4)
print("siguiente")
multiplicacion(5,5)