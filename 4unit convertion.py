#Start

print(
"""\n
       #########################
      # CONVERTION-CALCULATORS #
      #########################
	""")

#In this program, "_" means "to" eg. "km_mi" is kilometres to miles

#starting if statement chain
def mi_km():
    mile = int(input("\nEnter Mile: "))
    print(mile*1.6, "kilometers")
def km_mi():
    km= int(input("\nEnter Kilometer: "))
    print(km/1.6, "mile")

def kg_vis():
    kg = float(input("\nEnter Kilogm: "))
    print(kg*.6, "Viss")
def vis_kg():
    vis= float(input("\nEnter Viss: "))
    print(vis/.6, "Kilogm")

def f_c():
    fah=int(input("\nEnter Temperature in °F: "))
    celsius = (fah-32)/1.8
    print("Temperature in °C = ", celsius)
def c_f():
    cel = int(input("\nEnter Temperature in °C: ")) 
    fahrenheit = (cel*1.8)+32
    print("Temperature in °F = ", fahrenheit)

def kw_hp():
    kw = float(input("\nEnter Kilowatt: "))
    hp = (kw/0.746)
    print("HosePower = ", hp)
    
def hp_kw():
    hp = float(input("\nEnter HosePower: "))
    kw = (hp*0.746)
    print("KiloWatt = ", kw)


    
    
 #creates startup menu
menu_type=("""
	1: Length
	2: Weight
	3: Temperature
	4: Power
	""")


 #choose which what to convert
print(menu_type)
measure=int(input("\nPlease select number:"))

#starting if statement chain

if measure==1:
     #menu to chose from either mile to kilometer or vice-versa
    print("\n 1: Mile to Kilometer")
    print(" 2: Kilometer to Mile\n")
    choice=int(input("Choose number: "))
     #If 1 is chosen follows by asking what metric distance to convert
    if choice== 1:
        print=(mi_km())
    
    elif choice== 2:
        print=(km_mi())
       
    else:
        print("Invalid Entry")
        


if measure==2:
     #menu to chose from either F to C or vice-versa
    print("\n 1: Kilogm to Viss")
    print(" 2: Viss to Kilogm\n")
    choice=int(input("Choose number: "))
     #If 1 is chosen follows by asking what metric distance to convert
    if choice== 1:
        print=(kg_vis())
    
    elif choice== 2:
        print=(vis_kg())
       
    else:
        print("Invalid Entry")
        

if measure==3:
     #menu to chose from either F to C or vice-versa
    print("\n 1: °F to °C")
    print(" 2: °C to °F\n")
    choice=int(input("Choose number: "))
     #If 1 is chosen follows by asking what metric distance to convert
    if choice== 1:
        print=(f_c())
    
    elif choice== 2:
        print=(c_f())
       
    else:
        print("Invalid Entry")
        
if measure==4:
     #menu to chose from either F to C or vice-versa
    print("\n 1: KiloWatt to HosePower")
    print(" 2: HosePower to KiloWatt\n")
    choice=int(input("Choose number: "))
     #If 1 is chosen follows by asking what metric distance to convert
    if choice== 1:
        print=(kw_hp())
    
    elif choice== 2:
        print=(hp_kw())
       
    else:
        print("Invalid Entry")


#Done by shwethwar in 18/4/19 at 4:53pm
#Reference https://codereview.stackexchange.com/questions/66923/conversions-calculator        
#Thanks Sir AungWinHtut       
