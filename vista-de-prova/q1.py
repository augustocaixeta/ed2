def verifica(lista):
    n = len(lista)
    for i in range(1, n):
        if lista[i - 1] > lista[i]:
            return False

    return True