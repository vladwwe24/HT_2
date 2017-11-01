# task 6 calculator
x = int(input('Enter a first number'))
y = int(input('Enter a last number'))
op = input('Enter an operation')
def calc(x, y, op):
     if op in ('+', '-', '*', '/'):
         if op == '+':
             print(x + y)
         elif op == '-':
             print(x - y)
         elif op == '*':
             print(x * y)
         elif op == '/':
             if y != 0 :
                 print(x / y)
             else:
                 print ('Division by zero')
     else:
         print('Error: wrong operation')

calc(x, y, op)
