def heapfy(arr, num, idx):
    largest = idx
    left = (idx * 2) + 1
    right = (idx * 2) + 2

    if left < num and arr[idx] < arr[left]:
        largest = left

    if right < num and arr[largest] < arr[right]:
        largest = right

    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        heapfy(arr, num, largest)

def heapSort(arr):
    num = len(arr)

    for i in range(num // 2 - 1, -1, -1):
        heapfy(arr, num, i)

    for i in range(num - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapfy(arr, i, 0)

    return arr
