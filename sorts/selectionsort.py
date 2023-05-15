def selectionSort(arr):
    num = len(arr)

    for i in range(num):
        mid_idx = i

        for j in range(i+1, num):
            if arr[mid_idx] > arr[j]:
                mid_idx = j

        arr[i], arr[mid_idx] = arr[mid_idx], arr[i]

    return arr