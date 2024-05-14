print("kodlama")
baslik= "Taşıt Kredisi"
print(baslik)
baslik="İhtiyaç kredisi"
print(baslik)

#int0tam sayı
vade=36
vade2="36"
ekVade= 6
#float,decimal,double
aylikOdeme=200.50
#boolen0true false
yukselisteMi=False

#matematiksel

print(vade+5)
print(vade+ekVade)
print(vade-3)
print(vade*ekVade)
#bölmede float şekilde değer döndürür.tam bölünse bile
print(vade/2)

# %mod operatorü

print(10%2)
print(vade%2)
print(vade%5)

#mantıksal
print(1==1)
print(1==2)
print(1<3)
print(1>4)

print(1!=1)
print(1!=2)

#or ikisinden biri veya anlamına

print(1<4 or 1>5)

#and ikiside 
print(1<4 and 1>5)


print(1<4 or 1>5 and 3>2)

#karar yapıları

# if else elif

sayi1=15
sayi2=15

# sayi1 sayi2 den büyükse  ekrana sayi1 büyük yazdır
# condition=şart
#indent
if sayi1>sayi2:
    print("sayi1 sayi2 den büyük")
    print("if bloğunun icindeyim")

elif sayi1==sayi2:
    print("iki sayi eşit")
#if veya eliften biri sağlanmadıysa else 
else:
    print("sayi1 sayi2 den küçüktür")

print("if bloğunun dışındayım")

# if sayi1<sayi2:
#     print("sayi1 sayi2 den büyük")
#     print("if bloğunun icindeyim")

# print("if bloğunun dışındayım")
