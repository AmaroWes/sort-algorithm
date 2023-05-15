def bubbleSort(arr):
    num = len(arr)
    for i in range(num):
        swapp = False

        for j in range(0, num-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapp = True

        if swapp == False:
            break

    return arr
