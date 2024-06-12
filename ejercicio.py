from funciones import *
desc_salud = 0.07
desc_afp = 0.12
trabajadores = []
opc=0
while True:
    limpiar_pantalla()
    opc = menu()
    validacion_opc(opc)
    if opc == 1:
        limpiar_pantalla()
        nombre = input("Ingresar nombre del trabajador: ")
        limpiar_pantalla()
        apellido = input("Ingresar apellido: ")
        limpiar_pantalla()
        cargo = input("Ingresar cargo del trabajadr: ")
        limpiar_pantalla()
        sueldo = int(input("Ingresar sueldo bruto: "))

        trabajador = {"nombre": nombre, "apellido": apellido, "cargo": cargo, "sueldo": sueldo}
        trabajadores.append(trabajador)
    elif opc == 2:
        for x in range(len(trabajadores)):
            nombre = trabajadores[x]
            print(nombre)
            esperar()
    elif opc == 3:
        for x in range(len(trabajadores)):
            pass
    else:
        print("Adios¡¡")
        break