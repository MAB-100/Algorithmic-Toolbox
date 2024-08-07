def points_cover_optimized(starts, ends, points):
    events = []
    
    # Create events for each segment start and end
    for start, end in zip(starts, ends):
        events.append((start, 'L'))  # Segment start
        events.append((end + 1, 'R'))  # Segment end (exclusive)
    
    # Create events for each point query
    for point in points:
        events.append((point, 'P'))
    
    # Sort events: firstly by position, then by type ('L' -> 'P' -> 'R')
    events.sort(key=lambda x: (x[0], x[1]))
    
    active_segments = 0
    result = {}
    
    # Process events
    for pos, typ in events:
        if typ == 'L':
            active_segments += 1
        elif typ == 'R':
            active_segments -= 1
        elif typ == 'P':
            result[pos] = active_segments
    
    # Collect results in the order of original points
    return [result.get(point, 0) for point in points]

if __name__ == '__main__':
    from sys import stdin
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts = data[2:2 + n]
    input_ends = data[2 + n:2 + 2 * n]
    input_points = data[2 + 2 * n:]
    
    output_count = points_cover_optimized(input_starts, input_ends, input_points)
    print(*output_count)
