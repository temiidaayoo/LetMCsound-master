import mysql.connector
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from fpdf import FPDF
import os
import io
import datetime
import uuid

app = Flask(__name__)
CORS(app)

# --- 1. CONFIGURACIÓN ---
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password', 
    'port': 3307,
    'database': 'LetMCsoundDB'
}
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)
def inicializar_bd():
    # 1. Crear base de datos sin seleccionar ninguna
    conn = mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        port=DB_CONFIG['port']
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS LetMCsoundDB")
    cursor.close()
    conn.close()

    # 2. Crear tablas dentro de la base ya creada
    conn = mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        port=DB_CONFIG['port'],
        database="LetMCsoundDB"
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255),
            password VARCHAR(255)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_venta VARCHAR(50),
            comprador VARCHAR(255),
            titulo_beat VARCHAR(255),
            precio FLOAT,
            licencia VARCHAR(50)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    
def obtener_ruta_base():
    return os.path.dirname(os.path.abspath(__file__))

# --- 2. FUNCIÓN DE LIMPIEZA DE TEXTO (Para evitar errores con €) ---
def limpiar_texto(texto):
    reemplazos = {
        "\u20ac": "EUR",    # Euro
        "\u2018": "'", "\u2019": "'", # Comillas simples
        "\u201c": '"', "\u201d": '"', # Comillas dobles
        "\u2013": "-", "\u2014": "-", # Guiones
        "ñ": "n", "Ñ": "N"
    }
    for original, nuevo in reemplazos.items():
        texto = texto.replace(original, nuevo)
    return texto.encode('latin-1', 'replace').decode('latin-1')

# --- 3. GENERADOR DE PDF (Con búsqueda inteligente de logo) ---
def generar_pdf_contrato(datos_venta):
    try:
        base_dir = obtener_ruta_base()
        
        # Procesar plantilla
        tipo_licencia = datos_venta.get('licencia', 'standard').lower().strip()
        nombre_archivo = f"{tipo_licencia}.txt"
        ruta_plantilla = os.path.join(base_dir, "plantillas_txt", nombre_archivo)
        
        print(f"🔍 Procesando plantilla: {nombre_archivo}")

        # Leer contenido
        contenido_texto = ""
        if os.path.exists(ruta_plantilla):
            with open(ruta_plantilla, "r", encoding="utf-8", errors="ignore") as f:
                contenido_texto = f.read()
        else:
            print(f"❌ ARCHIVO NO ENCONTRADO: {ruta_plantilla}")
            contenido_texto = f"CONTRATO {tipo_licencia.upper()} (Plantilla no encontrada)"

        # Rellenar datos
        contenido_texto = contenido_texto.replace("{COMPRADOR}", datos_venta.get('comprador', 'Cliente'))
        contenido_texto = contenido_texto.replace("{TITULO}", datos_venta.get('titulo', 'Beat'))
        contenido_texto = contenido_texto.replace("{PRECIO}", str(datos_venta.get('precio', '0.00')))
        contenido_texto = contenido_texto.replace("{ID_VENTA}", datos_venta.get('id_venta', '0000'))
        contenido_texto = contenido_texto.replace("{FECHA}", str(datetime.datetime.now().strftime("%Y-%m-%d")))

        # Limpiar caracteres prohibidos
        contenido_final = limpiar_texto(contenido_texto)

        # --- CREAR PDF ---
        pdf = FPDF()
        pdf.add_page()
        
        # >>> AQUÍ ESTÁ LA CORRECCIÓN DEL LOGO <<<
        # Busca varios nombres posibles por si acaso
        posibles_logos = ["letmc.png", "letmc.jpg", "logo.png", "logo.jpg"]
        logo_encontrado = None
        
        for nombre_logo in posibles_logos:
            ruta_prueba = os.path.join(base_dir, nombre_logo)
            if os.path.exists(ruta_prueba):
                logo_encontrado = ruta_prueba
                break
        
        if logo_encontrado:
            print(f"✅ Logo encontrado en: {logo_encontrado}")
            # x=10, y=8 son las coordenadas, w=33 es el tamaño
            pdf.image(logo_encontrado, x=10, y=8, w=33) 
        else:
            print(f"⚠️ AVISO: No se encontró 'letmc.png' ni 'logo.png' en {base_dir}")

        pdf.ln(40) 
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, f"Licencia {tipo_licencia.capitalize()}", ln=True, align='C')
        pdf.ln(10)

        pdf.set_font("Arial", size=11)
        pdf.multi_cell(0, 7, contenido_final)
        
        pdf_bytes = pdf.output(dest='S').encode('latin-1', 'replace')
        return io.BytesIO(pdf_bytes), None

    except Exception as e:
        print(f"🔥 Error generando PDF: {e}")
        return None, str(e)

# --- 4. RUTAS ---
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (nombre, password) VALUES (%s, %s)"
        cursor.execute(sql, (data.get('username'), data.get('password')))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"success": True, "message": "Registrado"}), 201
    except Exception:
        return jsonify({"success": False, "message": "Error registro"}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM usuarios WHERE nombre = %s AND password = %s"
        cursor.execute(sql, (data.get('username'), data.get('password')))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user: return jsonify({"success": True, "user": user}), 200
        return jsonify({"success": False}), 401
    except Exception: return jsonify({"success": False}), 500

@app.route('/comprar', methods=['POST'])
def comprar():
    try:
        data = request.json
        id_venta = str(uuid.uuid4())[:8]
        datos_venta = {
            'id_venta': id_venta,
            'titulo': data.get('titulo', 'Beat'),
            'precio': data.get('precio', 0),
            'licencia': data.get('licencia', 'Standard'), 
            'comprador': data.get('usuario', 'Invitado')
        }

        # Guardar BD
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            sql = "INSERT INTO ventas (id_venta, comprador, titulo_beat, precio, licencia) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (id_venta, datos_venta['comprador'], datos_venta['titulo'], datos_venta['precio'], datos_venta['licencia']))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Error BD: {e}")

        # Generar PDF
        pdf_buffer, error = generar_pdf_contrato(datos_venta)
        if error: return jsonify({"success": False, "message": error}), 500

        return send_file(
            pdf_buffer,
            as_attachment=True,
            download_name=f"Contrato_{datos_venta['licencia']}_{id_venta}.pdf",
            mimetype='application/pdf'
        )
    except Exception as e:
        print(f"Error General: {e}")
        return jsonify({"success": False, "message": "Error servidor"}), 500

if __name__ == '__main__':
    inicializar_bd()
    app.run(debug=True, port=5000)