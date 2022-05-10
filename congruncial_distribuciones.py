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