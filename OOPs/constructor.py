#constuctor is a special method which is automatically called when an object of a class is created. It is used to initialize the attributes of the class.
#In Python, the constructor is defined using the __init__ method. The __init__ method takes at least one argument, which is usually named self. The self argument refers to the instance of the class that is being created.
#self is used to access the attributes and methods of the class. It is a convention to use self as the first parameter of the __init__ method, but you can use any name you want.

class svh:
    
    def __init__(self,name,age,networth):
        self.name=name
        self.age=age
        self.networth=networth
        
    def info(self):
        print(f"my name is {self.name} and i am {self.age} years old and my networth is {self.networth}")
a = svh("satyarth",19,5000)
b = svh("shailesh",20,6400)
a.info()
b.info()
#if we do not define a constructor in a class, then the default constructor is used, which does not take any arguments and does not initialize any attributes.
#defult constructor is provided by Python and it does not do anything. It is used when we do not want to initialize any attributes of the class.

class svh:
    def __init__(self):
        print("this is a default constructor")
a = svh()
#here we cretared two same class with the same name but different constructors. This is called constructor overloading. In Python, we cannot have multiple constructors in a class, but we can achieve constructor overloading by using default arguments in the __init__ method.