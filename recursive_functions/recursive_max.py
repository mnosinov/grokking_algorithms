def recursive_max(lst):
    if lst == []:
        return None

    if len(lst) == 1:
        return lst[0]

    recursive_max_item = recursive_max(lst[1:])

    if lst[0] > recursive_max_item:
        return lst[0]
    else:
        return recursive_max_item


if __name__ == '__main__':
    print(recursive_max([4, 12, 3, 2, 9]))
    print(recursive_max([4]))
    print(recursive_max([]))
