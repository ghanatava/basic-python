'''polymorphism: using same method to produce different result based on the class
it is present in'''

class Kali:
    def advantage(self):
        print('More powerful')
    def disadvantage(self):
        print('Resource intensive')

class Parrot:
    def advantage(self):
        print('Light weight')
    def disadvantage(self):
        print('Small community')
kali=Kali()
parrot=Parrot()
for obj in [kali,parrot]:
    print(type(obj))
    obj.advantage()
    obj.disadvantage()

