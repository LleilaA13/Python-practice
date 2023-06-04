
def InsertionSort(array : list) -> list:
    # your code goes here
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

if __name__ == "__main__":
    L = [55, -1, 6, 32, 29, -10, 4, 2, 7, 43, 2,5, 7, 78, 8, 8]
    sortedL = InsertionSort(L)
    print(sortedL)