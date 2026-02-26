import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de página
st.set_page_config(page_title="Mantenimiento Ejecutivo - Esc Expl", layout="wide")

# --- BASE DE DATOS DE ASPECTOS A CONTROLAR ---
# Extraído de la Lista de Control de Mantenimiento Ejecutivo [cite: 1, 6]
DATA_CHECKLIST = {
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

st.title("📋 Mantenimiento Ejecutivo - Rospentek")
st.write("Escuadrón de Exploración de Caballería Blindado 11")

# --- ENCABEZADO ---
with st.expander("Datos del Responsable y Unidad", expanded=True):
    col1, col2 = st.columns(2)
    responsable = col1.text_input("Responsable (Grado y Apellido) [cite: 2]")
    seccion = col2.text_input("Sección [cite: 3]")
    tipo_v = st.selectbox("Categoría de Vehículo/Equipo", list(DATA_CHECKLIST.keys()))
    comodidad = st.text_input("Grupo Comodidad [cite: 5]")
    fecha_hoy = datetime.now().strftime('%d/%m/%Y')

# --- CUERPO DEL CHECKLIST ---
st.subheader(f"Aspectos a controlar: {tipo_v}")
items = DATA_CHECKLIST[tipo_v]
respuestas = []

for i, item in enumerate(items):
    col_t, col_s, col_n, col_o = st.columns([4, 1, 1, 3])
    col_t.write(f"**{item}**")
    # Se añade i a la key para evitar duplicados si el texto del item se repite
    si = col_s.checkbox("Sí", key=f"si_{tipo_v}_{i}")
    no = col_n.checkbox("No", key=f"no_{tipo_v}_{i}")
    obs = col_o.text_input("Obs", key=f"obs_{tipo_v}_{i}", placeholder="Observaciones...")
    respuestas.append({"Aspecto": item, "Sí": "X" if si else "", "No": "X" if no else "", "Observaciones": obs})

# --- OBSERVACIONES FINALES ---
st.divider()
obs_especialista = st.text_area("OBSERVACIONES DEL ESPECIALISTA / SOLICITUDES AL ESCALÓN SUPERIOR")

# --- BOTÓN DE IMPRESIÓN / REPORTE VISUAL ---
if st.button("🖨️ Generar Reporte para Imprimir / PDF"):
    # Construcción del reporte en HTML para la función de impresión del navegador
    html_report = f"""
    <div style="font-family: 'Arial'; padding: 30px; border: 1px solid #000;">
        <h2 style="text-align: center;">LISTA DE CONTROL DE MANTENIMIENTO EJECUTIVO</h2>
        <p><b>UNIDAD:</b> Escuadrón de Exploración de Caballería Blindado 11</p>
        <p><b>RESPONSABLE:</b> {responsable} &nbsp;&nbsp;&nbsp; <b>SECCIÓN:</b> {seccion}</p>
        <p><b>FECHA:</b> {fecha_hoy} &nbsp;&nbsp;&nbsp; <b>GRUPO COMODIDAD:</b> {comodidad}</p>
        <hr>
        <h3>Vehículo/Equipo: {tipo_v}</h3>
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background-color: #f2f2f2;">
                    <th style="border: 1px solid black; padding: 8px;">Aspecto a Controlar</th>
                    <th style="border: 1px solid black; padding: 8px; width: 40px;">SÍ</th>
                    <th style="border: 1px solid black; padding: 8px; width: 40px;">NO</th>
                    <th style="border: 1px solid black; padding: 8px;">Observaciones</th>
                </tr>
            </thead>
            <tbody>
    """
    for r in respuestas:
        html_report += f"""
                <tr>
                    <td style="border: 1px solid black; padding: 8px;">{r['Aspecto']}</td>
                    <td style="border: 1px solid black; text-align: center;">{r['Sí']}</td>
                    <td style="border: 1px solid black; text-align: center;">{r['No']}</td>
                    <td style="border: 1px solid black; padding: 8px;">{r['Observaciones']}</td>
                </tr>
        """
    
    html_report += f"""
            </tbody>
        </table>
        <p><b>OBSERVACIONES DEL ESPECIALISTA:</b> {obs_especialista}</p>
        <br><br>
        <div style="display: flex; justify-content: space-around; text-align: center;">
            <div>____________________<br>J SEC [cite: 9]</div>
            <div>____________________<br>Especialista [cite: 11]</div>
            <div>____________________<br>J Sec Cdo y Ser [cite: 15]</div>
        </div>
    </div>
    <script>window.print();</script>
    """
    st.components.v1.html(html_report, height=800, scrolling=True)
