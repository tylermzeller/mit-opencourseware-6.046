'''
Weighted Interval Scheduling: Divide and Conquer w/ Dynamic Programming
  Define resources and requests
    1 resource, n requests (1, 2, ..., n)
  Define s(i) = start time of request i, f(i) = finish time of request i
    where s(i) < f(i)
  Two requests, i, j, are compatible if they don't overlap (f(i) <= s(j) or
    f(j) <= s(i))
  Define w(i) = the weight of request i
  Define R_j = {i | s(i) > f(j) for i != j}
  Given a set of intervals as (a, b, w) tuples, where 'a' = an integer start time,
   b = an integer finish time, and w = an integer weight, select a compatible subset of the requests/
    intervals of maximum weight.

  Divide and Conquer interval scheduling:
    WIS(1, 2, ..., n) = max{WIS(2, ..., n), w(1) + WIS(R_1)}

'''

best_schedule_weight = {}
best_schedule = {}

def find_compatible_request(intervals, request, length):
    for i in range(length):
        if intervals[i][0] >= request[1]:
            return i
    return -1

def calc_weight(schedule):
    summ = 0
    for interval in schedule:
        summ += interval[2]
    return summ

def weighted_interval_scheduling(intervals, length):
    if length == 1 or length == 0:
        return intervals

    # WIS(2, ..., n)
    schedule1 = []
    if intervals[1] in best_schedule:
        schedule1 = best_schedule[intervals[1]]
    else:
        schedule1 = weighted_interval_scheduling(intervals[1:], length - 1)
        best_schedule[intervals[1]] = schedule1

    # w(1) + WIS(R_1)
    first = intervals[0]
    if first in best_schedule:
        schedule2 = best_schedule[first]
    else:
        schedule2 = [first]
        R_j = find_compatible_request(intervals, first, length)
        if R_j > 0:
            schedule2 += weighted_interval_scheduling(intervals[R_j:], length - R_j)
        best_schedule[first] = schedule2

    if calc_weight(schedule1) > calc_weight(schedule2):
        return schedule1
    return schedule2

def schedule_intervals(intervals):
    # sort intervals by starting time
    sorted_intervals = sorted(intervals, key=lambda tup: tup[0])
    return weighted_interval_scheduling(sorted_intervals, len(sorted_intervals))


if __name__=='__main__':
    def print_results(intervals, schedule):
        print 'Input: '
        print ', '.join(str(tpl) for tpl in intervals)
        print 'Schedule:'
        print ', '.join(str(tpl) for tpl in schedule)

    intervals = [(1,3,5), (2,5,6), (4,6,5), (6,7,4), (5,8,11), (7,9,2),]

    schedule = schedule_intervals(intervals)
    print schedule
    print calc_weight(schedule)
