import random
def select(array, i):
    if len(array) <= 5:
        copy = array[:]
        copy.sort()
        return copy[i - 1]
    else:
        medians = []
        j = 0
        while j < len(array):
            subarray = array[j:j+5]
            medians.append(select(subarray, len(subarray) / 2))
            j += 5
        mom = medians[len(medians) / 2]
        l = []
        r = []
        for elm in array:
            if elm > mom:
                r.append(elm)
            elif elm < mom:
                l.append(elm)
        p = len(l) + 1
        if i == p:
            return mom
        elif i < p:
            return select(l, i)
        return select(r, i - p)

if __name__=='__main__':
    array = [random.randint(0, 10000) for _ in range(100)]
    array = list(set(array))
    median = select(array, len(array) / 2)
    print median
    array.sort()
    print array[(len(array) / 2) - 1]
