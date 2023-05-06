numero=0
print("tabla del 7")
#ciclo while para la tabla 7
while numero<=10:
    #lleva identacion
    print('7x'+str(numero)+"0"+str(numero*7)) #forma tradicional o nativa concatenar variables
    print(f'7x{numero}={numero*7}')   #manera interpolacion de texto y variables
    numero += 1
print("fin") 

