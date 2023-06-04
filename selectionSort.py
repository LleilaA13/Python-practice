#SELECTION SORT:

def SelectionSort(array : list) -> list:
    # your code goes here
    for i in range(len(array)):
        minIndex = i
        for j in range(i+1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        (array[i], array[minIndex]) = (array[minIndex], array[i])
    return array

if __name__ == "__main__":
    L = [55, -1, 6, 32, 29, -10, 4, 2, 7, 43, 2,5, 7, 78, 8, 8]
    sortedL = SelectionSort(L)
    print(sortedL)