import debug
import random

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return array

def insertion_sort(array):
    for i in range(1 ,len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array = swap(array, j, j-1)
            j-=1
    return array

def selection_sort(array):
    for i in range(1, len(array)):
        j = i
        for k in range(i+1, len(array)):
            if (array[k] < array[j]):
                j = k
                swap(j, len(array)-1)
    return array

def main():
    x = range(0, 100)
    random.shuffle(x)

    debug.clean('x_unsorted')
    debug.clean('x_insertion_sort')

    debug.watch_list('x_unsorted', x)
    print x

    insertion_x = insertion_sort(x)
    debug.watch_list('x_insertion_sort', insertion_x)
    print insertion_x

    selection_x = selection_sort(x)
    debug.watch_list('x_selection_sort', selection_x)
    print selection_x

if __name__ == '__main__':
    main()
