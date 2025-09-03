def selection(arr, n, index):
    if index >= n - 1:
        return
    min_idx = index
    for i in range(index + 1, n):
        if arr[i] < arr[min_idx]:
            min_idx = i
    
    if min_idx != index:
        arr[index], arr[min_idx] = arr[min_idx], arr[index]

    selection(arr, n, index + 1)

arr = [6, 2, 3, 0, 1]
n = len(arr)

selection(arr, n, 0)
print(arr)