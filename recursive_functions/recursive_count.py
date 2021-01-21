def recursive_count(lst):
    if lst == []:
        return 0
    return 1 + recursive_count(lst[1:])


if __name__ == '__main__':
    print(recursive_count([1, 4, 2, 65, 7, 8, 9]))
    print(recursive_count([4]))
    print(recursive_count([]))
