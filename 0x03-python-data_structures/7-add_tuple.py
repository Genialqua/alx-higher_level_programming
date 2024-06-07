def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements by adding (0, 0) as default values
    if len(tuple_a) < 2:
        tuple_a += (0, 0)
    if len(tuple_b) < 2:
        tuple_b += (0, 0)

    # Take only the first two elements of each tuple
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    # Add corresponding elements of both tuples
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
