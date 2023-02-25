queries = [3, 2, 1, 2, 6]

output = 17

def minimumWaitingTime(queries):
    # Sorting in ascending order ensures that we calculate the minimum.
    queries.sort()
    total_waiting_time = 0
    prev_time = 0
    for time in queries:
        print(total_waiting_time)
        total_waiting_time += prev_time
        prev_time += time
    return total_waiting_time


print(minimumWaitingTime(queries))