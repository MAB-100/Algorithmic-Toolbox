from sys import stdin

def closest_smaller_number_index(sorted_list, n):
    left, right = 0, len(sorted_list) - 1
    closest = None
    closest_index = -1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] <= n:
            closest = sorted_list[mid]
            closest_index = mid
            left = mid + 1  # Move right to find if there's a closer smaller number
        else:
            right = mid - 1  # Move left
    return closest, closest_index

def check_consecutive_differences(numbers, n):
    # Iterate through the list up to the second-to-last element
    for i in range(len(numbers) - 1):
        difference = abs(numbers[i] - numbers[i + 1])
        # Check if the difference is greater than n
        if difference > n:
            return -1
    # If no difference is greater than n, return 0 (or handle as needed)
    return 0
def min_refills(distance, tank, stops):
    # write your code here
    # Add the start and end points to the stops list
    fuel_refill = tank
    refills = 0
    stops = [0] + stops + [distance]
    
    possibility = check_consecutive_differences(stops, tank)
    if possibility == -1:
        return -1
    else:
        while stops != [] and distance > tank:
            # print(stops)

            stop , index  = closest_smaller_number_index(stops, tank)
            # print(stop, index)
            tank = stop + fuel_refill
            refills += 1
            stops = stops[index + 1:]
        
        return refills  # Return the number of refills

def refills(d, m, n, stops):
 
    if stops == [] and d > m:
        return -1
       
    if d <= m:
        return 0
   
    if d - stops[-1] > m:
        return -1
   
 
    furthest_refill = 0
    prev_stop = 0
    fcount = 0
    for stop in stops:
        if stop - prev_stop > m:
            return -1
        if stop >= furthest_refill and stop <= m:
            furthest_refill = stop
            fcount = fcount + 1
        prev_stop = stop
    stops = stops[fcount:]
    d = d - furthest_refill
    stops = [stop - furthest_refill for stop in stops]
    return 1 + refills(d, m, n, stops)
 
 
 
 


import random
import time
if __name__ == '__main__':

    d, m, num_stops, *stops = map(int, stdin.read().split()) # Read the input
    print(min_refills(d, m, stops))

#    while True:
#         print("TESTING")
#         d = random.randint(1, 1000)
#         m = random.randint(1, 400)
#         num_stops = random.randint(1, 10)
#         stops = [random.randint(1, d) for _ in range(num_stops)]
#         stops.sort()

#         if refills(d, m, num_stops, stops) != min_refills(d, m, stops):
#             print("INPUT")
#             print(d, m, num_stops, *stops)    
#             print("MY OUTPUT")
#             print(min_refills(d, m, stops))
#             print("CORRECT OUTPUT")
#             print(refills(d, m, num_stops, stops))
#             break
        