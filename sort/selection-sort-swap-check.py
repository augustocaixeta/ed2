def shift(arr, start, n):
    smallest_idx = start

    for i in range(start + 1, n):
        if arr[i] < arr[smallest_idx]:
            smallest_idx = i

    if smallest_idx != start:
        arr[start], arr[smallest_idx] = arr[smallest_idx], arr[start]

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        shift(arr, i, n)

arr = [6, 7, 9, 4, 3, 0]
selection_sort(arr)
print(arr)
