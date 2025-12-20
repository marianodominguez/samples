'''
Find the maximum subarray

Kadane's algorithm
reference: https://www.youtube.com/watch?v=2MmGzdiKR9Y

Time: O(n)
Space: O(1)

'''
# Example
l = [ -1, 2, 3, -4, -5, 6, 10, -10]

# Initialize variables
max_val = l[0]
max_pos = l[0]
initial=0
final=0

# Iterate through the array
for index in range(1,len(l)):
    # Update max_val
    max_val = max(l[index], max_val+l[index])
    # Update max_pos and indices
    if max_val > max_pos:
        final = index
        max_pos = max_val
    else: 
        initial=index
print("idx=", initial, final)
print("max=", max_pos)
