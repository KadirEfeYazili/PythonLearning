"""
class Çalışan():
    calışan_liste=[]
    sigorta_puanı=25
    def __init__(self,isim,cinsiyet,maas):
        self.isim=isim
        self.__cinsiyet=cinsiyet
        self.maas=maas
        Çalışan.calışan_liste.append(self.isim)
    @classmethod
    def personeli_görüntüle(cls):
        print("Personel listesi yazdırılıyor!")
        print(cls.calışan_liste)
    def personel_ekle(self,ad):
        Çalışan.calışan_liste.append(ad)
    def sigorta_yatırım(self):
        Çalışan.sigorta_puanı+=15
        print(Çalışan.sigorta_puanı)
    @staticmethod
    def İfade_et(özellik):
        print("En belirgin özelliği", özellik)
#nesne oluşturmam
çalışan1=Çalışan("Ayhan Koçak","Erkek",30000)
#print(Çalışan.calışan_liste)
çalışan2=Çalışan("Eda Özülkü","Kadın",60000)
#print(Çalışan.calışan_liste)
#Çalışan.personeli_görüntüle()
çalışan2.personeli_görüntüle()
çalışan1.personel_ekle("Ferhat Görçer")
çalışan1.personeli_görüntüle()
print(çalışan1.sigorta_puanı) #25
çalışan1.sigorta_yatırım()
çalışan1.sigorta_yatırım()
"""
"""
a) Bir "Anne" sınıfı oluşturunuz.
Nesne öznitelikleri: isim, yaş, gözrengi, boy
Nesne metodu: "bilgileri_görüntüle" olsun ve şu şekilde
yazdırsın:
"Annemizi tanıyalım"
Adı:..
Yaşı:..
Gözrengi:..
Boyu:..
b) "Anne" sınıfını miras alan bir "Evlat" sınıfı
tanımlayın.
Evlat sınıfı "Anne" sınıfını miras alsın,
özniteliklere ayrıca "zeka_puanı" eklensin.
c)"Evlat" sınıfı "Bilgileri_görüntüle" metodunu
"overriding" yapsın, ve "Evlat zeka_puanı:.." ekleyip
yazdırsın
"""
"""
class Anne():
    def __init__(self,isim,yaş,gözrengi,boy):
        self.isim=isim
        self.yaş=yaş
        self.gözrengi=gözrengi
        self.boy=boy
    def bilgileri_görüntüle(self):
        print("Annemizi tanıyalım")
        print("Adı:{} \nYaşı:{}\nGözrengi:{}\nBoy:{}".format(self.isim,self.yaş,self.gözrengi,self.boy))
class Evlat(Anne):
    def __init__(self,isim,yaş,gözrengi,boy,zeka_puanı):
        super().__init__(isim,yaş,gözrengi,boy)
        self.zeka_puanı=zeka_puanı
    def bilgileri_görüntüle(self):
        super().bilgileri_görüntüle()
        print("Zeka puanı:{}".format(self.zeka_puanı))

evlat1=Evlat("Hasan altuğ", 8,"mavi",90,140)
print(evlat1.zeka_puanı) #140
evlat1.bilgileri_görüntüle()
#nesne oluştur
#anne1=Anne("Yeşim çiçek",41,"Kahve",170)
#anne1.bilgileri_görüntüle()
"""