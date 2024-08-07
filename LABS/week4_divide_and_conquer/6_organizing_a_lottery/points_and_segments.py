def count_segments_containing_points(segments, points):
    # Create events for segments and points
    events = []
    for start, end in segments:
        events.append((start, 'L'))
        events.append((end, 'R'))
    for point in points:
        events.append((point, 'P'))
 
    # Sort events. If two events have the same coordinate, 'L' comes before 'P' and 'P' comes before 'R'
    events.sort(key=lambda x: (x[0], x[1]))
 
    segment_count = 0
    point_count = {}
    for point in points:
        point_count[point] = 0
 
    for event in events:
        if event[1] == 'L':
            segment_count += 1
        elif event[1] == 'R':
            segment_count -= 1
        else:
            point_count[event[0]] = segment_count
 
    # Return the results in the original order of points
    return [point_count[point] for point in points]
 
# Input reading
n, m = map(int, input().split())
S = []
for _ in range(n):
    s = list(map(int, input().split()))
    S.append(s)
P = list(map(int, input().split()))
 
# Applying the function
result = count_segments_containing_points(S, P)
print(*result)