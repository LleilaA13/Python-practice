# BUBBLE SORT:

def BubbleSort(array: list) -> list:
    # your code goes here
    swapped = False
    for i in range(len(array)-1):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]
        if not swapped:
            return
    return array


if __name__ == "__main__":
    L = [55, -1, 6, 32, 29, -10, 4, 2, 7, 43, 2, 5, 7, 78, 8, 8]
    sortedL = BubbleSort(L)
    print(sortedL)
