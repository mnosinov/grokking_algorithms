def quick_sort(lst):
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    less_items = [i for i in lst[1:] if i <= pivot]
    larger_items = [i for i in lst[1:] if i > pivot]
    return quick_sort(less_items) + [pivot] + quick_sort(larger_items)


if __name__ == '__main__':
    print(quick_sort([5, 2, 8, 9, 0, 1, 67, 3, 2]))
    print(quick_sort([23]))
    print(quick_sort([]))
