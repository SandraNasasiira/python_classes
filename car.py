class Car:

    def __init__(self,model,color,name,speed):
              self.name=name
              self.model=model
              self.color=color
              self.speed=speed
    def move(self):
        return f"Hey,this car moves fast and it's name is {self.name} and it is {self.color} in color and it's a {self.model}it moves{self.speed}"
    def hoot(self):
        return f"My car is {self.name}, it's{self.color}in color and it's a{self.model}and it hoots when it senses danger"