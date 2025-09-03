def shift(arr, n):
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = last

def insertion(arr, n):
    if n <= 1:
        return

    insertion(arr, n - 1)
    shift(arr, n)

arr = [6, 2, 3, 0, 1]
n = len(arr)

insertion(arr, n)
print(arr)