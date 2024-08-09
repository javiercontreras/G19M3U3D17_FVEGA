#1Importar scripts y librerias
import os
import sys
import display as dp
import cocina as cook
import art
#2Definir constantes
masas = {"1":"Masa Tradicional","2":"Masa Delgada","3":"Masa con bordes con Queso"}
salsas = {"1":"Salsa de Tomate","2":"Salsa Alfredo", "3":"Salsa Barbecue","4":"Salsa Pesto"}
extras = {"1":"Tomate", "2":"Champiñones","3":"Aceituna","4":"Cebolla","5":"Pollo","6":"Jamón","7":"Carne", "8":"Tocino","9":"Queso"}
finish = bool(False)
tiempo_base = int(20)
extras_cliente = []
#3definir funciones de MAIN
def ux_spacio():
    (print("--------------------------------------------"))
    pass 
# detecta el OS
clear = 'cls' if sys.platform == 'win32' else 'clear'
# ejecuta la limpieza

#4 Iniciar el bucle
while not finish:
#4.1 Mostrar principales opciones
    user_f_sel = dp.showMenu()
    os.system(clear)
    match user_f_sel:
        #Armar pizza
        case 1:
            
            masa = cook.seleccionarMasa(masas)
            os.system(clear)
            salsa = cook.seleccionarSalsas(salsas)
            os.system(clear)
            extras_cliente = cook.seleccionarExtras(extras, extras_cliente)
            os.system(clear)
        #Contenido
        case 2:
            os.system(clear)
            dp.miPizzaJut(masa, salsa, extras_cliente, extras)
        #tiempo
        case 3:
            os.system(clear)
            orden_n_min = dp.tiempo_total(tiempo_base, extras_cliente)
            print(f"Su pizzaJut estara lista en {orden_n_min}")
            ux_spacio()
        case 4:
            user_select = input("Para Agregar digite \"A\" para eliminar digite \"E\" : ")
            if user_select == 'A':
                extras_cliente = cook.seleccionarExtras(extras, extras_cliente)
            elif user_select == 'E':
                extras_cliente = cook.eliminarExtras(extras,extras_cliente)
        case 5:
            finish = True
            print("Gracias por elegir PizzaJut")
            exit()
        case _ :
            print("Default")
#4.2 Cliente inicia la seleccion de ingredientes

#4.3 Se muestra seleccuib de usuarui y tiempo estimado  

#5.Opciones de Cambiar  o Agregar 