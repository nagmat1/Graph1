def selection_sort(array2):
    array = array2
    for i in range(len(array)):
        index = i
        smallest = array[i]
        for j in range(i+1,len(array)):
            if array[j] < smallest:
                smallest = array[j]
                index = j
        print(smallest)
        temp = array[i]
        array[i] = smallest
        array[index] = temp
    return array


to_sort = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(selection_sort(to_sort))
