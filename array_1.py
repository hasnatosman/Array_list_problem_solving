"""
Problem: Write a program to reverse an array or string or list

let, L is a list
start = 0, end = n -1 index


"""


def reverse_list(L, start, end):
    while start < end:
        L[start], L[end] = L[end], L[start]
        start = start + 1
        end = end - 1


if __name__ == '__main__':
    L = [1, 2, 3, 4, 5]
    print('Inputted list: ', L)
    reverse_list(L, 0, 4)
    print('Reversed list: ', L)
    expected_result = [5, 4, 3, 2, 1]

    if L == expected_result:
        print('Passed!!')
    else:
        print('Failed!!')

