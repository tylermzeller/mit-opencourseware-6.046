'''
Interval Scheduling: Greedy Algorithms
  Define resources and requests
    1 resource, n requests (1, 2, ..., n)
  Define s(i) = start time of request i, f(i) = finish time of request i
    where s(i) < f(i)
  Two requests, i, j, are compatible if they don't overlap (f(i) <= s(j) or
    f(j) <= s(i))

  Given a set of intervals as (a, b) tuples, where 'a' = an integer start time and
    and b = an integer finish time, select a compatible subset of the requests/
    intervals of maximum size.

  Greedy interval scheduling pseudocode:
    1. Use a "simple" rule to select a request, i
    2. Reject all requests that are incompatible with i
    3. Repeat Step 1 until all requests are processed

  Our rule: Earliest finish time (pick the minimum f(i) of all requests)

'''

def get_earliest_finish(intervals):
    earliest = None
    for interval in intervals:
        if earliest == None:
            earliest = interval
        elif interval[1] < earliest[1]:
            earliest = interval
    return earliest

def filter_earlier_intervals(intervals, request):
    return filter(lambda x: x[0] >= request[1], intervals)

def filter_incompatible_intervals(intervals, request):
    return filter_earlier_intervals(intervals, request)

def select_request(intervals):
    return get_earliest_finish(intervals)

def schedule_intervals(intervals):
    schedule = []
    compatible_intervals = intervals[:]
    while len(compatible_intervals) > 0:
        # Step 1: Use simple rule to select a request
        selected_request = select_request(compatible_intervals)
        schedule.append(selected_request)
        # Step 2: Reject all requests that are incompatible with i
        compatible_intervals = filter_incompatible_intervals(compatible_intervals, selected_request)
        # Step 3: Repeat until all requests are processed
    return schedule


if __name__=='__main__':
    def print_results(intervals, schedule):
        print 'Input: '
        print ', '.join(str(tpl) for tpl in intervals)
        print 'Schedule:'
        print ', '.join(str(tpl) for tpl in schedule)

    intervals = [(1,2), (2,4), (3, 7), (3, 5), (2, 5), (1, 3), (4, 10)]

    schedule = schedule_intervals(intervals)
    print schedule
