from abc import ABC, abstractmethod

class Parent:
    def show(self):
        print("Inside Parent")

class Parent2:
    def show(self):
        print("Inside Parent2")

class Child(Parent2, Parent):
    def show(self):
        super().show()
        super(Parent2, self).show()
        return "Inside Child"
    
# class Child2:
#     def show(self):
#         print("Inside Child2")

# class Child3(Child2, Child):
#     def show(self):
#         super(Child2, self).show()
#         super().show()
#         return "Inside Child3"

obj = Child()
print(obj.show())