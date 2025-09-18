def bubble_sort(array):
    tamanho = len(array) - 1
    for i in range(tamanho):
        breakOut = True
        for j in range(tamanho - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                breakOut = False
        
        if breakOut:
            break

    return array