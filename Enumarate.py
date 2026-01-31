marks=[12,98,56,44,67,889,66,45,23,78]
index=0
for mark in marks:
    print(mark)
    if(index==6):
        print("shailesh hi")
    index+=1
    
#to replace above code with enumerate
marks=[12,98,56,44,67,889,66,45,23,78]
for index,mark in enumerate(marks,start=1):
    print(mark)
    if(index==6):
        print("shailesh hi")
    