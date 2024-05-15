from mathematical_operations import mathematical_operations
from globals import  a
from globals import  b
from mathematical_operations import operation

def division_by_zero():
    # global a
    global b
    global operation
    if operation=='/'and b==0 :
     return print ('деления на ноль запрешено')
    
