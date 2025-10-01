def partial_selection_sort(arr, max_swaps):
  n = len(arr)
  swap_counter = 0
  for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_index]:
        min_index = j
    
    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swap_counter += 1

    if swap_counter == max_swaps:
      break
  return arr

values = [72, 12, 62, 69, 27, 67, 41, 56, 33, 74]
result = partial_selection_sort(values, 4)
print("Array after 4 swaps:", result)