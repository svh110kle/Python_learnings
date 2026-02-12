# is and == are two different operators in Python that are used for comparison, but they serve different purposes.
# The '==' operator checks for value equality. It checks if the values of the objects being compared are equal, regardless of whether they are the same object in memory.
# The 'is' operator checks for identity. It checks if the two operands refer to the

#if objects is muteable, they may have the same value but be different objects in memory. In this case, '==' would return True, while 'is' would return False.
# Example:
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Output: True (values are equal)
print(a is b)  # Output: False (different objects in memory)

# If the objects are immutable (like integers, strings, etc.), Python may optimize memory usage by reusing the same object for identical values. In this case, '==' and 'is' may both return True.
# Example:
x = 10
y = 10
print(x == y)  # Output: True (values are equal)
print(x is y)  # Output: True (same object in memory due to optimization)
print(x is 10) # Output: True (same object in memory due to optimization)
# However, this behavior is not guaranteed for all immutable objects, and it can vary based on the implementation of Python. Therefore, it's generally recommended to use '==' for value comparison and 'is' for identity comparison.