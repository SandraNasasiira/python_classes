 class Dog:
 def __init__(self,color,name,age):
              self.name=name
              self.age=age
              self.color=color

 def bark(self):
        return f"my dog's name is{self.name},it is{self.age}years old and{self.color}.It barks at strangers"