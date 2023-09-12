def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

num = 6
print(f'the factorial of {num} is {factorial(num)}')



'''def firstMethod():
    secondMethod()
    print("First method")


def secondMethod():
    thirdMethod()
    print("Second method")


def thirdMethod():
    fourthMethod()
    print("Third method")


def fourthMethod():
    print("Fourth method")

firstMethod()'''