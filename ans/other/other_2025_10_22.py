"""
[1,0,0,1] k=1 False
[1,0,0,0,1] k=1 True
"""

def test(nums, k):
    max_len = len(nums)
    count = 0
    last = None
    for en, i in enumerate(nums):
        """
        [1,0,0,1] k=1 False
        [1,0,0,0,1] k=1 True
        """
        if max_len >= en + 1:
            if i == 0 and last == 0 and nums[en + 1] == 0:
                count += 1
        last = i

    if count >= k:
        return True
    return False



if __name__ == '__main__':
    nums = [1,0,0,1]
    print(test(nums, 1))

    nums = [1,0,0,0,1]
    print(test(nums, 1))
