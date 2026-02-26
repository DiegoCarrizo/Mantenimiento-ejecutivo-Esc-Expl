import streamlit as st

# Configuración básica
st.set_page_config(page_title="Mantenimiento Esc. Expl.", page_icon="🪖")

st.title("🪖 Control de Vehículos - Esc. Expl.")
st.info("Formulario de inspección rápida para salida a zona.")

# Formulario
with st.form("checklist_mantenimiento"):
    st.subheader("Identificación")
    unidad = st.text_input("NI / Matrícula del Vehículo")
    conductor = st.text_input("Grado y Apellido del Conductor")
    
    st.divider()
    
    st.subheader("Verificaciones")
    col1, col2 = st.columns(2)
    
    with col1:
        aceite = st.checkbox("Nivel de Aceite OK")
        agua = st.checkbox("Nivel de Refrigerante OK")
        frenos = st.checkbox("Líquido de Frenos OK")
        
    with col2:
        luces = st.checkbox("Sistema de Luces OK")
        radio = st.checkbox("Comunicaciones OK")
        neumaticos = st.checkbox("Presión de Neumáticos OK")

    novedades = st.text_area("Observaciones / Novedades")
    
    # Botón de envío
    enviar = st.form_submit_button("Registrar Inspección")

if enviar:
    st.success(f"Inspección de la unidad {unidad} registrada correctamente.")
    st.balloons()
