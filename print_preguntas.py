import preguntas as p

def print_pregunta(enunciado, alternativas):
    letras = ['A','B','C','D']
    count = 0
    print("\n"+ enunciado[0] + "\n")
    for i in alternativas:
        print(letras[count] +'. ' +i[0])
        count += 1

    # Imprimir enunciado y alternativas
    ###############################################################
    pass
    
    
    
    
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4