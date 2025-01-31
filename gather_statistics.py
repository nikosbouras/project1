import math


def gather_statistics(x, y):
    if type(x) is not list:
        raise TypeError('x must be a list')
    if type(y) is not list:
        raise TypeError('y must be a list')
    if len(x) != len(y):
        raise ValueError('x and y must have same length')

    x_mean = sum(x) / len(x)
    x_variance = sum([(element - x_mean) ** 2 for element in x]) / (len(x) - 1)
    x_std = math.sqrt(x_variance)

    y_mean = sum(y) / len(y)
    y_variance = sum([(element - y_mean) ** 2 for element in y]) / (len(y) - 1)
    y_std = math.sqrt(y_variance)

    covariance_x_y = sum([(x[i] - x_mean) * (y[i] - y_mean) for i in range(len(x))]) / len(x)

    return {
        'basic_statistics_X': {
            'mean': x_mean,
            'variance': x_variance,
            'std': x_std,
        },
        'basic_statistics_Y': {
            'mean': y_mean,
            'variance': y_variance,
            'std': y_std,
        },
        'covariance_X_Y': covariance_x_y
    }
