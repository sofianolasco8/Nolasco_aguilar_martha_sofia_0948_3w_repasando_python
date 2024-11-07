print(" ")
print("nolasco_aguilar_martha_sofia_0948_3w")
print(" ")
nota=int(input("ingresa la nota "))#indica al usuario ingresar su nota 
if nota <= 0 or nota > 5:#indica si la nota es menor o igual a cero pero mayor a 5 
    print("suspenso")#indica el mensaje que se va a mostrar 
else:
    nota >= 5 or nota < 6#indica si la nota es menor o igual a 5 pero mayor a 6 
    print("suficiente ")#indica el mensaje que se va a mostrar 
if nota >= 6 or nota < 7:#indica si la nota es menor o igual a 6 pero mayor a 7 
    print("BIEN")#indica el mensaje que se va a mostrar 
else:
    nota >=7 or nota < 9#indica si la nota es mayor o igual a 7 pero menor a 9 
    print("NOTABLE ")#indica el mensaje que se va a mostrar 
if nota > 9 or nota <=10:#indica si la nota es mayor a 9 o mayor o igual a 10
    print("SOBRESALIENTE")
else:
    print(" nota no valida")#se imprime mensaje de que la nota no es valida 
