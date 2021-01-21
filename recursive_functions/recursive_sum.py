def recursive_list_sum(lst):
    if lst == []:
        return 0
    return lst[0] + recursive_list_sum(lst[1:])


if __name__ == '__main__':
    print(recursive_list_sum([2, 6, 1, 0, 7]))
    print(recursive_list_sum([8]))
    print(recursive_list_sum([]))
