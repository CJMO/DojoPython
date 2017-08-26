
class dojo:

    def __init__(self,x,y,s):
        self.menor = x
        self.mayor = y
        self.salto = s
        self.rango = range(menor, mayor, salto)

    def sumar(self):
        suma = 0
        for i in self.rango:
            suma +=i
        print ("Suma: " , suma)


print ("Ingrese valor menor")
menor = int(input())

print ("Ingrese valor mayor")
mayor = int(input())

print ("Ingrese salto para el rango")
salto = int(input())

print ("Valores: ", menor, mayor)

rango = range(menor, mayor)

#suma = sumar(rango)

calcular = dojo(menor, mayor, salto)
calcular.sumar()
