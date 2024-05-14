
#dizi içerisinde farklı tipler kullanılabilir.
dizi=["ihtiyaç",10,True]



krediler=["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))
print(krediler)

print(krediler[0])
print(len(krediler))#lenght veri sayısını verir o yüzden indexs 1 eksiği ne kadardır


krediler.append("Özel Kredi")
print(krediler)

krediler.append("X kredisi")
print(krediler)
#parantez içi boş ise sonuncuyu siler
krediler.pop()
print(krediler)
#remove değer siler

krediler.remove("Taşıt Kredisi")
print(krediler)

#extebd 1 den fazla ekleme için
krediler.extend(["Y Kredisi","Z KREDİSİ"])
print(krediler)

