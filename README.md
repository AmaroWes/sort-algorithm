<h1 align="center">
  :computer: Sort Algorithms
</h1>
<br>

## :clipboard: Description

Project to analyze the difference between different methods of sort the groups of data and understand their complexity in a controlled environment.
This project is being developed for academic purposes, in the discipline "ALGORITMOS E ESTRUTURA DE DADOS 2" at "FACULDADE SENAC RS".

Is being tested the fallowing sort algorithms:
- bubble sort
- counting sort
- heap sort
- insertion sort
- merge sort
- quick sort
- radix sort
- selection sort
- shell sort

### explanation

Bubble Sort
* start with the first two elements, comparing them to check witch one is greater, and swapping them if it's the case, the process is repeated for the rest de array.

Counting Sort
* start by counting the number of objects having distinct key values, and calculate the position of each object in the output sequence.

Heap Sort
* start by converting the array to a binary heap, taking the last item that has children, comparing the set of numbers (3) to declare which one is greater, and swapping the position, the process is repeated for the rest of the tree and the array is reorganized based on maximum or minimum value, per configuration.

Insertion Sort
* start with the first two elements, comparing them to check which one is greater, and swapping them if it's the case, the process is repeated for the rest de array.

Merge Sort
* Think of it as a recursive algorithm continuously splits the array in half until it cannot be further divided. This means that if the array becomes empty or has only one element left, the dividing will stop, i.e. it is the base case to stop the recursion. If the array has multiple elements, split the array into halves and recursively invoke the merge sort on each of the halves. Finally, when both halves are sorted, the merge operation is applied. Merge operation is the process of taking two smaller sorted arrays and combining them to eventually make a larger one.

Quick Sort
* Start by selection a target to be the pivot, any can be selected, its done throw partitions which is recursive, so is compared to the smallest value and is swap the positions.

Radix Sort
* The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit. Radix sort uses counting sort as a subroutine to sort.

Selection Sort
* works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.

Shell Sort
* It's a variation of Insert Sort.

### Development

For development, you can use `main.py` to run the functions. Click the "run" button and `main.py` will run.

### Data Source

The data is being generated at the file dataset.py.

### Results

- 

## 💻 technologies

This project was developed with the following technologies:
- Python

This project is under the MIT license. See the [LICENSE](LICENSE.md) file for more details.

