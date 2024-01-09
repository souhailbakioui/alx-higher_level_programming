#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements from each tuple, or use 0 for missing elements
    a1, a2 = (
        tuple_a[0] if len(tuple_a) > 0 else 0,
        tuple_a[1] if len(tuple_a) > 1 else 0,
    )
    b1, b2 = (
        tuple_b[0] if len(tuple_b) > 0 else 0,
        tuple_b[1] if len(tuple_b) > 1 else 0,
    )

    # Sum the corresponding elements
    result_tuple = (a1 + b1, a2 + b2)

    return result_tuple
