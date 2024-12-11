# from collections import namedtuple
# # 1 misol
# talaba = [
#     ("Toxir",22,"matematika"),
#     ("Sobir", 23,"ona tili")
# ]
#
# Person = namedtuple('Person',['name','age','major'])
#
# for i in  talaba:
#     person=Person(*i)
#     print(f"Name: {person.name} Age: {person.age} Major:{person.major}")



#
# 2 misol
#
# maxsulot = [
#     ("Olma ","8.000","10"),
#     ("Anor", "15.000","8")
# ]
#
# Maxsulot = namedtuple('Maxsulot',['product_name','price','quantity'])
#
# for i in  maxsulot:
#     meva=Maxsulot(*i)
#     print(f"Meva: {meva.product_name} Narx: {meva.price} Miqdor:{meva.quantity}")

# 3 misol
# from collections import namedtuple
#
# shahar = [
#     ("Toshkent ","Uzbekistan","3.000.000"),
#     ("Farg'ona"," Uzbekistan" ,"320.000")
# ]
# Shaxarlar = namedtuple('Shaxarlar',['city','country','population'])
# def kop_aholi(shaharlar):
#     max_population = 0
#     largest_city = None
#     for city in shaharlar:
#         pop = int(city[2].replace('.', '').replace(',', ''))
#         if pop > max_population:
#             max_population = pop
#             largest_city = city
#     return Shaxarlar(*largest_city)
# for i in shahar:
#     s = Shaxarlar(*i)
#     print(f"City: {s.city.strip()}, Country: {s.country.strip()}, Population: {s.population}")
# aholilashgan = kop_aholi(shahar)
# print(f"Eng ko'p aholi yashaydigan shahar: {aholilashgan.city.strip()} Aholi soni: {aholilashgan.population}")
#
#
#
#

# 4 misol
# avtomobillar = [
#     ("Chevrolet", "Malibu", 2020),
#     ("Toyota", "Camry", 2022),
#     ("Honda", "Civic", 2021)
# ]
# Avtomobil = namedtuple('Avtomobil', ['make', 'model', 'year'])
#
# def eng_yangi_avtomobil(avtomobillar):
#     newest_car = sorted(avtomobillar, key=lambda x: x[2], reverse=True)[0]
#     return Avtomobil(*newest_car)
# for car in avtomobillar:
#     avtomobil = Avtomobil(*car)
#     print(f"Make: {avtomobil.make}, Model: {avtomobil.model}, Year: {avtomobil.year}")
# eng_yangi = eng_yangi_avtomobil(avtomobillar)
# print(f"Eng yangi avtomobil: {eng_yangi.make} {eng_yangi.model}, Yili: {eng_yangi.year}")
#


#
#  5 misol
# def fff(x):
#     def ff2(y):
#         return x + y
#     return ff2
#
# f = fff(5)
# f2 = f(10)
# print(f2)
#
# 6 misol
# def fff(a):
#     def ff2(b):
#         return a + b
#     return ff2
#
# f = fff("Salom ")
# f2 = f(input("ismingizni kiriting: "))
# print(f2)
#
#
# 7 misol
# def fff(a):
#     def ff2(b):
#         return a + b
#     return ff2
#
# f = fff( 5)
# f2 = f(int(input("son kiritng: ")))
# print( "javob", f2)

# 8 misol
# def create_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
# my_counter = create_counter()
# print(my_counter)

#  9 misol

# def fff(x):
#     def ff2():
#         return x ** 2
#     return ff2
#
# f = fff(int(input("Son kiriting: ")))
# f2 = f()
# print(f2)

#  10 misol
# def fff():
#     l = []
#
#     def ff2(ism):
#         l.append(ism)
#         return l
#
#     return ff2
#
# f2 = fff()
# print(f2("Toxir"))
# print(f2("Sobir"))
# print(f2("Bakir"))

#  11 misol
# def fff(a):
#     def ff2(b):
#         return  a * b / 100 - a
#     return ff2
#
# f = fff(int(input("chegirma foizini kiriting: ")))
# f2 = f(int(input("Maxsulot narxi kiriting: ")))
# print( "chegirmadagi narxi", f2)
#
# 12 misol
# def fff(a):
#     sss = a
#
#     def ff2(b):
#         nonlocal sss
#         sss *= b
#         return sss
#
#     return ff2
#
# f = fff(2)
# print(f(3))
# print(f(4))
# print(f(5))


#  13 msiol
# def fff(a):
#     qator = a
#     def ff2(b):
#         nonlocal qator
#         qator += b
#         return qator
#
#     return ff2
#
# f = fff("Salom, ")
# print(f("dunyo"))
# print(f(" Hello"))
# print(f(" world"))

#  14 misol
# d = []
# def fff(x):
#     def ff2():
#         global d
#         nonlocal x
#         for i in range(x):
#             if i % 2 == 1:
#                 d.append(i)
#     return ff2
#
# x = fff(int(input("Son kiriting: ")))
# x()
# print("toq sonlar ",d)
#
# 15 misol
#
# def fff(x):
#     def ff2(y):
#         return x ** y
#     return ff2
#
# f = fff(int(input("Son kiriting: ")))
# f2 = f(int(input("son2 kiriting: ")))
# print(f2)


#  16 msiol
# def fff(x):
#     def ff2():
#         return x
#     return ff2
# f =  input("so'z kiriting: ")
# f2=f[::-1]
# print(f2)

# 17 misol
# def fff():
#     savat = []
#
#     def ff2(mahsulot, narx):
#         savat.append((mahsulot, narx))
#         umumiy_summani_hisobla = sum(narx for _, narx in savat)
#         return umumiy_summani_hisobla
#
#     return ff2
#
#
# f = fff()
# print(f("Olma", 5000))
# print(f("Banan", 7000))
# print(f("Anor", 10000))

# 18 misol
narxlar = []
def fff():
    def ff2(narx):
        global narxlar
        narxlar.append(narx)
    return ff2

f = fff()
f(5000)
f(7000)
f(10000)
print(narxlar)