def bubble_sort(arr):
    n = len(arr) - 1
    for step in range(n):
        breakOut = True
        for i in range(n - step):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                breakOut = False
        
        if breakOut:
            break

arr = [6, 7, 9, 4, 3, 0]
bubble_sort(arr)
print(arr)
