pracky = [4, 9, 2, 0, 5, 8, 11, 33, 4, 77, 1, 88, 26, 7]


def linSrch(haystack, needle):
    for ant in haystack:
        if ant == needle:
            return haystack.index(ant)
        elif haystack.index(ant) == len(haystack) - 1:
            return -1
        else:
            continue


# print(linSrch(pracky, 55))


def bubSort(haystack):
    swap = True
    antcage = 0
    while swap == True:
        swap = False
        for index, ant in enumerate(haystack):
            # print(ant, index)
            print(haystack)
            if index == len(haystack) -1:
                continue
            elif ant > haystack[index + 1]:
                swap = True
                antcage = ant
                haystack[index] = haystack[index + 1]
                haystack[index + 1] = antcage
            else:
                continue
    return haystack


print(bubSort(pracky))





