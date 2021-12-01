with open("1.txt") as f:
    nums = [int(i.strip("\n")) for i in f.readlines()]


prev_sum = None
increases = 0
for prev, cur, next in zip(nums, nums[1:], nums[2:]):
    if prev_sum is not None:
        if prev+cur+next > prev_sum:
            increases += 1

    prev_sum = prev+cur+next
print(increases)