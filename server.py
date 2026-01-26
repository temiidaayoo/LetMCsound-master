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

# --- CONFIGURACIÓN BASE DE DATOS ---
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root', 
    'port': 3307,          # Tu puerto (según tu config.py)
    'database': 'LetMCsound-DB'
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# --- FUNCIÓN GENERAR PDF ---
def generar_pdf_contrato(datos_venta):
    # 1. Determinar ruta del archivo
    tipo_licencia = datos_venta['licencia'].lower() # standard, premium, exclusiva
    
    # AQUI ESTA EL CAMBIO: Buscamos dentro de la carpeta 'plantillas_txt'
    nombre_archivo = f"{tipo_licencia}.txt"
    ruta_plantilla = os.path.join("plantillas_txt", nombre_archivo)
    
    # 2. Leer la plantilla
    try:
        if os.path.exists(ruta_plantilla):
            with open(ruta_plantilla, "r", encoding="utf-8") as f:
                template = f.read()
        else:
            return None, f"Error: No se encuentra la plantilla en {ruta_plantilla}"
    except Exception as e:
        return None, f"Error leyendo plantilla: {str(e)}"

    # 3. Rellenar datos
    try:
        texto_contrato = template.format(
            id_venta=datos_venta['id_venta'],
            fecha=datetime.datetime.now().strftime("%Y-%m-%d"),
            prod_legal="KairoWave (Productor)",
            prod_dni="X-000000",
            cli_legal=datos_venta['comprador'],
            cli_dni="PENDIENTE", 
            titulo_obra=datos_venta['titulo'],
            precio=datos_venta['precio'],
            comision=round(float(datos_venta['precio']) * 0.10, 2)
        )
    except KeyError as e:
        return None, f"Error en el formato de la plantilla: falta el campo {str(e)}"

    # 4. Crear PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Título
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt=f"CONTRATO {tipo_licencia.upper()} - LetMC Sound", ln=1, align="C")
    pdf.ln(10)
    
    # Cuerpo
    pdf.set_font("Arial", size=11)
    # Codificar a latin-1 para tildes y caracteres especiales
    texto_seguro = texto_contrato.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 8, txt=texto_seguro)
    
    # Guardar en memoria (buffer)
    buffer = io.BytesIO()
    pdf_output = pdf.output(dest='S').encode('latin-1')
    buffer.write(pdf_output)
    buffer.seek(0)
    
    return buffer, None

# --- RUTAS DE LA API ---

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            return jsonify({"success": True, "message": "Bienvenido"}), 200
        else:
            return jsonify({"success": False, "message": "Credenciales incorrectas"}), 401
    except Exception as e:
        print(f"Error Login: {e}")
        return jsonify({"success": False, "message": "Error de servidor"}), 500

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            cursor.close()
            conn.close()
            return jsonify({"success": False, "message": "El usuario ya existe"}), 400

        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"success": True, "message": "Usuario registrado"}), 201
    except Exception as e:
        print(f"Error Registro: {e}")
        return jsonify({"success": False, "message": "Error de servidor"}), 500

@app.route('/comprar', methods=['POST'])
def comprar():
    try:
        data = request.json
        
        id_venta = str(uuid.uuid4())[:8]
        
        datos_venta = {
            'id_venta': id_venta,
            'titulo': data.get('titulo'),
            'precio': data.get('precio'),
            'licencia': data.get('licencia'), 
            'comprador': data.get('usuario')
        }

        # Generamos el PDF
        pdf_buffer, error = generar_pdf_contrato(datos_venta)
        
        if error:
            print(f"Error PDF: {error}")
            return jsonify({"success": False, "message": error}), 500

        nombre_archivo = f"Contrato_{datos_venta['licencia']}_{id_venta}.pdf"
        
        # Enviamos el archivo al navegador
        return send_file(
            pdf_buffer,
            as_attachment=True,
            download_name=nombre_archivo,
            mimetype='application/pdf'
        )
    except Exception as e:
        print(f"Error Compra: {e}")
        return jsonify({"success": False, "message": "Error procesando compra"}), 500

if __name__ == '__main__':
    print("Servidor corriendo en puerto 5000...")
    app.run(debug=True, port=5000)