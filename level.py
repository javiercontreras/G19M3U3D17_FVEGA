def choose_level(n_pregunta, p_level):
    if n_pregunta/p_level <= 1:
        level = 'basicas'
    elif n_pregunta/p_level <= 2:
        level = 'intermedias'
    elif n_pregunta/p_level <= 3:
        level = 'avanzadas'
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(6, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias