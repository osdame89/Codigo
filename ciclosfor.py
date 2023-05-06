"""
el cilco for tiene la sigueinte sintaxis
for elemnto in interable:
    codigo

#uso basico para iteral usando ciclo for
numeros=[8,7,5,4,3,2,0,2,3]

for n in numeros:
    print(n)
"""
#diciconario en pythopn
valores={
    'A':3,
    'E':4,
    'I':8,
    'O':10,
    'R':11
}
#imprimiendo la llave de un diccionario

for d in valores:
    print(d)

#imprimiendo el valor del diccionario
for h in valores.values():
    print(h)

#imprimiendo el valor y llave del diccionario

for l, v in valores.items():
    print('d =',l,'| v=',v)

#for nativo clase range

for i in range(11):
    print(i)

# clase range incremento de valores minimo y un maximo

for i in range(2,11,2):
    print(i)