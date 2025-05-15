import PIA_modulo as PIA
import os

def main():
    PIA.registrar()
    while True:
        os.system("clear") 
        try:
            print("\tMENU PRINCIPAL")
            print("-" * 32)
            print(
                "Selecciona una opcion:\n1- Verificar dominios maliciosos\n2- Verificar links de Google maliciosos\n3- Importar datos desde la API\n4- Verificar datos acerca de (Url,domain,etc)\n5- Indicadores maliciosos iOs\n6-Salir"
            )
            print("-" * 32)
            opcion = int(input("\nOpcion: "))
            if opcion == 1:
                verificar_dominio()
            elif opcion == 2:
                verificar_link_google()
            elif opcion == 3:
                importar_datos()
            elif opcion == 4:
                verificar_malware()
            elif opcion == 5:
                verificar_datosiOs()
            elif opcion == 6:
                print("Gracias por usar el sistema. ¡Hasta luego!")
                PIA.registrar()
            else:
                input("Opción no válida")
        except:
            input("Debes ingresar un número")

def verificar_malware():
    os.system("clear")
    archivo_txt = "malware.txt"
    datos = PIA.cargar_datos_txt(archivo_txt)

    if datos:
        for dominio in datos:
            print(f"Tipo: {dominio['type']}, Dominio: {dominio['indicator']}")
    else:
        print("No se encontraron dominios maliciosos en el archivo TXT.")

    grafica = input("¿Desea ver la gráfica de frecuencia? (S/N): ")
    if grafica.lower() == "s":
        PIA.grafica_malware()
        input("\nPresiona ENTER para continuar...")

def verificar_dominio():
    os.system("clear")
    archivo_txt = "dominios_maliciosos.txt"
    datos = PIA.cargar_datos_txt(archivo_txt)

    if datos:
        for dominio in datos:
            print(f"Tipo: {dominio['type']}, Dominio: {dominio['indicator']}")
    else:
        print("No se encontraron dominios maliciosos en el archivo TXT.")

    grafica = input("¿Desea ver la gráfica de frecuencia? (S/N): ")
    if grafica.lower() == "s":
        PIA.graficar_dominios_maliciosos()
        input("\nPresiona ENTER para continuar...")
        

def verificar_link_google():
    os.system("clear")
    archivo_txt = "google_links_maliciosos.txt"
    datos = PIA.cargar_datos_txt(archivo_txt)

    if datos:
        for link in datos:
            print(f"Tipo: {link['type']}, Link: {link['indicator']}")
    else:
        print("No se encontraron links maliciosos en el archivo TXT.")

    grafica = input("¿Desea ver la gráfica de frecuencia? (S/N): ")
    if grafica.lower() == "s":
        PIA.graficar_links_maliciosos()
        input("\nPresiona ENTER para continuar...")

def verificar_datosiOs():
    os.system("clear")
    archivo_txt = "iOs_maliciosos.txt"
    datos = PIA.cargar_datos_txt(archivo_txt)
    
    if datos:
        for link in datos:
            print(f"Tipo: {link['type']}, Link: {link['indicator']}")
    else:
        print("No se encontraron datos maliciosos en el TXT.")
    grafica = input("¿Desea ver la gráfica de frecuencia? (S/N): ")
    if grafica.lower() == "s":
        PIA.graficaiOs()
        input("\nPresiona ENTER para continuar...")

def importar_datos():
    os.system("clear")
    if not PIA.hay_conexion():
        print("No hay conexión a internet. No se pueden importar datos.")
        return

    try:
        limite = int(input("¿Cuántos indicadores desea importar por tipo? "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    # Pulse ID de dominios maliciosos
    pulse_dominios = "5dad761b5597a507ee5c1c66"
    indicadores_dominios = PIA.obtener_indicadores_otx(pulse_dominios, limite)
    if indicadores_dominios:
        PIA.guardar_datos_txt(indicadores_dominios, "dominios_maliciosos.txt")

    # Pulse ID de links de Google maliciosos
    pulse_links = "6213f2c919cb371e8d38bae5"
    indicadores_links = PIA.obtener_indicadores_otx(pulse_links, limite)
    if indicadores_links:
        PIA.guardar_datos_txt(indicadores_links, "google_links_maliciosos.txt")

    pulse_iOs="67f5555b6ce863d998e83e26"
    indicadores_iOs=PIA.obtener_indicadores_otx(pulse_iOs,limite)
    if indicadores_iOs:
        PIA.guardar_datos_txt(indicadores_iOs,"iOs_maliciosos.txt")
    
    pulse_malware="681407e55a4e4fb5dcfa96bc"
    indicadores_malware=PIA.obtener_indicadores_otx(pulse_malware,limite)
    if indicadores_malware:
        PIA.guardar_datos_txt(indicadores_malware,"malware.txt")
    print("Importacion completada")


if __name__ == "__main__":
    main()
