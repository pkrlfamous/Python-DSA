def selectionSort(nums):
    for i in range(len(nums)):
        minpos = i  # storing the index of the min element

        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:  # compare two elements
                minpos = j  # just storing the min position

        temp = nums[i]  # swapping the index i with the min position
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)  # printing num on every iteration


num = [5, 3, 8, 6, 7, 2]

selectionSort(num)

print(num)
