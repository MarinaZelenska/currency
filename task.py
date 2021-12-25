def split(values, number):
    values_size = len(values)
    if number > values_size:
        return values
    number_divide = int(values_size / number)
    remainder_of_the_division = values_size % number
    result = []
    iterator = iter(values)
    for i in range(number_divide):
        result.append([])
        for j in range(number):
            result[i].append(iterator.__next__())
        if remainder_of_the_division:
            result[i].append(iterator.__next__())
            remainder_of_the_division -= 1
    return result


assert split([1, 2, 3, 4], 2) == [
    [1, 2],
    [3, 4],
]
assert split([1, 2, 3, 4, 5, 6], 2) == [
    [1, 2],
    [3, 4],
    [5, 6],
]
assert split([1, 2, 3, 4, 5, 6], 3) == [
    [1, 2, 3],
    [4, 5, 6],
]
assert split([1, 2, 3, 4, 5], 3) == [
    [1, 2, 3],
    [4, 5],
]
assert split([1, 2, 3, 4, 5], 2) == [
    [1, 2],
    [3, 4],
    [5, ],
]
assert split([1, 2, 3, 4, 5], 10) == [
    [1, 2, 3, 4, 5],
]
