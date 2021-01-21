def find_smallest(lst):
    smallest_item = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < smallest_item:
            smallest_item = lst[i]
    return smallest_item


def find_largest(lst):
    largest_item = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > largest_item:
            largest_item = lst[i]
    return largest_item


def sort_list(lst, desc_mode=False):
    sorted_list = []
    for _ in range(len(lst)):
        if not desc_mode:
            next_element = find_smallest(lst)
        else:
            next_element = find_largest(lst)
        sorted_list.append(next_element)
        lst.remove(next_element)
    return sorted_list


if __name__ == '__main__':
    lst = [9, 3, 7, 1, 8, 4, 8]
    print(sort_list(lst, desc_mode=True))
