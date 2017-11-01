# task 4
x = int(input())
y = int(input())
def func(x, y):
    if x is y :
        print('x = y')
    elif x is not y :
        if x > y :
            print('x - y = ' + str(x - y))
        elif x < y :
            print('y - x = ' + str(y - x))

func(x, y)
