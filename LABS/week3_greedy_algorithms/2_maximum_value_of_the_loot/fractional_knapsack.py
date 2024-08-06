from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    # Sort by value per weight
    value_per_weight = [v / w for v, w in zip(values, weights)]
    sorted_items = sorted(zip(value_per_weight, values, weights), reverse=True)
    for item in sorted_items:
        if capacity == 0:
            return value
        weight = min(item[2], capacity)
        value += weight * item[0]
        capacity -= weight

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
