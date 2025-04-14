"""
Miras (inheritence)
Örnek1. Robot sınıfı tanımlayalım.
nesne öznitelikleri: name
nesne metodu:say_hi olsun ve "merhaba desin, ismini yazdırsın"
Robot sınıfını miras alan
PhysicianRobot chil class ı oluşturalım
"""
"""
class Robot():
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("Hello, my name is " +self.name)
class PhysicianRobot(Robot):
    pass
#nesne oluştur
robot1=Robot("Hasan")
robot2=PhysicianRobot("Ahmet")
print(robot1.name)
robot1.say_hi()  #Hello, my name is Hasan
print(robot2.name)
robot2.say_hi() #Hello, my name is Ahmet
"""
# say_hi() metoduna overriding yapılıyor.(güncelleme)
# şöyle desin:"everything will be ok.self.name take cares of you"
import random
class Robot():
    def __init__(self,name):
        self.name=name
        self.healt_level=random.random()
    def say_hi(self):
        print("Hello, my name is " +self.name)
    def needs_a_doctor(self):
        if self.healt_level<0.8:
            return True
        else:
            return False
class PhysicianRobot(Robot):
    def say_hi(self):
        super().say_hi() #üst sınıfın metodunu direk aldı
        print("Everything will be ok !")
        print(self.name + " takes care of you !")
    def heal(self,robo):
        robo.healt_level=random.uniform(robo.healt_level,1)
        print(robo.name+" has been healed by "+ self.name)
#nesne oluştur
robot1=Robot("Hasan")
print(robot1.healt_level) #rastgele değerler atanmış
print(robot1.needs_a_doctor())
#robot1.say_hi()
robot2=PhysicianRobot("Ahmet")
#robot2.say_hi()
robot2.heal(robot1) #Hasan has been healed by Ahmet
#robot1.heal(robot2) Robot sınıfı PhysicianRobot'un metdolarını almaz
robot2.say_hi()