class Myclass:
    def __init__(self,value):
        self._value = value
    def show(self):
        print(f"Value is {self._value}")
        

    
    @property
    def ten_value(self):
        return 10 * self._value
    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value / 10
        
obj = Myclass(5)
obj.ten_value = 100
print(obj.ten_value)
obj.show()

#getter and setter are used to control access to the attributes of a class. The @property decorator is used to define a getter method, which allows you to access the value of an attribute as if it were a regular attribute. The @ten_value.setter decorator is used to define a setter method, which allows you to set the value of an attribute while performing some additional logic (in this case, dividing the new value by 10 before assigning it to _value).
#using getter we can calculate the value on the fly without storing it, and using setter we can control how the value is set and perform any necessary validation or transformation before assigning it to the attribute.
