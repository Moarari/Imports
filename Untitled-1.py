import random, time, os, string, requests
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# temp=-10
# class Car:
#     def __init__(self,brand,fuel=10,i_show_sped=10):
#         self.brand=brand
#         self.fuel=fuel
#         self.i_show_sped=i_show_sped
#     def stop(self,i_show_sped=0):
#             self.i_show_sped-=self.i_show_sped
#             print(f'{self.brand} ma rychlost {self.i_show_sped}km/h a zastavilo')
#     def go(self,fuel=10,i_show_sped=10):
#         if  self.fuel<=0:
#             print('najprv natankuj')
#             self.stop()
#         else:
#             if temp<-9 and self==ElCar:
#                 if self.fuel<15:
#                     self.i_show_sped+=self.fuel
#                     self.fuel-=self.fuel
#                     print(f'{self.brand} ide rychlostou {self.i_show_sped}km/h a v nadrzi ma {self.fuel} paliva')
#                 else:
#                     self.fuel-=15
#                     self.i_show_sped+=10
#                     print(f'{self.brand} ide rychlostou {self.i_show_sped}km/h a v nadrzi ma {self.fuel} paliva')
#             else:        
#                 self.fuel-=10
#                 self.i_show_sped+=10
#                 print(f'{self.brand} ide rychlostou {self.i_show_sped}km/h a v nadrzi ma {self.fuel} paliva')
# class ElCar(Car):
#     def charge(self,fuel=10):
#         if self==GasCar:
#             print('toto je benzinove auto, nemozes ho tu tankovat.')
#         else:
#             if temp<-9:
#                 self.fuel+=10
#                 print(f'{self.brand} sa nabilo o 10 a teraz ma {self.fuel}')
#             else:    
#                 self.fuel+=10
#                 print(f'{self.brand} sa nabilo o 10 a teraz ma {self.fuel}')
# class GasCar(Car):
#     def top_up(self,fuel=10):
#         if self==ElCar:
#             print('toto je Elektricke auto, nemozes ho tu tankovat.')
#         else:
#             self.fuel+=10
#             print(f'{self.brand} sa natankovalo o 10 a teraz ma {self.fuel}')
# print(temp)
# car1=GasCar('audy',10,0)
# car2=ElCar('tezla',0,10)
# car1.top_up()
# car1.top_up()
# car2.go()
# car2.charge()
# car2.go()
# car1.go()
# car2.go()
# car2.go()
# car2.go()
# car2.go()
# car2.go()
# car2.go()
# car2.stop()
# car2.charge()
# car2.go()

# clear()
# a=[]
# b=2
# c=3
# print('Aku dlzku helsa si prajes:')
# vstup = int(input("Zadaj číslo: "))
# clear()
# print('Please wait.')
# print('Loading...')
# time.sleep(1)
# clear()


# def heslo():
#     global a,b,c

#     for i in range(0,vstup):
#         options = [1,2,3]
#         option = random.choice(options)
#         if option==c:
#             options = ['~','!','@','#','$','%','&','*','+','=','?',]
#             option = random.choice(options)
#             a.append(option)
#             c+=1
#         elif option==b:
#             options = range(0,10)
#             option = random.choice(options)
#             a.append(option)
#             b+=1
#         else:
#             options = string.ascii_letters
            
            
#             option = random.choice(options)
#             a.append(option)
#     print('Vase heslo:')
#     print('')        
#     print(*a, sep="")
#     print('') 
#     print('------------------------------------')
# heslo()




# trieda-   
# objekt
# metoda
# dedenie
# konstructor



# def kocka(a):
#     b=a
#     for i in range(0,a+1):
#         print(' '*b,'♦'*i)
#         b-=1
# kocka(5)    


# class Notifikacia():
#     def __init__(self,odkoho,obsah,precitanost):
#             self.odkoho=odkoho
#             self.obsah=obsah
#             self.precitanost=precitanost
# # ---------------------------------------------------------------------------- 
#     def zobraz(self):
#         print('---------------------------------------------------------')
#         print(f'{self.odkoho} {self.precitanost}')
# # ------------------------------------------------------------------------------
#     def precitaj(self):
#         print('---------------------------------------------------------')
#         if self.precitanost!='Nova':
#             print('Spravu ste uz precitali')
#             print(f'{self.obsah}')
#         else:
#              self.precitanost='stara'
#              print(f'Sprava bola precitana')
#              print(f'{self.obsah}')    
# # ---------------------------------------------------------------------------
# text1=Notifikacia('od Babka 12:30','Dobru hut k obedu :D','Nova')
# text2=Notifikacia('Edupage 8.20','Ziak chybal na hodine','Nova')
# # ----------------------------------------------------------------
# text1.zobraz()
# text1.precitaj()
# text2.zobraz()
# text2.precitaj()
# print('--------------------------------------------------------')


# a=1
# b=0
# list=[]
# print('Lengt of password:')
# vstup= int(input())
# # --------------------------------------------
# clear()
# for i in range(0,vstup):
#     moznost3 = int(random.randint(0,1))
#     if moznost3==1:

