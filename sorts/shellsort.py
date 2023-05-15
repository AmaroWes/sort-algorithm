def shellSort(arr):
    num = len(arr)
    gap = num // 2

    while gap > 0:
        i = gap
        while i < num:
            j = i - gap
            while j >= 0:
                if arr[j+gap] > arr[j]:
                    break
                else:
                    arr[j+gap], arr[j] = arr[j], arr[j + gap]
                j -= gap
            i += 1
        gap = gap // 2
    
    return arr