import math
import numpy as np
import mpmath

def congruncial_multiplicativo(seed, const, mod):
	num=0 
	num2=0.0
	for i in range(1,21):
		num = (const*seed)%mod #Aplicacion de la formula
		num2 = float(num)/float(mod-1) # Operación para obtener el valor en el rango de 0 a 1
		#print(i,num,round(num2,4))
		seed = num # Se utilizará el número entero obtenido como semilla de la siguiente operación.
	return num

#print(congruncial_multiplicativo(5,5,32))

def erlang(k,lamda,rep,seed,const,mod):
    cordenada=list()
    for i in range(rep):
        suma=0
        for j in range(1,k):
            var=-1*(k*lamda)
            num=np.log(congruncial_multiplicativo(seed,const,mod))
            suma=suma+(var*num)
        cordenada.append(suma)
    return cordenada

def chi_cuadrado(seed, const, mod, rep, k):
    var=list()
    for i in range(rep):
        num_gen=congruncial_multiplicativo(seed, const, mod)
        cal1=mpmath.gamma(k/2)
        cal2=mpmath.gammainc(k/2,num_gen/2)
        aux=(cal1-cal2)/cal1
        var.append([aux,num_gen])
    var = sorted(var, key=lambda num : num[1])
    return var

def tstudent(seed, const, mod, rep, k):
    var=list()
    for i in range(rep):
        num_gen=congruncial_multiplicativo(seed, const, mod)
        cal1=mpmath.gamma((k+1)/2)
        cal2=(k*3.14)**0.5
        cal3=mpmath.gamma(k/2)
        cal4=1+(((num_gen**2)/k))
        cal5=(-1*((k+1)/2))
        aux=cal1/(cal2*cal3)
        aux=aux*(cal4**cal5)
        var.append([aux,num_gen])
    var = sorted(var, key=lambda num : num[1])
    return var

def pareto(lim_inferior,lim_superior,seed, const, mod,repeticiones,a,b):
    U = list()
    X = list()
    for i in range(repeticiones):
        U.append(congruncial_multiplicativo(seed, const, mod))
    for j in range(len(U)):
        X.append(b*U[j]**(-1/a))
    x=np.arange(lim_inferior,lim_superior,0.1)
    y=list()
    for i in x:
        cont=0
        for j in X:
            if(j<i):
                cont=cont+1
        cont=cont/repeticiones
        y.append(cont)
    y=np.array(y)
    return [x,y]