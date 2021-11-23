def substring(str):
    print(str[:len(str)//2])
    return str[:len(str)//2]

print(substring("qwertykeyboards"))

def reverse(nums):
    start = 0
    end = len(nums)-1
    while end> start:
        nums[start],nums[end] = nums[end],nums[start]
        start = start + 1
        end = end - 1