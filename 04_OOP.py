"""
Parent class: Pet sınıfı tanımlayın
sınıf değişkeni:_class_info olsun ve "pet animals"
nesne metodu: about(): "this is about" +self._class_info
-------------------------------
Dog ve Cat sınıfı(child class) Pet sınıfını miras alsın
"""
"""
class Pet:
    _class_info="Pet animals"
    def about(self):
        print("This is about"+self._class_info +"!")
#miras ala sınıf Dog ve Cat
class Dog(Pet):
    pass
#nesne olutur
köpek1=Dog()
köpek1.about() #This is aboutPet animals! Miras alındı
print(Pet._class_info) #Pet animals
print(Dog._class_info) #Pet animals 
# #miras ile hem nesne metodu(about)
#hem de sınıf özniteliği _class_info Dog sınıfına aktarıldı.
"""
class Pet:
    _class_info="Pet animals"
    def about(self):
        print("This is about "+self._class_info +"!")
#miras alt sınıf ya da child class Dog ve Cat
class Dog(Pet):
    _class_info="Man's best friend"
class Cat(Pet):
    _class_info="all kinds of cat"
"""
Aynı isimle değişkeni child class ta tanımlarsam
en son tanımladığım geçerli olur. 
"""
#nesne oluştur
köpek2=Dog()
print(Dog._class_info)
kedi1=Cat()
print(Cat._class_info)
#Pet sınıfında nesne oluşturma
pet1=Pet()
#metod çağırma
pet1.about()
köpek2.about()
kedi1.about()
#Örnek1.
"""
vCalışan sınıfı oluştur.
vNesne özniteliklerim: ad, soyad,maas
vsınıf özniteliğim: zam_oranı, personel_sayısı
*Nesne oluşturulur oluşturulmaz personel_sayısı artsın
Nesne metodları: tamad(), arttır() 
tamad():ad ve soyadı düzgünce ("".format(ad,soyad))yazdırsın
arttır(): maaşı, zam orasına göre arttırsın 
Sınıf metodları: 
zam_oranı_değiş(): zam oranını "yeni_oran" a göre değiştirsin

"""
class Calisan():
    zam_oranı=1.05
    personel_sayısı=0
    def __init__(self,ad,soyad,maaş):
        self.ad=ad
        self.soyad=soyad
        self.maaş=maaş
        Calisan.personel_sayısı+=1
    def tamad(self):
        print("Ad: {}\nSoyad: {}".format(self.ad,self.soyad))
    def arttır(self):
        self.maaş=self.maaş*self.zam_oranı
    @classmethod
    def zam_oranı_değiş(cls,yeni_oran):
        cls.zam_oranı=yeni_oranı

#nesne oluştur
calısan1=Calisan("Yunus","Emre",50.000)
calısan2=Calisan("Emre","Altuğ",100.000)
calısan3=Calisan("Kenan","Doğulu",200.000)
calısan1.tamad()
calısan1.arttır()
print(calısan1.maaş)
print(calısan1.personel_sayısı)