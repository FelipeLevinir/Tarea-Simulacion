import tkinter
import clases_distribuciones
import matplotlib.pyplot as plt

ventana = tkinter.Tk()
#ventana.geometry("1200x300")

class Ventana:
    def __init__(self,ventana):
        
        self.ventana=ventana
        self.ventana.title("Distribuciones")

        #self.boton_congruencial=tkinter.Button(self.ventana, text="Genereacion de \nnumeros", width=30, height=2, font=("Times",12), command=lambda:self.click(0))
        #self.boton_congruencial.grid(row=0,column=0)

        self.boton_exponencial=tkinter.Button(self.ventana, text="Distribución \nExponencial", width=30, height=2, font=("Times",12), command=lambda:self.click(1))
        self.boton_exponencial.grid(row=0,column=1)

        self.boton_erlang=tkinter.Button(self.ventana, text="Distribución \nErlang", width=30, height=2, font=("Times",12), command=lambda:self.click(2))
        self.boton_erlang.grid(row=0,column=2)

        self.boton_normal_01=tkinter.Button(self.ventana, text="Distribución \nNormal(0,1)", width=30, height=2, font=("Times",12), command=lambda:self.click(3))
        self.boton_normal_01.grid(row=0,column=3)

        self.boton_normal=tkinter.Button(self.ventana, text="Distribución de \nNormal", width=30, height=2, font=("Times",12), command=lambda:self.click(4))
        self.boton_normal.grid(row=1,column=0)

        self.boton_uniforme_continua=tkinter.Button(self.ventana, text="Distribución de \nUniforme Continua", width=30, height=2, font=("Times",12), command=lambda:self.click(5))
        self.boton_uniforme_continua.grid(row=1,column=1)

        self.boton_chi_cuadrado=tkinter.Button(self.ventana, text="Distribución \nChi-Cuadrado", width=30, height=2, font=("Times",12), command=lambda:self.click(6))
        self.boton_chi_cuadrado.grid(row=1,column=2)

        self.boton_t_student=tkinter.Button(self.ventana, text="Distribución \nT-Student", width=30, height=2, font=("Times",12), command=lambda:self.click(7))
        self.boton_t_student.grid(row=1,column=3)

        self.boton_pareto=tkinter.Button(self.ventana, text="Distribución \nPareto", width=30, height=2, font=("Times",12), command=lambda:self.click(8))
        self.boton_pareto.grid(row=2,column=0)

        self.boton_weibull=tkinter.Button(self.ventana, text="Distribución \nWeibull", width=30, height=2, font=("Times",12), command=lambda:self.click(9))
        self.boton_weibull.grid(row=2,column=1)

        self.boton_triangular=tkinter.Button(self.ventana, text="Distribución \nTriangular", width=30, height=2, font=("Times",12), command=lambda:self.click(10))
        self.boton_triangular.grid(row=2,column=2)

        self.boton_uniforme_discreta=tkinter.Button(self.ventana, text="Distribución de \nUniforme Discreta", width=30, height=2, font=("Times",12), command=lambda:self.click(11))
        self.boton_uniforme_discreta.grid(row=2,column=3)

        self.boton_benoulli=tkinter.Button(self.ventana, text="Distribución \nBernoulli", width=30, height=2, font=("Times",12), command=lambda:self.click(12))
        self.boton_benoulli.grid(row=3,column=0)

        self.boton_poisson=tkinter.Button(self.ventana, text="Distribución \nPoisson", width=30, height=2, font=("Times",12), command=lambda:self.click(13))
        self.boton_poisson.grid(row=3,column=1)

        self.boton_binomial=tkinter.Button(self.ventana, text="Distribución \nBinomial", width=30, height=2, font=("Times",12), command=lambda:self.click(14))
        self.boton_binomial.grid(row=3,column=2)

        self.boton_geometrica=tkinter.Button(self.ventana, text="Distribución \nGeometrica", width=30, height=2, font=("Times",12), command=lambda:self.click(15))
        self.boton_geometrica.grid(row=3,column=3)

    def click(self,opcion):
        #if(opcion==0):
        #    self.ventana_numeros()
        if(opcion==1):
            self.ventana_exponencial()
        if(opcion==2):
            self.ventana_erlang()
        if(opcion==3):
            self.ventana_normal_01()
        if(opcion==4):
            self.ventana_normal()
        if(opcion==5):
            self.ventana_uniforme_continua()
        if(opcion==6):
            self.ventana_chi_cuadrado()
        if(opcion==7):
            self.ventana_t_studet()
        if(opcion==8):
            self.ventana_pareto()
        if(opcion==9):
            self.ventana_weibull()
        if(opcion==10):
            self.ventana_triangular()
        if(opcion==11):
            self.ventana_uniforme_discreta()
        if(opcion==12):
            self.ventana_bernoulli()
        if(opcion==13):
            self.ventana_poisson()
        if(opcion==14):
            self.ventana_binominal()
        if(opcion==15):
            self.ventana_geometrica()

    #def ventana_numeros(self):
    #    ventana=tkinter.Tk()
    #    ventana_numeros=Ventana_Numeros(ventana)

    def ventana_exponencial(self):
        ventana=tkinter.Tk()
        ventana_exponencial=Ventana_Exponencial(ventana)
    
    def ventana_erlang(self):
        ventana=tkinter.Tk()
        ventana_erlang=Ventana_Erlang(ventana)

    def ventana_normal_01(self):
        ventana=tkinter.Tk()
        ventana_normal_01=Ventana_Normal_01(ventana)

    def ventana_normal(self):
        ventana=tkinter.Tk()
        ventana_normal=Ventana_Normal(ventana)

    def ventana_uniforme_continua(self):
        ventana=tkinter.Tk()
        ventana_uniforme_continua=Ventana_Uniforme_Continua(ventana)

    def ventana_chi_cuadrado(self):
        ventana=tkinter.Tk()
        ventana_chi_cuadrado=Ventana_Chi_Cuadrado(ventana)
    
    def ventana_t_studet(self):
        ventana=tkinter.Tk()
        ventana_t_studet=Ventana_T_Studet(ventana)

    def ventana_pareto(self):
        ventana=tkinter.Tk()
        ventana_pareto=Ventana_Pareto(ventana)

    def ventana_weibull(self):
        ventana=tkinter.Tk()
        ventana_weibull=Ventana_Weibull(ventana)

    def ventana_triangular(self):
        ventana=tkinter.Tk()
        ventana_triangular=Ventana_Triangular(ventana)

    def ventana_uniforme_discreta(self):
        ventana=tkinter.Tk()
        ventana_uniforme_discreta=Ventana_Uniforme_Discreta(ventana)

    def ventana_bernoulli(self):
        ventana=tkinter.Tk()
        ventana_bernoulli=Ventana_Bernoulli(ventana)
    
    def ventana_poisson(self):
        ventana=tkinter.Tk()
        ventana_poisson=Ventana_Poisson(ventana)

    def ventana_binominal(self):
        ventana=tkinter.Tk()
        ventana_binominal=Ventana_Binominal(ventana)

    def ventana_geometrica(self):
        ventana=tkinter.Tk()
        ventana_geometrica=Ventana_Geometrica(ventana)

