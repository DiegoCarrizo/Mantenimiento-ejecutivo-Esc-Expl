import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Mantenimiento Ejecutivo - Esc Expl", layout="wide")

# --- BASE DE DATOS DE ASPECTOS A CONTROLAR ---
# Extraído de la Lista de Control de Mantenimiento Ejecutivo
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
    responsable = col1.text_input("Responsable (Grado y Apellido)")
    seccion = col2.text_input("Sección")
    tipo_v = st.selectbox("Categoría de Vehículo/Equipo", list(DATA_CHECKLIST.keys()))
    comodidad = st.text_input("Grupo Comodidad")

# --- CUERPO DEL CHECKLIST ---
st.subheader(f"Aspectos a controlar: {tipo_v}")
items = DATA_CHECKLIST[tipo_v]
respuestas = []

for item in items:
    col_t, col_s, col_n, col_o = st.columns([4, 1, 1, 3])
    col_t.write(f"**{item}**")
    si = col_s.checkbox("Sí", key=f"si_{item}")
    no = col_n.checkbox("No", key=f"no_{item}")
    obs = col_o.text_input("Obs", key=f"obs_{item}", placeholder="Observaciones...")
    respuestas.append({"Aspecto": item, "Sí": "X" if si else "", "No": "X" if no else "", "Observaciones": obs})

# --- OBSERVACIONES FINALES ---
st.divider()
obs_especialista = st.text_area("OBSERVACIONES DEL ESPECIALISTA / SOLICITUDES AL ESCALÓN SUPERIOR")

# --- GENERAR EXCEL ---
if st.button("Preparar Planilla Excel"):
    df = pd.DataFrame(respuestas)
    # Agregar metadatos al final
    df.loc[len(df)] = ["---", "---", "---", "---"]
    df.loc[len(df)] = ["Responsable:", responsable, "Sección:", seccion]
    df.loc[len(df)] = ["Obs. Especialista:", obs_especialista, "", ""]
    
    # Crear archivo en memoria
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Checklist')
    
    st.download_button(
        label="📥 Descargar Excel para Archivo",
        data=output.getvalue(),
        file_name=f"Checklist_{tipo_v}_{seccion}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
