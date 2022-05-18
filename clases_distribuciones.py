import math
import numpy as np
import mpmath
import matplotlib.pyplot as plt

e = 2.17
pi = 3.14

class Congruencial_Multiplicativo:
    def __init__(self,seed,const,mod):
        self.seed=seed
        self.const=const
        self.mod=mod

    def generar_numero(self):
        num=(self.const*self.seed)%self.mod
        num2=float(num)/float(self.mod-1)
        self.seed=num
        return num2

class Chi_Cuadrado:
    def __init__(self,n,gama,x):
        self.n=n
        self.gama=gama
        self.x=x
    def chi_cuadrado(self):
        x=self.x.generar_numero()
        #total=(((x/2)**((self.n/2)-1))*(e**(-x/2)))/2*self.gamma*(self.n/2)
        calculo1=((x/2)**((self.n/2)-1))
        calculo2=(e**(-x/2))
        calculo3=(2*self.gama*(self.n/2))
        total_chi_cuadrado=(calculo1*calculo2)/calculo3
        return [total_chi_cuadrado,x]

class T_Student:
    def __init__(self,n,gama,t):
        self.n=n
        self.gama=gama
        self.t=t
    def t_student(self):
        t=self.t.generar_numero()
        calculo1=(self.gama*((self.n+1)/2))
        calculo2=(math.sqrt(self.n*pi)*self.gama*(self.n/2))
        calculo3=(1+(t**2)/2)**((-self.n+1)/2)
        total_t_student=(calculo1/calculo2)*calculo3
        return [total_t_student,t]

class Pareto:
    def __init__(self,k,alfa,x):
        self.k=k
        self.alfa=alfa
        self.x=x
    def pareto(self):
        x=self.x.generar_numero()
        total_pareto=(self.alfa*(self.k**self.alfa))/x**(self.alfa+1)
        return [total_pareto,x]

class Erlang:
    def __init__(self,k,mu,x):
        self.k=k
        self.mu=mu
        self.x=x
    def erlang(self):
        x=self.x.generar_numero()
        calculo1=(x**(self.k-1))*e**(-x/self.mu)
        calculo2=self.mu**(math.factorial(self.k-1))
        total_erlang=calculo1/calculo2
        return [total_erlang,x]

class Exponencial:
    def __init__(self,gama,x):
      self.x=x
      self.gama=gama
    def exponencial(self):
      x=self.x.generar_numero()
      calculo=(1/self.gama)*(e**(-x/self.gama))
      return [calculo,x]