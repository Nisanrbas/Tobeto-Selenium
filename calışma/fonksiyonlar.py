#fonksiyonlar
#def fonksiyon tanımlamadır


fiyat=100
indirim=20

yeniFiyat=fiyat-indirim

def calculate():
   print(100-20)

calculate()

calculate()

def calculateWthParams(a,b):
    print(a-b)


calculateWthParams(100,20)

calculateWthParams(100,30)

def sayHello(name):
    print(f"merhaba {name}")


sayHello(5)
sayHello("Nisa")

def calculateAndReturm(price,discount):
    return price-discount

yeniFiyat=calculateAndReturm(200,50)
print(yeniFiyat)
print("*************************")

def cal1(price,discount):
  print(price-discount)

def cal2(price,discount):
    return price-discount


print("*************************")
fonk1=cal1(100,50)
fonk2=cal2(200,50)
print("*************************")
#returnde değer olarak alır ama diğerinde değer olmadığı için none 
print(fonk1)
print(fonk2)