def find_unique_triplets(nums):
    nums.sort()  # Sort the list to make it easier to avoid duplicates
    triplets = []
    n = len(nums)

    for i in range(n - 2):
        # Avoid duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])

                # Move pointers and avoid duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1  # Increase the sum
            else:
                right -= 1  # Decrease the sum

    return triplets

# Input and Output
nums = list(map(int, input("Enter the list of integers: ").split()))
result = find_unique_triplets(nums)

print("\nUnique Triplets that sum up to zero:")
print(result)

