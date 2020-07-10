###############################################
# Author: Rafael Passos Guimarães
# E-mail: rapassos@gmail.com
# Date: 10/Jul/2020
###############################################

#Funções aritméticas 
#Soma
def soma(a,b):
    return a + b

#Subtração
def subtracao(a,b):
    return a - b

#Multiplicação
def multiplicacao(a,b):
    return a * b

#Divisão
def divisao(a,b):
    return a / b

print(soma(1,2))
print(soma(3,4))
print(subtracao(10,8))
print(subtracao(7,15))
print(multiplicacao(1,2))
print(multiplicacao(3,4))
print(divisao(1,2))
print(divisao(3,4))


#Classe Calculadora
class Calculadora:
    def __init__(self,num1,num2):
        self.a = num1
        self.b = num2
    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b


calc = Calculadora(11,3)
print(calc.a)
print(calc.b)
print(calc.soma())
print(calc.subtracao())
print(calc.multiplicacao())
print(calc.divisao())


#Classe Calculadora2
class Calculadora2:
    #def __init__(self):
    #    pass
    def soma(self,a ,b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b


calc2 = Calculadora2()
print(calc2.soma(1,3))
print(calc2.subtracao(5,4))
print(calc2.multiplicacao(2,3))
print(calc2.divisao(7,2))

#Classe Televisão
class Televisao:
    def __init__(self):
        self.power = False
        self.canal = 0
    
    def btnLigaDesliga(self):
        if self.power:
            self.power = False
            self.canal = 0
        else:
            self.power = True
            self.canal = 2

    def setCanal(self, canal):
        if self.power:
            self.canal = canal

    def upCanal(self):
        if self.power:
            self.canal+=1

    def downCanal(self):
        if self.power:
            self.canal-=1

tv = Televisao()
print('A televisão está ligada: {}'.format(tv.power))
print('A televisão está no canal: {}'.format(tv.canal))
tv.btnLigaDesliga()
print('A televisão está ligada: {}'.format(tv.power))
print('A televisão está no canal: {}'.format(tv.canal))
tv.upCanal()
print('A televisão está no canal: {}'.format(tv.canal))
tv.upCanal()
print('A televisão está no canal: {}'.format(tv.canal))
tv.setCanal(20)
print('A televisão está no canal: {}'.format(tv.canal))
tv.downCanal()
print('A televisão está no canal: {}'.format(tv.canal))
tv.btnLigaDesliga()
print('A televisão está ligada: {}'.format(tv.power))
print('A televisão está no canal: {}'.format(tv.canal))
tv.btnLigaDesliga()
print('A televisão está ligada: {}'.format(tv.power))
print('A televisão está no canal: {}'.format(tv.canal))
tv.setCanal(5)
print('A televisão está no canal: {}'.format(tv.canal))