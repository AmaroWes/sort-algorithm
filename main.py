from sorts.heapsort import heapSort
from sorts.bubblesort import bubbleSort
from sorts.countingsort import countingSort
from sorts.insertsort import insertSort
from sorts.mergesort import mergeSort
from sorts.quicksort import quickSort
from sorts.radixsort import radixSort
from sorts.selectionsort import selectionSort
from sorts.shellsort import shellSort

from dataset import dataset0, dataset1, dataset2
from dataset import dataset3, dataset4, dataset5

from time import time


if __name__ == "__main__":
    tempHeapSort = list()
    tempBubbleSort = list()
    tempCountingSort = list()
    tempInsertSort = list()
    tempMergeSort = list()

    # Heap Sort
    tempStartHeapSort = time()
    heapSort(dataset1)
    tempStopHeapSort = time()
    tempHeapSort.append(tempStopHeapSort - tempStartHeapSort)

    tempStartHeapSort = time()
    heapSort(dataset2)
    tempStopHeapSort = time()
    tempHeapSort.append(tempStopHeapSort - tempStartHeapSort)

    tempStartHeapSort = time()
    heapSort(dataset3)
    tempStopHeapSort = time()
    tempHeapSort.append(tempStopHeapSort - tempStartHeapSort)

    tempStartHeapSort = time()
    heapSort(dataset4)
    tempStopHeapSort = time()
    tempHeapSort.append(tempStopHeapSort - tempStartHeapSort)

    tempStartHeapSort = time()
    heapSort(dataset5)
    tempStopHeapSort = time()
    tempHeapSort.append(tempStopHeapSort - tempStartHeapSort)

    #Bubble Sort
    tempStartBubbleSort = time()
    bubbleSort(dataset1)
    tempStopBubbleSort = time()
    tempBubbleSort.append(tempStopBubbleSort - tempStartBubbleSort)

    tempStartBubbleSort = time()
    bubbleSort(dataset2)
    tempStopBubbleSort = time()
    tempBubbleSort.append(tempStopBubbleSort - tempStartBubbleSort)

    tempStartBubbleSort = time()
    bubbleSort(dataset3)
    tempStopBubbleSort = time()
    tempBubbleSort.append(tempStopBubbleSort - tempStartBubbleSort)

    tempStartBubbleSort = time()
    bubbleSort(dataset4)
    tempStopBubbleSort = time()
    tempBubbleSort.append(tempStopBubbleSort - tempStartBubbleSort)

    tempStartBubbleSort = time()
    bubbleSort(dataset5)
    tempStopBubbleSort = time()
    tempBubbleSort.append(tempStopBubbleSort - tempStartBubbleSort)

    # Counting Sort
    tempStartCountingSort = time()
    countingSort(dataset1)
    tempStopCountingSort = time()
    tempCountingSort.append(tempStopCountingSort - tempStartCountingSort)

    tempStartCountingSort = time()
    countingSort(dataset2)
    tempStopCountingSort = time()
    tempCountingSort.append(tempStopCountingSort - tempStartCountingSort)

    tempStartCountingSort = time()
    countingSort(dataset3)
    tempStopCountingSort = time()
    tempCountingSort.append(tempStopCountingSort - tempStartCountingSort)

    tempStartCountingSort = time()
    countingSort(dataset4)
    tempStopCountingSort = time()
    tempCountingSort.append(tempStopCountingSort - tempStartCountingSort)

    tempStartCountingSort = time()
    countingSort(dataset5)
    tempStopCountingSort = time()
    tempCountingSort.append(tempStopCountingSort - tempStartCountingSort)

    # Insert Sort
    tempStartInsertSort = time()
    insertSort(dataset1)
    tempStopInsertSort = time()
    tempInsertSort.append(tempStopInsertSort - tempStartInsertSort)

    tempStartInsertSort = time()
    insertSort(dataset2)
    tempStopInsertSort = time()
    tempInsertSort.append(tempStopInsertSort - tempStartInsertSort)

    tempStartInsertSort = time()
    insertSort(dataset3)
    tempStopInsertSort = time()
    tempInsertSort.append(tempStopInsertSort - tempStartInsertSort)

    tempStartInsertSort = time()
    insertSort(dataset4)
    tempStopInsertSort = time()
    tempInsertSort.append(tempStopInsertSort - tempStartInsertSort)

    tempStartInsertSort = time()
    insertSort(dataset5)
    tempStopInsertSort = time()
    tempInsertSort.append(tempStopInsertSort - tempStartInsertSort)

    # Merge Sort
    tempStartMergeSort = time()
    mergeSort(dataset1)
    tempStopMergeSort = time()
    tempMergeSort.append(tempStopMergeSort - tempStartMergeSort)

    tempStartMergeSort = time()
    mergeSort(dataset2)
    tempStopMergeSort = time()
    tempMergeSort.append(tempStopMergeSort - tempStartMergeSort)

    tempStartMergeSort = time()
    mergeSort(dataset3)
    tempStopMergeSort = time()
    tempMergeSort.append(tempStopMergeSort - tempStartMergeSort)

    tempStartMergeSort = time()
    mergeSort(dataset4)
    tempStopMergeSort = time()
    tempMergeSort.append(tempStopMergeSort - tempStartMergeSort)

    tempStartMergeSort = time()
    mergeSort(dataset5)
    tempStopMergeSort = time()
    tempMergeSort.append(tempStopMergeSort - tempStartMergeSort)

    for i in range(5):
        print(f"Heap Sort {i+1}: {tempHeapSort[i]}")
        print(f"Bubble Sort {i+1}: {tempBubbleSort[i]}")
        print(f"Insert Sort {i+1}: {tempInsertSort[i]}")
        print(f"Counting Sort {i+1}: {tempCountingSort[i]}")
        print(f"Merge Sort {i+1}: {tempMergeSort[i]}")
        print(f"\n")