

class BinarySearch:

    def binarySearch(self, iterator, find):
        iterator.sort()
        l = 0
        h = len(iterator)-1
        while l <= h:
            m = (l + h)//2
            print('m',m)
            if find == iterator[m]:
                return True
            else:
                if find > iterator[m]:
                    l = m+1
                    m = (l+h)//2
                else:
                    h = m-1
                    m = (l+h)//2
        return False


list = [1,2,4,3,5,6,10]
num = 11
bs = BinarySearch()

result = bs.binarySearch(list, num)

if result:
    print(f'{num} in list')
else:
    print(f'{num} not in list')