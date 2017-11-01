# task 5 
x = input()
def func(x):
     a = list(x)
     lt = list('qwertyuioplkjhgfdsazxcvbnm')
     num = list('1234567890')
     lt1 = [i for i in a if i in lt]
     num1 = [i for i in a if i in num]
     ln1 = len(lt1)
     ln2 = len(num1)
     ln = len(x)
     b = ln
     if ln >= 30 and ln <= 50 :
        print('In string are %d symbols' % (ln))
        print(' %d letters and %d numbers' % (ln1, ln2))
     elif ln < 30 :
        print(' %d letters and %d numbers' % (ln1, ln2))
     elif ln > 50 :
         while b != 50 :
             a.pop()
             b -= 1
             print(' %d letters and %d numbers' % (ln1, ln2))

func(x)
