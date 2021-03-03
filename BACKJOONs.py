
import itertools


def solution(M, load):
    load.sort()
    load.reverse()
    result = list(map(sum, itertools.combinations(load, 2)))
    print(result)


solution(10, [2, 3, 8, 7, 9])
