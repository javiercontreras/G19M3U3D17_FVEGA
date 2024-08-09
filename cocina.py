import main as m

def seleccionarMasa(masas):
    for k,v in masas.items():
        print(f"Selecciones ({k}), para {v} ")
    tipo_masa = str(input("Su opcion es : "))
    return masas[tipo_masa]
    
def seleccionarSalsas(salsas):
    for k,v in salsas.items():
        print(f"Selecciones ({k}), para {v} ")
    tipo_salsa = str(input("Su opcion es : "))
    return salsas[tipo_salsa]

def seleccionarExtras(extras,extras_user):
    extras_cliente = extras_user
    extrasON = True
    print("Desea agregar ingredientes Extras??, para finalizar digite 0 ")
    for k,v in extras.items():
        print(f"Seleccione ({k}), para {v} ")
    print(f"Seleccione (0), para Finalizar ")
    while extrasON:
        try:
            x = int(input("Agregar a mi pizza : "))
        except ValueError:
            m.ux_spacio()
            print("Por favor ingrese una opcion valida")
            x = 0
        if (x == 0):
            extrasON = False
            break

        extras_cliente.append(x)
    return extras_cliente

def eliminarExtras(extras_pizzaJut, extras_user):
    eliminar = True
    print("Para eliminar un ingrediente Extra, digite el numero del extra, digite 0 para finalizar ")
    for i in extras_user:
        print(f"Opcion {i} Extra {extras_pizzaJut[str(i)]}")
    while eliminar:
        if(len(extras_user)==0):
            eliminar = False
        else:
            x = input("Su opcion es : ")
            if(x == 0 or x > ()):
                eliminar = False
                break
            else:
                extras_user.remove(int(x))
                print(extras_user)
            
    return extras_user