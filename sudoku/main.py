import numpy as np
import copy
import os
import json

ac = 0


def process_data(file):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file)
    with open(file_path, 'r', encoding='utf-8') as data:
        obj = json.load(data)
        arr = np.array(obj)
    return arr


def block():
    x = np.zeros((9, 9))
    j = 0
    for i in range(3):
        for a in range(i * 27, 9 + i * 27, 3):
           A1 = np.array([a, a + 1, a + 2])
           x[j] = np.array([A1, A1 + 9, A1 + 18]).flatten()
           j += 1
    return x.astype(int)


def delete_state(arr, states):
    """
    :param arr:
    :param states:
    :return:
    """
    n = len(arr)
    blocks = block()  # need check blocks
    states_last = np.zeros((81, 9))
    rows = np.array([np.arange(a, a + 9) for a in range(0, 73, 9)])
    columns = np.array([np.arange(a, a + 73, 9) for a in range(0, 9)])
    while not np.array_equal(states_last, states):
        states_last = copy.copy(states)
        for i in range(n):  # modify states
            if arr[i] != 0:
                for l in [blocks, rows, columns]:
                    result = np.where(l == i)
                    num = result[0]  # idx of square
                    for k in l[num][l[num] != i]:
                        states[k, arr[i] - 1] = 0  # find indexes of elements in same square and delete unneeded state
        for i in range(n):  # modify numbers
            if np.sum(states[i]) == 1:
                idx = np.where(states[i] == 1)
                arr[i] = idx[0] + 1
    return arr, states


def assumption(arr, states, j):  # if -> solved, else -> continue find new one. return out of circle -> without answers
    #print("t =", j)
    for i in range(9):
        if states[j, i] == 0:
            continue
        arr_try = copy.deepcopy(arr)
        states_try = copy.deepcopy(states)
        states_try[j] = np.zeros(9)
        states_try[j][i] = 1
        arr_try, states_try = csv(arr_try, states_try)
        if check_solved(arr_try):
            return arr_try, states_try
        if check_undetermined(states_try):
            global ac
            ac = 1
            return arr_try, states_try
    return arr, states


def check_solved(arr):  # add check for deleting all elements
    """
    :param arr:
    :return:
    >>> check_solved(np.array([[0, 1], [1, 1]]))
    False
    >>> check_solved(np.array([[1, 1], [1, 1]]))
    True
    """
    if np. all((arr != 0)):
        return True
    else:
        return False


def check_undetermined(states):  # exite obj with no state -> yes
    """
    :param states:
    :return:
    >>> check_undetermined(np.array([[0, 0],[0, 0]]))
    False
    >>> check_undetermined(np.array([[0, 1],[0, 0]]))
    False

    """
    unsolved = np.any(np.all((states == 0), axis=1))
    #print(unsolved)
    if np.any(sum(states.T) > 1, axis=0) and not unsolved:
        return True
    else:
        return False


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
        for j in range(len(arr)):
            if arr[j] == 0:
                arr, states = assumption(arr, states, j)  # return: have answer or doesn't have one
                break
    return arr, states


def main():
    file = '../sudoku_02.json'
    arr = process_data(file)
    arr = arr.flatten()
    states = np.ones((len(arr), 9))
    for i in range(len(arr)):
        if arr[i] != 0:
            states[i] = np.zeros(9)
            states[i, arr[i]-1] = 1
    arr, states = csv(arr, states)
    arr = np.reshape(arr, (9, 9))
    if check_solved(arr):
        print(arr)
    elif ac == 1:
        print("no polymorphism")
    else:
        print("No answer!")


if __name__ == '__main__':
    main()
