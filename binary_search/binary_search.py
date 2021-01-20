def binary_search_iterative(item, lst):
    low = 0
    high = len(lst) - 1
    while low <= high:
        guess_idx = (low + high) // 2
        guess = lst[guess_idx]
        print('guess: ' + str(guess))
        # import pdb; pdb.set_trace()
        if item == guess:
            return guess
        elif item > guess:
            low = guess_idx + 1
        else:
            high = guess_idx - 1
    return None


def binary_search_recursive(item, lst, low, high):
    print('start---. low: {}, high: {}'.format(low, high))
    if low > high:
        return None
    guess_idx = (low + high) // 2
    guess = lst[guess_idx]
    print('guess_idx: ' + str(guess_idx))
    print('guess: ' + str(guess))
    if item == guess:
        return guess
    elif item > guess:
        low = guess_idx + 1
    else:
        high = guess_idx - 1
    print('next call---')
    return binary_search_recursive(item, lst, low, high)


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9]
    print(lst)
    #print(binary_search_iterative(7, lst))
    print(binary_search_recursive(9, lst, 0, len(lst) - 1))
