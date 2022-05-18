import math
import numpy as np
import mpmath
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import binom

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

class Congruencial_Multiplicativo_Entero:
    def __init__(self,seed,const,mod):
        self.seed=seed
        self.const=const
        self.mod=mod

    def generar_numero_entero(self):
        num=(self.const*self.seed)%self.mod
        num2=float(num)/float(self.mod-1)
        self.seed=num
        return num

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

class Bernoulli:
    def __init__(self,rep,p,x):
      self.rep=rep
      self.p=p
      self.x=x
    def bernoulli(self):
      list1 = list()
      list2 = list()
      for i in range(self.rep):
          x=self.x.generar_numero()
          list1.append(x)
      for j in range(len(list1)):
          if(list1[j]<=self.p):
              list2.append(1)
          else:
              list2.append(0)
      return list2

class Binomial:
    def __init__(self,n,p,x):
        self.n=n
        self.p=p
        self.x=x
    def binomial(self):
        binomial = stats.binom(self.n,self.p)
        x=self.x.generar_numero()
        fmp = binomial.pmf(x)
        return [x,fmp]

#Distribucion normal(0,1); u=0; o=1
#f(x):   1/( sqrt(2*PI) ) * e^[x^2/2] 
class Normal_01:
    def __init__(self,x):
        self.x=x
    def normal_01(self):
        x=self.x.generar_numero()
        total_normal_01=( 1/((2*pi)**(0.5)) )*( (e)**((x**2)/2) ) #1/( sqrt(2*PI) ) * e^[x^2/2] 
        return [total_normal_01, x]

class Normal:
    def __init__(self,o,u,x):
        self.o=o #desviacion estandar
        self.u=u #Media aritmetica
        self.x=x 
    def normal(self):
        x=self.x.generar_numero()
        part1= 2*(self.o**2)#se resuelve el denomidador del expontente de e
        part2 = -1*((x-self.u)**2)#se resuelve el numeraddor del exponente de e
        part3=np.log(np.e**(part2/part1))#se despeja e, obteniendo el valor del exponente resuelto
        part4=math.sqrt(2*pi)#se resuelve la raiz
        part5 = part3/(part4 * self.o)#se resuelve la ecuacion de dsitribucion
        return [part5,x]
        
class UniCont:
    def __init__(self,limMax,limMin,x):
        self.limMax = limMax
        self.limMin = limMin
        self.x = x
    def unicont(self):
        x=self.x.generar_numero()
        if (x <= self.limMin):
            return [0,x]
        elif(self.limMax >= x):
            return [1,x]
        else:
            paso1 = x - self.limMin
            paso2 = self.limMax - self.limMin
            paso3 = paso1 / paso2
            return [paso3,x]

#Distribucion Poisson;
#f(x):   [e^(-l) * l^x]/x!
#x>=0   l -> real positivo
class Poisson:
    def __init__(self,lamda,x):
        self.x=x
        self.lamda=lamda
    def poisson(self):
        x=self.x.generar_numero_entero()
        total_possion=((e**(-self.lamda))*(self.lamda**x)) / math.factorial(x) #[(e^(-l))*(l^x)]/x!
        return [total_possion, x]

#Distribucion Geometrica
#p(x;p) = (1-p)^(x-1)*p
#r>=1 y p (0<=p<=1)
class Geometrica:
    def __init__(self,p,x):
        self.x=x
        self.p=p
    def geometrica(self):
        x=self.x.generar_numero()
        total_geometrica=( (1-self.p)**(x-1) )*self.p #(1-p)^(x-1)*p
        return [total_geometrica, x]

class Weibull:
    def __init__(self,a,l,x):
        self.a=a
        self.l=l
        self.x=x
    def weibull(self):
        x=self.x.generar_numero()
        calculo1=self.l*self.a*(self.l*x)**(self.a-1)
        calculo2=e**-(self.l*x)**self.a
        total_weibull=calculo1*calculo2
        return [total_weibull,x]

class Weibull:
    def __init__(self,a,l,x):
        self.a=a
        self.l=l
        self.x=x
    def weibull(self):
        x=self.x.generar_numero()
        calculo1=self.l*self.a*(self.l*x)**(self.a-1)
        calculo2=e**-(self.l*x)**self.a
        total_weibull=calculo1*calculo2
        return [total_weibull,x]


class Triangular:
    def __init__(self,a,b,c,x):
        self.a=a
        self.b=b
        self.c=c
        self.x=x
        # b = a < b
        # c = a <= c <= b
    def triangular(self):
        x=self.x.generar_numero_entero()
        if(x < self.a):
            total_triangular = 0
        elif(self.a<=x and self.c>x):
            calculo1 = 2*(x-self.a)
            calculo2 = (self.b-self.a)*(self.c-self.a)
            total_triangular = calculo1/calculo2
        elif(x == self.c):
            total_triangular = 2/(self.b-self.a)
        elif(self.c < x and self.b >= x):
            calculo1 = 2*(self.b-x)
            calculo2 = (self.b-self.a)*(self.b-self.c)
            total_triangular = calculo1/calculo2
        elif(self.b < x):
            total_triangular = 0
        return [total_triangular,x]