def first_last6(nums):
    if 6 in nums[0:]:
        print(True)
    elif 6 in nums[:-1]:
        print(True)
    else:
        print(False)


first_last6([13, 6, 1, 2, 3])
