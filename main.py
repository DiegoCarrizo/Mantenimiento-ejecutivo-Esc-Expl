import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Mantenimiento Ejecutivo", layout="wide")

# --- DATOS DEL DOCUMENTO ---
st.title("LISTA DE CONTROL DE MANTENIMIENTO EJECUTIVO")
st.write("ESCUADRÓN DE EXPLORACIÓN DE CABALLERÍA BLINDADO 11")

col1, col2 = st.columns(2)
responsable = col1.text_input("RESPONSABLE", placeholder="Grado y Apellido")
seccion = col2.text_input("SECCIÓN")
fecha = col1.text_input("FECHA DE EJECUCIÓN", value=f"ROSPENTEK (SC), {datetime.now().strftime('%d')} de Febrero de 2026")
comodidad = col2.text_input("GRUPO COMODIDAD")

# --- LISTADO DE ÍTEMS (Extraído del Word) ---
# Agrupamos por categorías para que sea más fácil de llenar
categorias = {
    "VEE HUMMER / UNIMOG / MB": [
        "Engrase de rótulas delanteras", "Aceite de motor", "Filtro de aire", 
        "Control de refrigerante", "Líquidos de freno", "Control de caliper",
        "Control de aceite de caja de velocidades", "Control de aceite caja de transmisión",
        "Control de aceite diferencial trasero", "Control de aceite diferencial delantero",
        "Control de aceite reductores de rueda delantero", "Control de aceite reductores de rueda trasero",
        "Control de aceite bomba hidráulica", "Control de ajuste de puertas delanteras",
        "Control de ajuste de puertas traseras", "Presión de neumáticos",
        "Control de luces de posición", "Control de luz alta y baja",
        "Control de guiño y baliza", "Control relojes de tablero", "Control de batería"
    ],
    "VC SK 105 (Tanque)": [
        "Control de aceite de motor", "Control de aceite de caja de reenvío", "Control de aceite de caja de cambio",
        "Control de caja de engranaje y en dirección", "Control de aceite hidráulico", "Control de combustible",
        "Control de reductor final", "Control de agua y anticongelante", "Control de aceite de rueda tractora",
        "control de rodamientos", "control de brazo tensor", "Control de rueda tensora",
        "Control de rodillo de apoyo", "Control de tensado de correas de bomba de agua",
        "Control de tensado de correa sistema de ventilador", "Control de pastilla de freno",
        "Control de nivel de hidráulico de motor de torre", "Control de niveles del freno de cañón",
        "Control de niveles del recuperador", "Control de molinetes de carga", "Control de atacador",
        "Control de corona dentada", "Control del azimut", "Control de luz de torre",
        "Control del tiro eléctrico", "Control del motor de torre", "Control del extractor de gases",
        "Control del telémetro láser", "Control de faro de puntería", "Control de luz alta y baja",
        "Control de luz de guiño y baliza", "Control de luces de combate", "Control de estado de baterías",
        "Control de ácido de baterías", "Control de fuelle de torre", "Control de engrase de cardans",
        "Control de filtros de aire", "Control de pre filtro de combustible"
    ],
    "MOTOCICLETA ROYAL ENFIELD": [
        "Control de aceite de motor", "Control de aceite de frenos", "Control de embrague",
        "Control de discos de frenos", "Control de luces alta y baja", "Control de sensores",
        "Control de relojería tablero analógico- digital", "Control de tensado de cadena",
        "Control de cable acelerador", "Control de sistema de amortiguación"
    ],
    "EQUIPOS DE COMUNICACIONES": [
        "Control de conectores y terminales", "Control de lubricación de conectores y terminales",
        "Control de extremos de antenas y soportes", "Control de sistema de conexión",
        "Control de cables de alimentación de VRC", "Control de cable Cx VRC",
        "Ajuste de la base de radio", "Control de encendido y apagado",
        "Control de testeo digital HARRIS y ELBIT", "Control digital de baterías HARRIS y ELBIT",
        "Control microteléfono, auricular y PTT", "Ajuste de sintonizador de VRC",
        "Controlar antena 7 tramos HARRIS", "Controlar Base de antena de HARRIS"
    ]
}


resultados = {}

for cat, items in categorias.items():
    st.header(cat)
    for item in items:
        c1, c2, c3, c4 = st.columns([4, 1, 1, 4])
        c1.write(item)
        si = c2.checkbox("SÍ", key=f"si_{item}")
        no = c3.checkbox("NO", key=f"no_{item}")
        obs = c4.text_input("Obs", key=f"obs_{item}")
        resultados[item] = {"SI": "X" if si else "", "NO": "X" if no else "", "OBS": obs}

st.markdown("---")
obs_final = st.text_area("OBSERVACIONES DEL ESPECIALISTA / SOLICITUDES AL ESCALÓN SUPERIOR")

# --- FUNCIÓN DE IMPRESIÓN MEJORADA ---
# Creamos un bloque de HTML que contiene SOLO la información relevante para imprimir
if st.button("🖨️ GENERAR VISTA DE IMPRESIÓN"):
    # Construimos una tabla HTML para que el navegador la entienda
    html_report = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; }}
            table {{ width: 100%; border-collapse: collapse; }}
            th, td {{ border: 1px solid black; padding: 8px; text-align: left; }}
            h2 {{ text-align: center; }}
        </style>
    </head>
    <body>
        <h2>LISTA DE CONTROL MANTENIMIENTO EJECUTIVO</h2>
        <p><b>Responsable:</b> {responsable} | <b>Sección:</b> {seccion}</p>
        <p><b>Fecha:</b> {fecha} | <b>Grupo Comodidad:</b> {comodidad}</p>
        <table>
            <tr><th>Aspecto a Controlar</th><th>SÍ</th><th>NO</th><th>Observaciones</th></tr>
    """
    for item, datos in resultados.items():
        html_report += f"<tr><td>{item}</td><td>{datos['SI']}</td><td>{datos['NO']}</td><td>{datos['OBS']}</td></tr>"
    
    html_report += f"""
        </table>
        <p><b>Observaciones Specialist:</b> {obs_final}</p>
        <br><br>
        <div style="display: flex; justify-content: space-between;">
            <p>____________________<br>J SEC</p>
            <p>____________________<br>ESPECIALISTA</p>
            <p>____________________<br>J SEC CDO Y SER</p>
        </div>
        <script>window.print();</script>
    </body>
    </html>
    """
    st.components.v1.html(html_report, height=600, scrolling=True)
