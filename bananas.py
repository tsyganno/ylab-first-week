from itertools import combinations


def bananas(s):
    count_combinations = combinations(s, 6)
    d = {}
    for el in 'banana':
        count = s.count(el)
        for i in range(count):
            index_el = s.find(el)
            if el not in d:
                d[el] = [index_el]
                s = s[:index_el] + '-' + s[index_el + 1:]
            else:
                d[el].append(index_el)
                s = s[:index_el] + '-' + s[index_el + 1:]
    dataset = []
    for el in count_combinations:
        for key in d.keys():




    return count_combinations


a = bananas('bbananana')
print(a)


"""d = {}
    for el in 'banana':
        count = s.count(el)
        for i in range(count):
            index_el = s.find(el)
            if el not in d:
                d[el] = [index_el]
                s = s[:index_el] + '-' + s[index_el + 1:]
            else:
                d[el].append(index_el)
                s = s[:index_el] + '-' + s[index_el + 1:]
    print(d)"""