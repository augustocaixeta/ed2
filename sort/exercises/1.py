def is_arr_sorted(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

arr = [1, 2, 3, 4, 5]
print(is_arr_sorted(arr))