#         options = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
#         option = random.choice(options)
#         list.append(option)
#     else:
#         moznosti =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
#         moznost =random.choice(moznosti)
#         list.append(moznost.upper())
# # ----------------------------------------------
# g=0
# moznost1 = int(random.randint(0, vstup-1))
# g=moznost1
# options = ('#','/','?','$','%','&','@','+','-','*','!')
# option = random.choice(options)
# list[g]=option
# # ------------------------------------------------
# def skus():
#     global moznost1,g
#     moznost2 = int(random.randint(0, vstup-1))
#     g=moznost2
#     if moznost2==moznost1:
#         skus()
#     else:  
#         cislo = int(random.randint(0, vstup))
#         list[g]=cislo
# skus()    
   
# # ------------------------------------------------
# clear()
# print(f'Input was: {vstup}')
# print('Your password:')
# print('')
# print("".join(map(str, list)))
# print('')
# print('------------------------------')

# response = requests.get('https://boozeapi.com/api/v1/cocktails')

# if response.status_code==200:
#     data = response.json()
#     print('Nad tatrou sa bliska hromi divo biju')
#     for cocktail in data:
#         name = cocktail.get('name')
#         print(f"Koktejl: {name}")
# else:
#     print('Error:', response.status_code, response.text )


# time.sleep(3)
# clear()


from flask import Flask
url = "https://boozeapi.com/api/v1/cocktails"
response = requests.get(url)
data = response.json()

ingrediencie=[]
drinks = data
meno_drinku = ''
vodka_count = 0
gin_count = 0
rum_count = 0
vodka=False
rum=False
gin=False
adresa=''
adresy=[]
mena=[]
print('Drinky a ich obsah:')

for drink in drinks:
    veci = drinks.get("data", [])
    for vec in veci:
        vodka=False
        rum=False
        gin=False
        meno_drinku = vec.get("name")
        ingredients = vec.get("ingredients", {})
        adresa = vec.get('image',{})
        adresy.append(adresa)
        mena.append(meno_drinku)




        for ingredient in ingredients:
            ingrediencie.append(ingredient['type'])
            if "Vodka" in ingredient['type'] and vodka==False:
                vodka=True
                vodka_count += 1
            if "Gin" in ingredient['type']and gin==False:
                gin=True
                gin_count += 1
            if "Rum" in ingredient['type']and rum==False:
                rum=True
                rum_count += 1

        print(f'{meno_drinku} obsahuje: {", ".join(map(str,ingrediencie))}')
        ingrediencie=[]
        print(adresa)
        

app = Flask(__name__)

@app.route("/")
def hello_world():
    return(f"""
                
                <img src="{adresy[0]}" alt="{mena[0]}" width="100" height="100">
                <p>{mena[0]}</p>
                <img src="{adresy[1]}" alt="{mena[1]}" width="100" height="100">
                <p>{mena[1]}</p>
                <img src="{adresy[2]}" alt="{mena[2]}" width="100" height="100">
                <p>{mena[2]}</p>
                <img src="{adresy[3]}" alt="{mena[3]}" width="100" height="100">
                <p>{mena[3]}</p>
                <img src="{adresy[4]}" alt="{mena[4]}" width="100" height="100">
                <p>{mena[4]}</p>
                <img src="{adresy[5]}" alt="{mena[5]}" width="100" height="100">
                <p>{mena[5]}</p>
                <img src="{adresy[6]}" alt="{mena[6]}" width="100" height="100">
                <p>{mena[6]}</p>
                <img src="{adresy[7]}" alt="{mena[7]}" width="100" height="100">
                <p>{mena[7]}</p>
                <img src="{adresy[8]}" alt="{mena[8]}" width="100" height="100">
                <p>{mena[8]}</p>
                <img src="{adresy[9]}" alt="{mena[9]}" width="100" height="100">
                <p>{mena[9]}</p>
                <img src="{adresy[10]}" alt="{mena[10]}" width="100" height="100">
                <p>{mena[10]}</p>
                <img src="{adresy[11]}" alt="{mena[11]}" width="100" height="100">
                <p>{mena[11]}</p>
                <img src="{adresy[12]}" alt="{mena[12]}" width="100" height="100">
                <p>{mena[12]}</p>
                <img src="{adresy[13]}" alt="{mena[13]}" width="100" height="100">
                <p>{mena[13]}</p>
                <img src="{adresy[14]}" alt="{mena[14]}" width="100" height="100">
                <p>{mena[14]}</p>
                <img src="{adresy[15]}" alt="{mena[15]}" width="100" height="100">
                <p>{mena[15]}</p>
                <img src="{adresy[16]}" alt="{mena[16]}" width="100" height="100">
                <p>{mena[16]}</p>
                <img src="{adresy[17]}" alt="{mena[17]}" width="100" height="100">
                <p>{mena[17]}</p>
                <img src="{adresy[18]}" alt="{mena[18]}" width="100" height="100">
                <p>{mena[18]}</p>
                <img src="{adresy[19]}" alt="{mena[19]}" width="100" height="100">
                <p>{mena[19]}</p>
                <img src="{adresy[20]}" alt="{mena[20]}" width="100" height="100">
                <p>{mena[20]}</p>

                    """)

print('')
print('Pocty alkoholu v drinkoch:')
print("Počet drinkov s vodkou:", vodka_count)
print("Počet drinkov s ginom:", gin_count)
print("Počet drinkov s rumom:", rum_count)
