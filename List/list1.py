from collections import Counter

def accessElements(list):
    for i in list:
        print(i)

# accessElements(list1)

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# print(list1.index(1)) # accessing the index of the value (1) i.e 1

# list1.insert(8, 2) # inserting 2 in index 8
# print(list1)

# list1.remove(2) # removes the first occurance of the 2
# print(list1)

# list1.append(9) # appends 9 at the last index of the list
# print(list1)

# list1.pop(2) # removes element at 2 index of the list
# print(list1)

list1[3] = 44  # changing the item at index 3 to 4
print(list1)

'''
del list1[2] # Deletes the item at index 2 (which is 3)
print(list1)

del list1[1:3]  # Deletes items at indices 1 and 2
print(list1)

del list1 # deletes entire list
print(list1)
'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

list2 = ['a', 'b', 'c', 'a', 'b', 'c']
list1.extend(list2)
print(list1)

count = list1.count('a')  # counts the occurance of elements
print(count)

# counts the elements in a list and stores then in key value pair
countDict = Counter(list1)
print(countDict)


'''list3 = ['class1', 'class2', 'class3', 'class4', 'class5']

def findElement(list, value):
    if value in list:
        return f'{value} at index {list.index(value)}'
    return f'{value} not in list'

print(findElement(list3, 'class4'))'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[::])
a[::1] = [10, 20, 30, 40, 50]
print(a)


numOfSub = int(input('Enter total number of subjects: '))
marks = []
totalMarks = 0

for i in range(numOfSub):
    mark = int(input(f'Enter marks obtained for sub number {i+1}: '))
    marks.append(mark)
    totalMarks += marks[i]

percentage = round((totalMarks/numOfSub*100)/100, 2)
print(f'Total percentage: {percentage}')

if percentage > 70:
    print('Good')
else:
    print('Nice try')


square = []

for i in range(1,6):
    square.append(i**2)

print(square)

# list comprehension
square = [i**2 for i in range(1,6)] # it is executed backward, first the range(1,6) and the expression i**2
print(square)