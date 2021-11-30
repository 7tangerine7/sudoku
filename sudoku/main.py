import numpy as np
import doctest
import copy


def process_data(file):
    return arr


def delete_state(arr, n, i, j):  #
    return arr


def assumption(arr, states, j):  # if -> solved, else -> continue find new one. return out of circle -> without answers
    for i in range(9):
        arr_try = copy.deepcopy(arr)
        states_try = copy.deepcopy(states)
        states_try[j] = np.zeros(9)
        states_try[j][i] = 1
        arr_try, states_try = csv(arr_try, states_try)
        if check_solved(arr):
            return arr_try, states_try
    return arr_try, states_try


def check_solved(arr):  # add check for deleting all elements
    if arr.all():
        return True
    else:
        return False


def check_undetermined(states):  # exite obj with no state -> yes
    if (~states.any(axis=1)).any():
        return False
    else:
        return True


def csv(arr, states):  # add check for deleting all elements
    """

    :param arr:
    :param states:
    :return:

    Find undetermined states. Return when answer exist or doesn't exist
    """
    arr, states = delete_state(arr, states)

    if check_undetermined(states):
        j = 0
        while j < len(arr):
            if arr[j] == 0:
                arr, states = assumption(arr, states, j)  # return or have answer or doesn't have one
                break
    return arr



def main():
    arr = process_data(file)
    arr = csv(arr)


if __name__ == '__main__':
    main()
