import numpy as np
import doctest
import copy


def process_data(file):
    return arr


def delete_state(arr, n, i, j):  #
    return arr


def assumption(arr, k):
    arr = copy.deepcopy(arr)
    return arr


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

    if check_solved(arr):
        return arr

    elif check_undetermined(states):
        j = 0
        while j < len(arr):
            if arr[j] == 0:
                #arr_try = copy.deepcopy(arr)
                #states_try = copy.deepcopy(states_try) this operation in assumption
                arr, states = assumption(arr, states, j)  # return or have answer or doesn't have one
                #arr_try, states_try = csv(arr_try, states_try)  # return right answers or answer doesn't exist
                break
    return arr



def main():
    arr = process_data(file)
    arr = csv(arr)


if __name__ == '__main__':
    main()
