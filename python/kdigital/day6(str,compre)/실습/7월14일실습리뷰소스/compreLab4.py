import random
nums = [random.randint(0,100) for _ in range(10)]
print(nums)

check_pass = {i+1 : 'pass' if nums[i] >= 60 else 'nopass' for i in range(10)}
print(check_pass)