"""
ID: edward.10
LANG: PYTHON3
TASK: milk2
"""


def get_sorted_time_intervals():
    with open('milk2.in', 'r') as f:
        N = int(f.readline().strip())

        time_intervals = []
        for _ in range(N):
            line = f.readline().strip()
            time_interval = list(map(int, line.split()))
            time_intervals.append(time_interval)

    return sorted(time_intervals)


def get_longest(time_intervals):
    START, END = time_intervals[0]
    i = 0

    longest_milked = 0
    longest_no_milked = 0
    while True:
        milk_duration = END - START
        if milk_duration > longest_milked:
            longest_milked = milk_duration

        if i+1 == len(time_intervals):
            break

        start, end = time_intervals[i+1]

        if START <= start <= END and START <= end <= END:
            pass
        elif START <= start <= END and END < end:
            END = end
        else:
            milk_duration = start - END
            longest_no_milked = max(milk_duration, longest_no_milked)
            print(longest_no_milked)
            START, END = start, end

        i += 1

    return longest_milked, longest_no_milked


if __name__ == '__main__':
    sorted_time_intervals = get_sorted_time_intervals()
    sorted_time_intervals = list(sorted_time_intervals)

    longest_milked, longest_no_milked = get_longest(sorted_time_intervals)
    
    with open('milk2.out', 'w') as f:
        f.write(str(longest_milked) + ' ' + str(longest_no_milked) + '\n')
