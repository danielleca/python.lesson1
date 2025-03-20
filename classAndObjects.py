class Car:
    #two types of functions are 1. Pre-build or built-in function 2. User-defined function
    def __init__(self,b,s,w,d):
        self.color=b
        self.seats=s
        self.windows=w
        self.tires=4
        self.doors=d
    def service(self):
        print("your service is due")

#creating an object
lamborghini=Car("yellow",2,4,2)
print(lamborghini.tires)
lamborghini.service()

class Bike:
    #two types of functions are 1. Pre-build or built-in function 2. User-defined function
    def __init__(self,b,s):
        self.color=b
        self.seats=s
        self.tires=2
    def repair(self):
        print("a repair is due")

#creating an object
Trek=Bike("red",1)
print(Trek.tires)
Trek.repair()
