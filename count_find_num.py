from itertools import combinations_with_replacement
from functools import reduce


def count_find_num(primesL, limit):
    result = set()
    for size in range(len(primesL), len(primesL) ** 3 + 1):
        count = 0
        for el in combinations_with_replacement(primesL, size):
            if all(x in el for x in primesL):
                multiplication = reduce(lambda x, y: x * y, el)
                if multiplication <= limit:
                    result.add(multiplication)
                    count += 1
        if count == 0:
            break
    if len(result) == 0:
        return []
    return [len(result), max(result)]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
