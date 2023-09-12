def linearSearch(list, search):
    found = False
    for i in list:
        if search == i:
            print(search, "found at index", list.index(i))
            found = True
    if not found:
        print(search, 'not found')

list = [1,2,3,4,5]
linearSearch(list, 6)