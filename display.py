
def showMenu():
    print("Seleccion una de las siguientes opciones : ")
    print("Arma tu Pizza Jat                (1)")
    print("Que tiene mi pizzaJat??          (2)")
    print("Cuanto tiempo tomara mi pizzaJat (3)")
    print("Agregar/eliminar ingredientes    (4)")
    print("Realizar la orden                (5)")
    try:
        x = int(input("Su opcion es : "))
    except ValueError:
        print("\n---------------------------------\nPor favor ingrese una opcion valida")
        x = 0
    return x

def dictSelect(dictionary):
    for k,v in dictionary.items():
        print(f"Seleccion {v} para {k}")
    pass

def miPizzaJut(masa, salsa, extras_user, extras):
    print("Tu pizza tiene :")
    print(f"Como base, un rica {masa}")
    print(f"Sobre ella, una  {salsa}")
    for i in extras_user:
        print(f"Extra {extras[str(i)]}")
    print("--------------------------------------------")
    pass

def tiempo_total(tiempo_base, extras_cliente):
    return str(tiempo_base + (len(extras_cliente) *2)) + " minutos"