#class Ventana_Numeros:
#    def __init__(self, ventana):
#        self.ventana=ventana
#        ventana.geometry("600x500")
#        self.ventana.title("Genereacion de numeros")
#        self.label=tkinter.Label(ventana, text="Parametros", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
#        self.label.grid(row=0, column=0, columnspan=4)

class Ventana_Exponencial:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("500x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribución \nExponencial", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################
        
        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.gamma_label=tkinter.Label(self.frame, text="Gamma: ", state="disabled", font=("Times",14))
        self.gamma_label.grid(row=0, column=0)
        self.gamma_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.gamma_input.grid(row=0, column=1)        

#############################################################################################################

        self.generar_exponencial=tkinter.Button(self.ventana, text="Generar", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_exponencial.grid(row=5,column=1,columnspan=2)

        self.label_generar_exponencial=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_generar_exponencial.grid(row=5, column=4,columnspan=4)

#############################################################################################################

    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_exponencial=clases_distribuciones.Exponencial(int(self.gamma_input.get()),self.num)

            for i in range(1000):  
                var=var_exponencial.exponencial()
                lista_x.append(var[1])
                lista_y.append(var[0])

            plt.scatter(lista_x, lista_y)
            plt.title('Distribución Exponencial')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()
##############################################################################################################  

class Ventana_Erlang:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribución \nErlang", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.k_label=tkinter.Label(self.frame, text="Constante (k): ", state="disabled", font=("Times",14))
        self.k_label.grid(row=0, column=0)
        self.k_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.k_input.grid(row=0, column=1)        

        self.mu_label=tkinter.Label(self.frame, text="Lamda: ", state="disabled", font=("Times",14))
        self.mu_label.grid(row=1, column=0)
        self.mu_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mu_input.grid(row=1, column=1)    

#############################################################################################################

        self.generar_erlang=tkinter.Button(self.ventana, text="Generar", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_erlang.grid(row=5,column=1,columnspan=2)

        self.label_generar_erlang=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_generar_erlang.grid(row=5, column=4,columnspan=4)

#############################################################################################################

    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_erlang=clases_distribuciones.Erlang(int(self.k_input.get()),int(self.mu_input.get()),self.num)

            for i in range(1000):  
                var=var_erlang.erlang()
                lista_x.append(var[1])
                lista_y.append(var[0])

            plt.scatter(lista_x,lista_y)
            plt.title('Distribución Erlang')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()

##############################################################################################################  

class Ventana_Normal_01:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nNormal(0,1)", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################
    
        #self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        #margen=10
        #self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        #self.gamma_label=tkinter.Label(self.frame, text="Gamma: ", state="disabled", font=("Times",14))
        #self.gamma_label.grid(row=0, column=0)
        #self.gamma_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        #self.gamma_input.grid(row=0, column=1)        

#############################################################################################################

        self.generar_erlang=tkinter.Button(self.ventana, text="Generar", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_erlang.grid(row=5,column=1,columnspan=2)

        self.label_generar_erlang=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_generar_erlang.grid(row=5, column=4,columnspan=4)

#############################################################################################################

    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_normal_01=clases_distribuciones.Normal_01(self.num)

            for i in range(1000):  
                var=var_normal_01.normal_01()
                lista_x.append(var[1])
                lista_y.append(var[0])

            plt.scatter(lista_x,lista_y)
            plt.title('Distribución Normal(0,1)')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()

##############################################################################################################  

class Ventana_Normal:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nNormal", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################
        #Ajustar nombres de las variables correspondiente a cada distribucion
        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.o_label=tkinter.Label(self.frame, text="Desviación estandar: ", state="disabled", font=("Times",14))
        self.o_label.grid(row=0, column=0)
        self.o_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.o_input.grid(row=0, column=1)        

        self.u_label=tkinter.Label(self.frame, text="Media aritmetica: ", state="disabled", font=("Times",14))
        self.u_label.grid(row=1, column=0)
        self.u_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.u_input.grid(row=1, column=1)    

#############################################################################################################

        self.generar_normal=tkinter.Button(self.ventana, text="Generar", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_normal.grid(row=5,column=1,columnspan=2)

        self.label_normal=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_normal.grid(row=5, column=4,columnspan=4)

#############################################################################################################
    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_normal=clases_distribuciones.Normal(int(self.o_input.get()),int(self.u_input.get()),self.num)

            for i in range(1000):  
                var=var_normal.normal()
                lista_x.append(var[1])
                lista_y.append(var[0])

            plt.scatter(lista_x,lista_y)
            plt.title('Distribución Normal')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()

class Ventana_Uniforme_Continua:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nUniforme Continua", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################
        
        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.lim_max_label=tkinter.Label(self.frame, text="Limite Maximo: ", state="disabled", font=("Times",14))
        self.lim_max_label.grid(row=0, column=0)
        self.lim_max_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.lim_max_input.grid(row=0, column=1)        

        self.lim_min_label=tkinter.Label(self.frame, text="Limite Minimo: ", state="disabled", font=("Times",14))
        self.lim_min_label.grid(row=1, column=0)
        self.lim_min_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.lim_min_input.grid(row=1, column=1)    

#############################################################################################################

        self.generar_uniforme_continua=tkinter.Button(self.ventana, text="Generar", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_uniforme_continua.grid(row=5,column=1,columnspan=2)

        self.label_uniforme_continua=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_uniforme_continua.grid(row=5, column=4,columnspan=4)

#############################################################################################################
    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_uniforme_continua=clases_distribuciones.UniCont(int(self.lim_max_input.get()),int(self.lim_min_input.get()),self.num)

            for i in range(1000):  
                var=var_uniforme_continua.unicont()
                lista_x.append(var[1])
                lista_y.append(var[0])

            plt.scatter(lista_x,lista_y)
            plt.title('Distribución Uniforme Continua')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()
##############################################################################################################   

class Ventana_Chi_Cuadrado:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nChi-Cuadrado", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)
        
        self.n_label=tkinter.Label(self.frame, text="N: ", state="disabled", font=("Times",14))
        self.n_label.grid(row=0, column=0)
        self.n_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.n_input.grid(row=0, column=1)        

        self.gamma_label=tkinter.Label(self.frame, text="Gamma: ", state="disabled", font=("Times",14))
        self.gamma_label.grid(row=2, column=0)
        self.gamma_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.gamma_input.grid(row=2, column=1)

#############################################################################################################

        self.generar_chi_cuadrado=tkinter.Button(self.ventana, text="Generar", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_chi_cuadrado.grid(row=5,column=1,columnspan=2)

        self.label_chi_cuadrado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_chi_cuadrado.grid(row=5, column=4,columnspan=4)

#############################################################################################################
    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_chi_cuadrado=clases_distribuciones.Chi_Cuadrado(int(self.n_input.get()),int(self.gamma_input.get()),self.num)

            for i in range(1000):  
                var=var_chi_cuadrado.chi_cuadrado()
                lista_x.append(var[1])
                lista_y.append(var[0])

            plt.scatter(lista_x,lista_y)
            plt.title('Distribución Chi-Cuadrado')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()
##############################################################################################################         

class Ventana_T_Studet:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nT-Student", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################
        
        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.n_label=tkinter.Label(self.frame, text="N: ", state="disabled", font=("Times",14))
        self.n_label.grid(row=0, column=0)
        self.n_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.n_input.grid(row=0, column=1)        

        self.gamma_label=tkinter.Label(self.frame, text="Gamma: ", state="disabled", font=("Times",14))
        self.gamma_label.grid(row=2, column=0)
        self.gamma_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.gamma_input.grid(row=2, column=1)
#############################################################################################################

        self.generar_t_student=tkinter.Button(self.ventana, text="Generar Grafica", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_t_student.grid(row=5,column=2,columnspan=2)

#############################################################################################################
    
    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_t_student=clases_distribuciones.T_Student(int(self.n_input.get()),int(self.gamma_input.get()),self.num)

            for i in range(1000):  
                var=var_t_student.t_student()
                lista_x.append(var[1])
                lista_y.append(var[0])

            plt.scatter(lista_x,lista_y)
            plt.title('Distribución T-Student')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()
            #print(num.generar_numero())

##############################################################################################################  

class Ventana_Pareto:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nPareto", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################
        
        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.k_label=tkinter.Label(self.frame, text="K: ", state="disabled", font=("Times",14))
        self.k_label.grid(row=0, column=0)
        self.k_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.k_input.grid(row=0, column=1)        
  
        self.alfa_label=tkinter.Label(self.frame, text="Gamma: ", state="disabled", font=("Times",14))
        self.alfa_label.grid(row=2, column=0)
        self.alfa_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.alfa_input.grid(row=2, column=1)
#############################################################################################################

        self.generar_pareto=tkinter.Button(self.ventana, text="Generar Grafica", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_pareto.grid(row=5,column=2,columnspan=2)

#############################################################################################################
    
    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_pareto=clases_distribuciones.Pareto(int(self.k_input.get()),int(self.alfa_input.get()),self.num)

            for i in range(1000):  
                var=var_pareto.pareto()
                lista_x.append(var[1])
                lista_y.append(var[0])

            plt.scatter(lista_x,lista_y)
            plt.title('Distribución Pareto')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()
            #print(num.generar_numero())

##############################################################################################################  

class Ventana_Weibull:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("800x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nWeibull", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################
        
        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.a_label=tkinter.Label(self.frame, text="Alfa: ", state="disabled", font=("Times",14))
        self.a_label.grid(row=0, column=0)
        self.a_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.a_input.grid(row=0, column=1)        

        self.l_label=tkinter.Label(self.frame, text="Lamda: ", state="disabled", font=("Times",14))
        self.l_label.grid(row=1, column=0)
        self.l_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.l_input.grid(row=1, column=1)    

#############################################################################################################

        self.generar_weibull=tkinter.Button(self.ventana, text="Generar", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_weibull.grid(row=5,column=1,columnspan=2)

        self.label_weibull=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_weibull.grid(row=5, column=4,columnspan=4)

#############################################################################################################
    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_weibull=clases_distribuciones.Weibull(int(self.a_input.get()),int(self.l_input.get()),self.num)

            for i in range(1000):  
                var=var_weibull.weibull()
                lista_x.append(var[1])
                lista_y.append(var[0])

            plt.scatter(lista_x,lista_y)
            plt.title('Distribución Weibull')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()
##############################################################################################################   

class Ventana_Triangular:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nTriangular", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################
        #Ajustar nombres de las variables correspondiente a cada distribucion
        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.a_label=tkinter.Label(self.frame, text="A: ", state="disabled", font=("Times",14))
        self.a_label.grid(row=0, column=0)
        self.a_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.a_input.grid(row=0, column=1)        

        self.b_label=tkinter.Label(self.frame, text="B: ", state="disabled", font=("Times",14))
        self.b_label.grid(row=1, column=0)
        self.b_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.b_input.grid(row=1, column=1)    

        self.c_label=tkinter.Label(self.frame, text="C: ", state="disabled", font=("Times",14))
        self.c_label.grid(row=2, column=0)
        self.c_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.c_input.grid(row=2, column=1)

#############################################################################################################

        self.generar_triangular=tkinter.Button(self.ventana, text="Generar Grafica", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_triangular.grid(row=5,column=2,columnspan=2)

#############################################################################################################
    
    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo_Entero(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_triangular=clases_distribuciones.Triangular(int(self.a_input.get()),int(self.b_input.get()),int(self.c_input.get()),self.num)

            for i in range(1000):  
                var=var_triangular.triangular()
                lista_x.append(var[1])
                lista_y.append(var[0])

            plt.scatter(lista_x,lista_y)
            plt.title('Distribución Triangular')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()
            #print(num.generar_numero())

##############################################################################################################  

class Ventana_Uniforme_Discreta:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nUniforme Discreta", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################
        #Ajustar nombres de las variables correspondiente a cada distribucion
        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.a_label=tkinter.Label(self.frame, text="A: ", state="disabled", font=("Times",14))
        self.a_label.grid(row=0, column=0)
        self.a_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.a_input.grid(row=0, column=1)        

        self.b_label=tkinter.Label(self.frame, text="B: ", state="disabled", font=("Times",14))
        self.b_label.grid(row=1, column=0)
        self.b_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.b_input.grid(row=1, column=1)    

#############################################################################################################

        self.generar_uni_discreta=tkinter.Button(self.ventana, text="Generar Grafica", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_uni_discreta.grid(row=5,column=2,columnspan=2)

#############################################################################################################
    
    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_va_discreta=clases_distribuciones.VA_discreta(int(self.a_input.get()),int(self.b_input.get()),self.num)

            for i in range(1000):  
                var=var_va_discreta.discreta()
                lista_x.append(var[1])
                lista_y.append(var[0])

            plt.scatter(lista_x,lista_y)
            plt.title('Distribución Uniforme Discreta')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()
            #print(num.generar_numero())

##############################################################################################################  

class Ventana_Bernoulli:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nBernoulli", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################
        #Ajustar nombres de las variables correspondiente a cada distribucion
        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.repeticiones_label=tkinter.Label(self.frame, text="Repeticiones: ", state="disabled", font=("Times",14))
        self.repeticiones_label.grid(row=0, column=0)
        self.repeticiones_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.repeticiones_input.grid(row=0, column=1)        

        self.p_label=tkinter.Label(self.frame, text="P: ", state="disabled", font=("Times",14))
        self.p_label.grid(row=1, column=0)
        self.p_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.p_input.grid(row=1, column=1)    

#############################################################################################################

        self.generar_pareto=tkinter.Button(self.ventana, text="Generar Grafica", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_pareto.grid(row=5,column=2,columnspan=2)

#############################################################################################################
    
    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            var_bernoulli=clases_distribuciones.Bernoulli(int(self.repeticiones_input.get()),float(self.p_input.get()),self.num)
            var=var_bernoulli.bernoulli()
            #print(var)
            x=0
            y=0
            for i in var:
                if(i==1):
                    x=x+1
                if(i==0):
                    y=y+1
            plt.title('Distribución Bernoulli')        
            plt.bar(range(2), [x,y], edgecolor='black')
            plt.xticks(range(2), [0,1])
            plt.ylim(min(x,y)-1, max(x,y)+1)
            plt.show()

##############################################################################################################  

class Ventana_Poisson:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nPoisson", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################
     
        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.lamda_label=tkinter.Label(self.frame, text="Lamda: ", state="disabled", font=("Times",14))
        self.lamda_label.grid(row=0, column=0)
        self.lamda_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.lamda_input.grid(row=0, column=1)        

#############################################################################################################

        self.generar_poisson=tkinter.Button(self.ventana, text="Generar Grafica", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_poisson.grid(row=5,column=2,columnspan=2)

#############################################################################################################
    
    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo_Entero(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_poisson=clases_distribuciones.Poisson(int(self.lamda_input.get()),self.num)

            for i in range(1000):  
                var=var_poisson.poisson()
                lista_x.append(var[1])
                lista_y.append(var[0])

            plt.scatter(lista_x,lista_y)
            plt.title('Distribución Poisson')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()
            #print(num.generar_numero())

##############################################################################################################  

class Ventana_Binominal:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nBinominal", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################
        
        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.reep_label=tkinter.Label(self.frame, text="Repeticiones: ", state="disabled", font=("Times",14))
        self.reep_label.grid(row=0, column=0)
        self.reep_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.reep_input.grid(row=0, column=1)        

        self.p_label=tkinter.Label(self.frame, text="P: ", state="disabled", font=("Times",14))
        self.p_label.grid(row=1, column=0)
        self.p_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.p_input.grid(row=1, column=1)    

#############################################################################################################

        self.generar_poisson=tkinter.Button(self.ventana, text="Generar Grafica", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_poisson.grid(row=5,column=2,columnspan=2)

#############################################################################################################
    
    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_binomial=clases_distribuciones.Binomial(int(self.reep_input.get()),float(self.p_input.get()),self.num)

            for i in range(1000):  
                var=var_binomial.binomial()
                lista_x.append(var[1])
                lista_y.append(var[0])

            #plt.scatter(,)
            plt.plot(lista_x, lista_y, '--')
            plt.vlines(lista_x, 0, lista_y, colors='b', lw=5, alpha=0.5)
            plt.title('Distribución Binomial')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()
            #print(num.generar_numero())

##############################################################################################################  

class Ventana_Geometrica:
    def __init__(self, ventana):
        self.ventana=ventana
        #ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nGeometrica", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

#############################################################################################################

        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=2, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_label=tkinter.Label(self.frame, text="Seed: ", state="disabled", font=("Times",14))
        self.seed_label.grid(row=0, column=0)
        self.seed_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_input.grid(row=0, column=1)        

        self.const_label=tkinter.Label(self.frame, text="Constante: ", state="disabled", font=("Times",14))
        self.const_label.grid(row=1, column=0)
        self.const_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.const_input.grid(row=1, column=1)    

        self.mod_label=tkinter.Label(self.frame, text="Modulo: ", state="disabled", font=("Times",14))
        self.mod_label.grid(row=2, column=0)
        self.mod_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.mod_input.grid(row=2, column=1)  

#############################################################################################################

        self.generar_numero=tkinter.Button(self.ventana, text="Generar Número", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(0))
        self.generar_numero.grid(row=3,column=1,columnspan=2)

        self.label_numero_generado=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_numero_generado.grid(row=3, column=4,columnspan=2)

#############################################################################################################
        #Ajustar nombres de las variables correspondiente a cada distribucion
        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.p_label=tkinter.Label(self.frame, text="P: ", state="disabled", font=("Times",14))
        self.p_label.grid(row=0, column=0)
        self.p_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.p_input.grid(row=0, column=1)        

#############################################################################################################

        self.generar_geometrica=tkinter.Button(self.ventana, text="Generar Grafica", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_geometrica.grid(row=5,column=2,columnspan=2)

#############################################################################################################
    
    def click(self,opc):
        if(opc==0):
            self.num = clases_distribuciones.Congruencial_Multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #self.label_numero_generado.configure(text="Generador de números creado con la semilla: "+str(self.seed_input.get()))
        
        if(opc==1):        
            lista_x=list()
            lista_y=list()

            var_geometrica=clases_distribuciones.Geometrica(float(self.p_input.get()),self.num)

            for i in range(1000):  
                var=var_geometrica.geometrica()
                lista_x.append(var[1])
                lista_y.append(var[0])

            plt.scatter(lista_x,lista_y)
            plt.title('Distribución Geometrica')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()
            #print(num.generar_numero())

##############################################################################################################   

tarea=Ventana(ventana)
ventana.mainloop()