with open("1.txt") as f:
    nums = [int(i.strip("\n")) for i in f.readlines()]


deltas = [next-cur for cur, next in zip(nums, nums[1:])]
print(sum(1 for i in deltas if i > 0))
