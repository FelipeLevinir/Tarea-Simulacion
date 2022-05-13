import opcode
import tkinter
import congruncial_distribuciones

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

        self.boton_benoulli=tkinter.Button(self.ventana, text="Distribución \nBenoulli", width=30, height=2, font=("Times",12), command=lambda:self.click(12))
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
        #Ajustar nombres de las variables correspondiente a cada distribucion
        self.frame=tkinter.Frame(ventana,borderwidth=5, relief="sunken")
        margen=10
        self.frame.grid(row=4, column=0, columnspan=11, ipadx=margen, ipady=margen, padx=margen, pady=margen)

        self.seed_labelx=tkinter.Label(self.frame, text="Parametro 1: ", state="disabled", font=("Times",14))
        self.seed_labelx.grid(row=0, column=0)
        self.seed_inputx=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_inputx.grid(row=0, column=1)        

        self.seed_labely=tkinter.Label(self.frame, text="Parametro 2: ", state="disabled", font=("Times",14))
        self.seed_labely.grid(row=1, column=0)
        self.seed_inputy=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_inputy.grid(row=1, column=1)    

        self.seed_labelz=tkinter.Label(self.frame, text="Parametro 3: ", state="disabled", font=("Times",14))
        self.seed_labelz.grid(row=2, column=0)
        self.seed_inputz=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.seed_inputz.grid(row=2, column=1)

    def click(self,opc):
        if(opc==0):
            num = congruncial_distribuciones.congruncial_multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            self.label_numero_generado.configure(text="Numero generado:"+str(num))


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

        self.lamda_label=tkinter.Label(self.frame, text="Lamda: ", state="disabled", font=("Times",14))
        self.lamda_label.grid(row=1, column=0)
        self.lamda_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.lamda_input.grid(row=1, column=1)    

        self.reep_label=tkinter.Label(self.frame, text="Repeticiones: ", state="disabled", font=("Times",14))
        self.reep_label.grid(row=2, column=0)
        self.reep_input=tkinter.Spinbox(self.frame, from_=0 , to=999, increment=1)
        self.reep_input.grid(row=2, column=1)

#############################################################################################################

        self.generar_erlang=tkinter.Button(self.ventana, text="Generar", width=22, height=2, anchor="center", font=("Times",9), command=lambda:self.click(1))
        self.generar_erlang.grid(row=5,column=1,columnspan=2)

        self.label_generar_erlang=tkinter.Label(ventana, text="", state="disabled", width=30, height=2, foreground="black", font=("Times",16), anchor="w")
        self.label_generar_erlang.grid(row=5, column=4,columnspan=4)

#############################################################################################################

    def click(self,opc):
        if(opc==0):
            num = congruncial_distribuciones.congruncial_multiplicativo(int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            self.label_numero_generado.configure(text="Numero generado:"+str(num))
        if(opc==1):
            earlang = congruncial_distribuciones.erlang(int(self.k_input.get()),int(self.lamda_input.get()),int(self.reep_input.get()),int(self.seed_input.get()),int(self.const_input.get()),int(self.mod_input.get()))
            #Graficar!
            self.label_generar_erlang.configure(text="Numero generado:"+str(earlang))

##############################################################################################################  

class Ventana_Normal_01:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nNormal(0,1)", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

class Ventana_Normal:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nNormal", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

class Ventana_Uniforme_Continua:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nUniforme Continua", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)


class Ventana_Chi_Cuadrado:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nChi-Cuadrado", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

class Ventana_T_Studet:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nT-Student", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

class Ventana_Pareto:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nPareto", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

class Ventana_Weibull:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nWeibull", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

class Ventana_Triangular:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nTriangular", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

class Ventana_Uniforme_Discreta:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nUniforme Discreta", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

class Ventana_Bernoulli:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nBernoulli", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

class Ventana_Poisson:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nPoisson", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

class Ventana_Binominal:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nBinominal", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

class Ventana_Geometrica:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.geometry("600x500")
        self.ventana.title("Genereacion de numeros")
        self.label=tkinter.Label(ventana, text="Parametros Distribucion \nGeometrica", state="disabled", width=30, height=2, foreground="black", font=("Times",20), anchor="center")
        self.label.grid(row=0, column=0, columnspan=4)

tarea=Ventana(ventana)
ventana.mainloop()