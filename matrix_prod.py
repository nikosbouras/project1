def matrix_prod(a, b):
    if type(a) is not list:
        raise TypeError('a must be a list')
    if type(b) is not list:
        raise TypeError('b must be a list')

    a_rows = len(a)
    a_cols = len(a[0])
    b_rows = len(b)
    b_cols = len(b[0])

    for x in a:
        if type(x) is not list:
            raise TypeError('a must be a list of lists')
        if len(x) != a_cols:
            raise ValueError('every row in a must have same length')
    for x in b:
        if type(x) is not list:
            raise TypeError('b must be a list of lists')
        if len(x) != b_cols:
            raise ValueError('every row in b must have same length')

    if a_cols != b_rows:
        raise ValueError('a rows must be as much as b columns')

    c = []

    for i in range(a_rows):
        c.append([])
        for j in range(b_cols):
            c[i].append(0)
            for k in range(a_cols):
                c[i][j] += a[i][k] * b[k][j]

    return c
