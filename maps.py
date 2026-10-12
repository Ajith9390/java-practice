from typing import override
class sub:
    def add(self):
        print("It is superclass:")

class child(sub):
    @override
    def add(self):
        print("child class:")
    
    def sum(self):
        print("IT is child class method:")
    

c=child()
c.add()
c.sum()

    
    
    
