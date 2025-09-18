def insertion_sort_recursive(v, n = None):
    if n is None:
        n = len(v)
    
    if n <= 1:
        return
    
    insertion_sort_recursive(v, n - 1)

    x = v[n - 1]
    j = n - 2
    while j >= 0 and v[j] > x:
        v[j + 1] = v[j]
        j -= 1
    v[j + 1] = x