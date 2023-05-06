class coche:
    #atributos: caracteristicas que los hace similares
    ruedas=4
    color=''
    aceleracion=0
    velocidad=0

    #Metodo constructor
    def __init__(self,color,aceleracion): #self se utiliza para tener contexto de codigo
        self.color=color
        self.aceleracion=aceleracion
        self.velocidad=0

    #metodos
    def acelelar(self):
        #self.velocidad=self.velocidad+self.aceleracion #manera larga
        self.velocidad+=self.aceleracion #manera corta de escritura
        return self.velocidad

class autoVolador(coche):
    #atributos coche volador
    alas=False
    ruedas=6

    #Constructor
    def __init__(self, color, aceleracion, estaVolando=False):
        super().__init__(color, aceleracion)
        self.estaVolando=estaVolando

    #metodo carro vuele
    def vuela(self):
        self.estaVolando=True
        return "Estoy volando"
#instancia de objetos 
c1=coche('rojo',20)
#llamado a objeto
print(c1.color," ",c1.acelelar())
print(c1.acelelar())
print(c1.acelelar())

#llamar coche colador
cv1=autoVolador('negro',60)
print(cv1.color)
print(cv1.vuela())
print(cv1.acelelar())