# task 2
def func(x , y = 'qwerty'):
    result = y
    if result is not func.__defaults__[0]:
        result = x ** y
        return result
func(1, 4)
