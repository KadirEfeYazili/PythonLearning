"""
#Bir Araç sınıfı oluşturalım
class Araç():
    pass
#Sınıftan nesne oluşturma
Bisiklet=Araç()
Bisiklet.renk="Pembe"
Bisiklet.model="Dağ bisikleti"
Bisiklet.marka="Salcano"
print("Renk:{}\n Model:{}\n Marka:{}\n".format(Bisiklet.renk,Bisiklet.model,Bisiklet.marka))
Tır=Araç()
Tır.renk="Kırmızı"
Tır.model="Yük tırı"
Tır.marka="Volvo"
print("Renk:{}\n Model:{}\n Marka:{}\n".format(Tır.renk,Tır.model,Tır.marka))
"""
"""
class Araç():
    renk="Siyah"
    model="Hız arabası"
    marka="Ferrari"
#Nesne oluştur
araba1=Araç()
#araba1 nesnesinin rengi nedir ?
print(araba1.renk)
#araba1 nesnesini modeli nedir ?
print(araba1.model)
#araba1 nesnesinin markası nedir ?
print(araba1.marka)
#Ayrı sınıftan bir sürü nesne oluşturabilirim
araba2=Araç()
print(araba2.renk)
#araba2 nesnesinin rengini sarı yapalım.
araba2.renk="sarı"
#Nesne üzerindeki değişiklikler sadece o nesneyi etkiler
#Ama sınıf üzerindeki değişiklikler tüm nesneleri etkiler
print(araba2.renk)
print(araba2.model)
print(araba2.marka)
"""
#Araç sınıfının içerisinde, __init__ metodunu tanımlayacağım
"""class Araç():
    def __init__(self,renk,model,marka):
        self.renk=renk
        self.model=model
        self.marka=marka
        self.hız=0
    def hızlandır(self):
        self.hız+=20
        return self.hız
# Araç sınıfında nesneler oluşturuyorum
Car1=Araç("Yeşil","Station","Ford-C max") #tek satırlar tüm özellikleri tanımladım
print("Renk:{}\n Model:{}\n Marka:{}\n".format(Car1.renk,Car1.model,Car1.marka))
#Car1 sınıfının rengini mavi yapalım
Car1.renk="Mavi"
print("Renk:{}\n Model:{}\n Marka:{}\n".format(Car1.renk,Car1.model,Car1.marka))
#Car2 nesnesi oluşturalım
Car2=Araç("Kırmızı","Hatchback","Volvo")
print("Renk:{}\n Model:{}\n Marka:{}\n".format(Car2.renk,Car2.model,Car2.marka))
#Nesne metodu olarak hızlandır metodunu ekledik
#Nasıl çalıştırıyorum ?
#nesne_adı.metod_adı()  şeklinde çalışır.
Car1.hızlandır()
print(Car1.hız)
Car1.hızlandır()
print(Car1.hız)"""


#Robot sınıfı oluşturalım ve name ve build_year özniteliklerini ekle
class Robot:
    pass
x=Robot() # x nesnesi
y=Robot() # y nesnesi
x.name="Marvin"
x.build_year="1970"
y.name="Caliban"
y.build_year="1980"
#•	Örnek  oluşturulurken, içte tüm öznitelikler sözlük yapısı altında saklanır.
print(x.__dict__) #{'name': 'Marvin', 'build_year': '1970'}
print(y.__dict__)
#print(y.brand) #AttributeError: 'Robot' object has no attribute 'brand'
#Sınıf adı üzerinden de öznitelik atanabilir
Robot.brand="kuka"
print(x.brand)
print(y.brand)
x.brand="thales"
print(y.brand) #kuka
print(x.brand) #thales
#Sınıf üzerine yapılan değişiklikler tüm nesneleri etkiler
#tersi doğru değil
#getattr() ile var olmayan  bir özniteliği ve değerini ekleyebiliriz
print(getattr(x,'energy',100))
#Örnek.
"""
1.Robot sınıfı oluştur
2.Nesne Öznitelikleri: name,build_year, brand
3.Nesne Metodu: say_hi olsun ve eğer name var ise
"Hi, I am"+ self.name, name yok ise "I am a Robot without name"
"""
"""
class Robot():
    def __init__(self,name,build_year, brand):
        self.name=name
        self.build_year=build_year
        self.brand=brand
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without name")
#nesne oluştur
robot1=Robot("Marvin","1970","thales")
print("Adı:{}\n Yılı:{}\n Marka:{}".format(robot1.name,robot1.build_year,robot1.brand))
#Özniteliklere sınıf adı ile erişilir mi?
#print(Robot.name) # AttributeError: type object 'Robot' has no attribute 'name'
#Nesne metodunun çağırılması
robot1.say_hi()#nesne_adı.Metod_adı()
# metodları PARANTEZ ile çağırıyoruz
#Sınıf adı ile nesne metodu çağrılır mı?
#Robot.say_hi() #Hata veriyor, çağrılmıyor
"""
#Örnek.
"""
Robot sınıfı
Nesne öznitelikleri: name ve build_year 
set_name(): name değişkenini değiştirir
get_name(): name değişkenini söyler
set_build_year(): build_year değiştirir
get_build_year(): build_year değerini söyler,döndürür
"""
"""
class Robot():
    def __init__(self,name,build_year):
        self.name=name
        self.build_year=build_year
    def get_name(self): #parametre almaz getter metodlar
        return self.name
    def set_name(self,isim): # yeni parametre alır
        self.name=isim
    def get_build_year(self):
        return self.build_year
    def set_build_year(self,değişen_yıl):
        self.build_year=değişen_yıl
#Nesne oluştur
robot2=Robot("Hegel","1967")
print(robot2.get_name()) #yeni ismi al
robot2.set_name("Herkül") #ismi Hegel >>> Herkül oldu
print(robot2.get_name()) #yeni ismi al
print(robot2.get_build_year())
robot2.set_build_year("2025")
print(robot2.get_build_year())
"""
#Örnek. Public, Protected, Private

class A:
    def __init__(self):
        self.public="I am public" # acik veri
        self._protect="I am protected" # yari gizli veri
        self.__private="I am private" # tamamen gizli veri

    def get_private(self):
        return self.__private
a=A()
print(a.public)
print(a._protect)
print(a.get_private())
#print(a.__private) #AttributeError: 'A' object has no attribute '__private'.
#Peki gizli veriye nasıl erişiriz ?
