#To create a class  use class keyword
#Start the class with a capital letter.If the class has more than one word Capitalise each word
#you can not have spaces in a class name
#when you save your code in a py file its calle a module
#To import a class from a module use dot notion  from module import class name
#car.py give it attributes,behaviour
#dog.py  attributes
class Student:
    school="Akirachix"
    def __init__(self,name,age):
              self.name=name
              self.age=age
    def Speak(self):
        return f"Hello my name is { self.name} and I am {self.age} years old and i love {self.school}"