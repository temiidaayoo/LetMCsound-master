import os

print("--- DIAGNÓSTICO DE ARCHIVOS ---")
ruta_actual = os.getcwd()
print(f"1. Python se está ejecutando desde: {ruta_actual}")

carpeta_plantillas = os.path.join(ruta_actual, "plantillas_txt")
print(f"2. Buscando carpeta de plantillas en: {carpeta_plantillas}")

if os.path.exists(carpeta_plantillas):
    print("   ✅ La carpeta 'plantillas_txt' EXISTE.")
    archivos = os.listdir(carpeta_plantillas)
    print(f"   📂 Archivos encontrados dentro: {archivos}")
    
    if "standard.txt" in archivos:
        print("   ✅ ¡El archivo 'standard.txt' fue encontrado correctamente!")
    else:
        print("   ❌ ERROR: No veo 'standard.txt'. Revisa los nombres listados arriba.")
        if "standard.txt.txt" in archivos:
            print("      ⚠️ DETECTADO ERROR DE DOBLE EXTENSIÓN: Tienes 'standard.txt.txt'")
else:
    print("   ❌ ERROR: La carpeta 'plantillas_txt' NO EXISTE en esta ruta.")

print("-------------------------------")
input("Presiona Enter para salir...")