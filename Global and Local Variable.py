x=10 #globlal variable

def my_function1():
    y=5
    print("The value of x is:",x) #accessing global variable
    print("The value of y is:",y) #accessing local variable
    
my_function1()
# to cahnge the value of global variable inside a function we need to use global keyword
def my_function():
    global x #declaring x as global variable
    x=20 #changing the value of global variable
    print("The value of x inside the function is:",x)
    
my_function()
print("The value of x outside the function is:",x) #accessing the changed value of global variable