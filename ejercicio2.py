nombreusuario=input("ingrese su nombre")
edad=int(input("digite su edad"))

if edad>=0 and edad <=15:
    print(f"no{nombreusuario},es niño")
elif  edad>15 and edad<=28:
        print(f"{nombreusuario},es joven")
elif edad>28 and edad<=60:
      print(f"{nombreusuario},es adulto")
elif edad>60 and edad <110:
      print(f"{nombreusuario},es adulto mayor")
else:
      print("edad invalidad")
      