f=open('file IO/myfile.txt','r')
text=f.read()
print(text)
f.close()

f=open('file IO/myfile.txt','a')
f.write('\nThis is an appended line.')
f.close()

f=open('file IO/myfile.txt','w')
f.write('This is a new content, previous content is deleted.')
f.close()

#with statement is used to automatically close the file after its block of code is executed, even if an error occurs. It is a good practice to use with statement for file handling.

with open('file IO/myfile.txt','r') as f:
    text=f.read()
    print(text)
