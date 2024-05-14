class Human:
    
#built_init
#initialize=başlatmak
    def __init__(self,name):
        self.name=name
        print("bir human instance'i üretildi")
    def __str__(self):
        return f"STR fonksiyonunda dönen değer :{self.name}"
     

    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print("Human is walk")

#instance=örnek
#self=this
human1=Human("ENES")
human1.talk("Merhaba")
human1.walk()
print(human1)


human2=Human("halit")
human2.talk("Selam")
human2.walk()
print(human2)

