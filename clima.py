mes=int(input("digite el numero segun corresponda al mes \n "
               "1 ->enero \n"
               "2 ->febrero \n"
               "3 ->marzo \n"
               "4 ->abril \n"
               "5 ->mayo \n"
               "6 ->junio \n"
               "7 ->julio \n"
               "8 ->agosto\n"
               "9 ->septiembre \n"
               "10 ->octubre \n"
               "11 -noviembre \n"
               "12 ->diciembre \n"
))

if  mes>0 and mes<=3:
    print("invierno")
elif mes==4 or mes==6:
    print ("Equinoccio de primavera que inicia en 20 de marzo 21 de junio")
elif mes==7 or mes==9:
    print ("Solsticio de verano (21 de junio) - Equinoccio de otoño (23 de septiembre)")
elif mes==10 or mes==12:
    print("Equinoccio de otoño (23 de septiembre) - Solsticio de invierno (22 de diciembre)")
else:
    print("dato erroneo")