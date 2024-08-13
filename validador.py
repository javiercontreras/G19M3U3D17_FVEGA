
def validate(opciones, eleccion):
    # validación de eleccion
    flag = True
    while flag:
        for i in opciones:
            if i in eleccion:
                eleccion = i
                flag = False
        if flag == True:
            eleccion = input('Opción no válida, ingrese una de las opciones válidas: ')
         
    return eleccion

if __name__ == '__main__':
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    x = validate(numeros, eleccion)
    print(x)
    
