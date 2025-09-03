# Algoritmos de ordenação já são estudados há décadas e conseguem tempo de execução O(n log n) na média.
# Eles seguem a estratégia de dividir para conquistar, como o Quick Sort, que utiliza um
# pivô como referência para separar os elementos menores e maiores, ordenando cada parte recursivamente.

def quick(arr, low, high):
    if low < high:
        pivot = arr[high]
        index = low - 1

        for i in range(low, high):
            if arr[i] <= pivot:
                index += 1
                arr[index], arr[i] = arr[i], arr[index]
            
        arr[index + 1], arr[high] = arr[high], arr[index + 1]
        pvt = index + 1
        
        quick(arr, low, pvt - 1)
        quick(arr, pvt + 1, high)

arr = [6, 2, 3, 0, 1]
n = len(arr)

quick(arr, 0, n - 1)
print(arr)