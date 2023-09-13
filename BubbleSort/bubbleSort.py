'''

'''

def sort(nums):
    for i in range(len(num)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


num = [ 5,3,8,6,7,2]
sort(num)
print(num)