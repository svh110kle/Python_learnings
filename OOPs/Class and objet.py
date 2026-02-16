class Person:
    name="shailesh"
    occupation="student"
    networth=6400
    def info(self):
        print(f"my name is {self.name} and i am a {self.occupation} and my networth is {self.networth}")
        
        
a = Person()
b= Person()
a.name="satyarth"
a.occupation="student"
a.networth=5000
b.name="shailesh"
b.occupation="student"
b.networth=6400
a.info()
b.info()