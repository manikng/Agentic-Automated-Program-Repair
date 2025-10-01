def subsequences(a, b, k):
    if k == 0:
        return [[]]
    if k > (b - a + 1):
        return []

    ret = []
    for i in range(a, b + 1):
        if k == 1:
            ret.append([i])
        else:
            for rest in subsequences(i + 1, b, k - 1):
                ret.append([i] + rest)

    return ret


"""
Subsequences

 
Input:
    a: An int
    b: An int
    k: A positive int

Output:
    A list of all length-k ascending sequences of ints in range(a, b)

Example:
    >>> subsequences(a=1, b=5, k=3)
    [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]
"""