#FOR DÖNGÜSÜ
#İ=0 İ<10 BİR ŞARTIN CONDİTATİON 
#RANGE İ DEĞERİNİ ALIP İÇERİSİNDEKİ DEĞER EULAŞANA KADAR 1 ARTTIRACAK FONKSİYON
for i in range(10):
    print("ii")
    print(i)

#sıfırdan başlamak isyeitorsak

print("**********************")

for i in range (5,10):
    print(i)
#değer olarak int vermek zorundayız 
print("**********************")
for i in range (5,20,2):
    print(i)

print("**********************")

krediler=["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
for kredi in krediler:
    print(kredi)

print("**********************")


for i in range(len(krediler)):
    print(krediler[i])
i=0
while i<10:
    print("x")
    i+=1
print("y")
print("**********")
while True:
    print("x")
    break
print("**********************")

i=0
while i<len(krediler):
    if krediler[i]=="Konut Kredisi":
        break
    print(krediler[i])
    i+=1
