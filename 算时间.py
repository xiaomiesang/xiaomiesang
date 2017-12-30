##speed = 60.0
##distance = 100.0
##time = distance/speed
##print (time)



##class Car:
##    speed = 0
##    def drive(self,distance):
##        time = distance/self.speed
##        print (time)
##
##car = Car()
##car.speed = 60.0
##car.drive(100.0)
##
##    


##speed1 = 60.0
##distance1 = 100.0
##time1 = distance1/speed1
##print (time1)
##
##distance2 = 200.0
##time2 = distance2/speed1
##print (time2)
##
##
##speed2 = 150.0
##distance1 = 100.0
##time3 = distance1/speed2
##print (time3)
##
##time4 = distance2/speed2
##print (time4)

##class Car:
##    speed = 0
##    def drive(self,distance):
##        time = distance/self.speed
##        print (time)
##
##car1 = Car()
##car1.speed = 60.0
##car1.drive(100.0)
##car1.drive(200.0)
##
##car2 = Car()
##car2.speed = 150.0
##car2.drive(100.0)
##car2.drive(200.0)

    


class vehicle:
    def __init__(self,speed):
        self.speed = speed

    def drive(self,distance):
        print ('need %f hours'%(distance/self.speed))

class Bike(vehicle):
    pass

class Car(vehicle):
    def __init__(self,speed,fuel):
        vehicle.__init__(self,speed)
        self.fuel = fuel

    def drive(self,distance):
        vehicle.drive(self,distance)
        print ('need %f fuels'%(distance*self.fuel))


b = Bike(15.0)
c = Car(80.0,0.012)
b.drive(100.0)
c.drive(100.0)
    
