def menu():
    print ("MENU")
    print("""    1. Registrar trabajador
    2. Listar todos los trabajadores
    3. Imprimir planilla de sueldos
    4. Salir del programa""")
    opc = int(input("ingresar una opción: "))
    return opc

def limpiar_pantalla():
    import os
    os.system("clear")

def esperar():
    import time
    time.sleep(2)
def descuento_salud(p_sueldo):
    dec = p_sueldo * 0.07
    return dec

def descuento_afp(p_sueldo):
    dec = p_sueldo * 0.12
    return dec

def validacion_opc(opc):
    while True:
        if opc == 1:
            break
        elif opc == 2:
            break
        elif opc == 3:
            break
        elif opc == 4:
            break
        else:
            print("Error Valor no valido¡¡")