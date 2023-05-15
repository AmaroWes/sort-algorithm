def pseuCountingSort(arr, exp):
    num = len(arr)

    output = [0] * num
    count = [0] * 10

    for i in range(0, num):
        idx = arr[i] // exp
        count[idx % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = num - 1
    while i >= 0:
        idx = arr[i] // exp
        output[count[idx % 10] - 1] = arr[i]
        count[idx % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, num):
        arr[i] = output[i]

def radixSort(arr):
    max_element = max(arr)
    exp = 1

    while max_element / exp >= 1:
        pseuCountingSort(arr, exp)
        exp *= 10

    return arr