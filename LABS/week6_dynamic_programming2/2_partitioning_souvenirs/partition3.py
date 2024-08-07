def can_partition(nums, target, subset_sums, index):
    if index == len(nums):
        # Check if all subsets have reached the target sum
        return subset_sums[0] == target and subset_sums[1] == target and subset_sums[2] == target
    
    for i in range(3):
        # Try to put the current number into subset i
        if subset_sums[i] + nums[index] <= target:
            subset_sums[i] += nums[index]
            if can_partition(nums, target, subset_sums, index + 1):
                return True
            subset_sums[i] -= nums[index]
        
        # If the subset sum is 0, it means it's the first item being placed into the subset, so no need to try other empty subsets
        if subset_sums[i] == 0:
            break

    return False

def partition3(values):
    total_sum = sum(values)
    if total_sum % 3 != 0:
        return 0
    
    target = total_sum // 3
    subset_sums = [0] * 3
    values.sort(reverse=True)  # Sorting to try larger elements first
    
    return 1 if can_partition(values, target, subset_sums, 0) else 0

if __name__ == '__main__':
    from sys import stdin
    input_data = list(map(int, stdin.read().split()))
    input_n = input_data[0]
    input_values = input_data[1:]
    assert input_n == len(input_values)
    print(partition3(input_values))
