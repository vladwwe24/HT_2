# task 3
a = int(input())
b = int(input())
c = int(input())
def func1(a):
   a *= a + 3
   return a

def func2(b):
    b += 5
    return b

def func3(c):
    c /= 10
    return c

def func4():
    r = float(func1(a) + func2(b) + func3(c))
    print(r)
    return r

func4()
