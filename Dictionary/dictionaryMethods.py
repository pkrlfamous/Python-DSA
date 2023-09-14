my_dict = {
    'Nepal': 'Kathmandu',
    'USA': 'Washington D.C',
    'Italy': 'Rome',
    'Japan': 'Tokyo'
}

'''Printing dictionary'''
print(my_dict)
print(len(my_dict))


'''Sort the dictionary by keys, don't forget to use dict() to convert the list of tuples retuned to dictionary'''
a = dict(sorted(my_dict.items()))
print(a)


'''Invalid dict, dict key should be immutable like, tuples, strings, integers, etc'''
'''my_dict = {
  1: "Hello", 
  [1, 2]: "Hello Hi", 
}'''


'''Accessing dictionary items by placing dict key inside square brackets'''
print(my_dict['Nepal'])
print(my_dict['Italy'])


'''get method to get the value by passing key'''
print(my_dict.get('Nepal'))
print(my_dict.get('USA'))


'''Changing the value of key'''
my_dict['Italy'] = 'Rome1'
print(my_dict)


'''Add an item to dict, to add multiple items use update() method'''
my_dict['Germany'] = 'Berlin'
print(my_dict)


'''The update() method updates the dictionary with the elements from another dictionary object'''
d1 = {'New Zealand': 'Wellington'}
my_dict.update(d1)  # OR my_dict.update({'New Zealand': 'Wellington'})
print(my_dict)


'''del Remove Dictionary Items'''
del my_dict['New Zealand']
print(my_dict)

keys_to_delete = ['Japan', 'German']

for item in keys_to_delete:
    try:
        del my_dict[item]
    except KeyError as e:
        print('Key not found', e)

print(my_dict)


'''items() method to get dictionary item'''
print(my_dict.items())

'''dict.key()'''
print(my_dict.keys())

'''dict.values()'''
print(my_dict.values())


for key, value in my_dict.items():
    # print(dict([(key, value)]))
    print({key:value})


'''popitem() Returns the latest inserted element (key,value) pair from the dictionary.'''
a = my_dict.popitem()
print(a)
print(my_dict)

'''The pop() method removes and returns an element from a dictionary having the given key.'''
a = my_dict.pop('Italy')
print(a)
print(my_dict)

'''Checking element in dictionary'''
print('Nepal' in my_dict)
print('Nepal' not in my_dict)
print('Singapore' in my_dict)


'''dictionary comprehsion'''
my_dict = {i: i*i for i in range(1,11)}
print(my_dict)

# item price in dollar
my_dict = {'milk': 1.2, 'tomato': 0.4, 'apple': 5}
dollar_to_pound = 0.76
print({key:value*dollar_to_pound for (key, value) in my_dict.items()}) # converting dollar to pound


# condition in dict comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_dict = {key:value for (key, value) in original_dict.items() if value % 2 == 0 }
print(even_dict)


# multiple condition in dict comprehension
new_dict = {key:value for(key,value) in original_dict.items() if value % 2 == 0 if value < 40}
print(new_dict)


# else condition in dict comprehension
new_dict = {key: ('old' if value > 40 else 'young')
            for(key,value) in original_dict.items()}
print(new_dict)


# nested dictionary comprehension
dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary)



dictionary = dict()
for k1 in range(11, 16):
    dictionary[k1] = {k2: k1*k2 for k2 in range(1, 6)}
print(dictionary)


dictionary = dict()
for k1 in range(11, 16):
    dictionary[k1] = dict()
    for k2 in range(1, 6):
        dictionary[k1][k2] = k1*k2
print(dictionary)