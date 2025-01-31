def list_operations(a, b):
    if type(a) is not list:
        raise TypeError('a must be a list')
    if type(b) is not list:
        raise TypeError('b must be a list')

    a_len = len(a)
    b_len = len(b)

    x_list = False
    y_list = False

    if a_len == b_len:
        x_list = [a[i] + b[i] for i in range(a_len)]
        y_list = [(a[i] * b[i]) ** 2 for i in range(a_len)]

    return {
        'sum_of_lists': x_list,
        'prod_of_lists': y_list,
        'length_of_list_A': a_len,
        'length_of_list_B': b_len
    }
