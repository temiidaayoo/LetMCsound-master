import mysql.connector

def probar_conexion(puerto):
    print(f"Probando conexión al puerto {puerto}...")
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='root', # O prueba con comillas vacías '' si falla
            port=puerto
        )
        if conn.is_connected():
            print(f"¡ÉXITO! MySQL está corriendo en el puerto {puerto}")
            conn.close()
            return True
    except Exception as e:
        print(f"Fallo en puerto {puerto}: {e}")
        return False

# Probamos los dos puertos más comunes
if not probar_conexion(3007):
    print("---")
    probar_conexion(3306)