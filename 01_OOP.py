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
class Araç():
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
print(Car1.hız)
