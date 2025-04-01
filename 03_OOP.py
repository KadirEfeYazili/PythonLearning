# HAFTA 3
"""
Robot Sınıfı Oluştur.
Öznitelik : namei build_year, timer eklensin
name ve build_year gizli
timer public öznitelik
nesne metotları: get_name, set_name
get_build_year, set_build_year
__str__ metodu ekleyelim. name : ... build_year : ...
"""

"""class Robot():

    def __init__(self, name, build_year, timer):
        self.__name = name
        self.__build_year = build_year
        self.timer = timer

    def set_name(self, isim):
        self.__name = isim

    def get_name(self):
        return self.__name

    def set_build_yr(self, yil):
        self.__build_year = yil

    def get_build_year(self):
        return self.__build_year

    def __str__(self):
        return "Name : " + self.__name + "\nBuild_year : " + str(self.__build_year)

#Nesne Oluştur

robot1 = Robot("Robot1", "1980", "Macintosh")
print(robot1.get_name()) # get_name metotu ile gizli veriye erişme

#timer değerine erişim
print(robot1.timer) # 100
robot1.set_name("DOGUS")
print(robot1.get_name())
robot1.set_build_yr("100")
print(robot1.get_build_year())
print(robot1.__str__())
"""

"""
Örnek Bir Student sınıfı oluştur.
Nesne Öznitelikler : name ve index 
Sınıf öznitelik: number_student ve değeri 40
destructive() yıkıcı metotu ekle : öğrenci sayısını her çağrışılında öğrenci sayısını bir azaltsın

"""
"""
class Student():

    number_Student = 40

    def __init__(self, name, index):
        self.name = name
        self.index = index
        Student.number_Student += 1 # her nesne oluşturuldupıunda number_Student değeri bir artacak

    def __del__(self):
        Student.number_Student -= 1 # her nesne silindiğinde number_Student değeri bir azalacak

st1 = Student("Zeyd",202302009024)
st2 = Student("Kadir",202302009102)


print(Student.number_Student)
del st2
print(Student.number_Student)
st3 = Student("Mahmud", 384294328764)
del st3
print(Student.number_Student)
"""

"""class A():
    a="I am a class attribute !"
x=A()
y=A()
print(y.a)
print(A.a)"""

"""
class Robot():
    __counter=0
    def __init__(self):
        Robot.__counter+=1
        #type(self).counter+=1
    def Robotinstances(self):
        return Robot.__counter
x=Robot()
print(x.Robotinstances())
y=Robot()
print(x.Robotinstances())"""

# -------------------

"""
@staticmethod bezeyicisi : bir methodun sınıf_adı
hem de Nesne_adı ile erişilebilirliğini sağlar sınıf içindeki 
metodun üzerinede @staticmethod yazarız ve self parametresi olmaz.
"""


"""class Robot():
    __counter = 0

    def __init__(self):
        Robot.__counter += 1

    @classmethod
    def robotInstances(cls):
        return Robot.__counter


robot3 = Robot()
print(robot3.robotInstances())
print(Robot.robotInstances())"""

"""
Örnek. "MAT"
"""

"""
class Mat():

    @staticmethod
    def pi():
        return 22/7

    @staticmethod
    def kök(sayi):
        return sayi**(1/2)

deneme1 = Mat()
print(deneme1.pi())
print(deneme1.kök(4))
print(deneme1.kök(121))

"""

"""
sınıf nitelikleri üzerinde işlme yapılacağı zaman classmethod beizyecisi ve cls parametreleri kullanılır.
"@classmethod" ve "cls"


"""

"""class Mat2():

    @classmethod
    def pi(cls):
        return 22/7

    @classmethod
    def kök(cls, sayi):
        return sayi**(1/2)

deneme1 = Mat2()
print(deneme1.pi())
print(deneme1.kök(81))
print(deneme1.kök(144))
"""

"""
"Franction" sınıf oluştur.
kesirli bir iafdetyi basit bir kesire indirgesin
"""
"""
class Fraction():
    def __init__(self, n, d):
        self.n, self.d = Fraction.reduce(n,d)

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    @classmethod
    def reduce(cls, pay, payda):
        g = cls.gcd(pay,payda)
        return pay // g, payda // g
    def __str__(self):
        return str(self.n) + "/" + str(self.d)


x=Fraction(9,54)
print(x)
"""