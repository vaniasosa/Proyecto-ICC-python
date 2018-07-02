print("CAJERO AUTOMÁTICO")
print("-----------------------")
print("¿Que transacción desea realizar?")
print("1.Crear una cuenta")
print("2.Retiro")
print("3.Deposito")
print("4.Estado de Cuenta")
print("5.Salir")
print("-----------------------")
opc = int(input("Elija opción="))
if opc==1 :
    print("Creando Cuenta")
    print("¿Desea crear otra cuenta?(S/N)")
    res = input("ingrese respuesta=")
    while  True :
        if res == si :
            
        
        else :
            print("regresando al sistema incial")
            break
elif opc==2 :
    print("ingrese DNI = ")
    print("ingrese clave=")
    print("MONTO A RETIRAR=")
    print("1. 20 soles")
    print("2. 50 soles")
    print("3. 100 soles")
    print("4. 200 soles")
    print("5. 500 soles")
    print("6. OTRO MONTO")
    opc1 = int(input("Elija opcion de monto a retirar="))
    if opc1==1:
        print("retirando 20 soles...")
    elif opc1==2 :
        print("retirando 50 soles...")
    elif opc1==3:
        print("retirando 100 soles...")
    elif opc1==4:
        print("retirando 200 soles...")
    elif opc1==5:
        print("retirando 500 soles...")
    elif opc1==6:
        mretiro=int(input("ingrese monto a retirar="))
        print("retirando","",mretiro,"","soles")
elif opc==3:
    dnideposito=int(input("INGRESE DNI DE PERSONA A DEPOSITAR="))
    mdeposito=int(input("INGRESE MONTO A DEPOSITAR="))
    print("usted a depositado","",mdeposito,"","soles a la cuenta de DNI","",dnideposito)
elif opc==4:
    y
elif opc==5:
    print("saliendo del sistema")
    print("BYEEEE.......")

    

