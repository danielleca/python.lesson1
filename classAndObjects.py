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