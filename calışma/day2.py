faiz=1.59
vade="36"
krediAdi="İhtiyaç Kredisi"



print(type(faiz))
print(type(vade))

#türleri int yapmam lazım toplayabilmek için çevrilebilecekler çevrilir mesela kredş adi cevrilmez
#print(int(krediAdi))gibi ynalış
print(int(vade)+12)
#int vade de tanımlasak int olarak alır ama 16. satırda tanımlarsak ilk str olduğunu gösterir sonra int cevirir
vade=int(input("lütfen istediğiniz vade sayısını giriniz:"))
print(type(vade))
vade=vade+12


# vade=int(input("lütfen istediğiniz vade sayısını giriniz:"))BU ALANDA İNT OLDU TYPE İNT
# print(type(vade))
# print(int(vade)+12)


#STRİNG İNTERPOLATİON

print("Seçtiğiniz vade :"+str(vade))

#FORMATA CEVİREREK
print("Seçtiğiniz vade :{vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade :{vade}")


metin="merhaba {name}".format(name=32)
print(metin)

#f string direk değişkeni kullanabiliriz veya python kodu

metin=f"Hoşgeldiniz{1+1}"
print(metin)