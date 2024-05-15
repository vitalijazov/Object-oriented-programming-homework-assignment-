
from globals import a
from globals import  b
from globals import globals

global operation  
operation=str(input('введите нужную операцию: '))
def mathematical_operations(): 
    if operation=='+':
        print (a+b)
    elif operation=='*':
        print(a*b)
    elif operation=='/' :
        print(a//b)
    elif operation== '-':
        print(a-b)
        











