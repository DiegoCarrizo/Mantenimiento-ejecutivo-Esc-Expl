import streamlit as st

st.title("🪖 Control de Vehículos - Esc. Expl.")

st.sidebar.header("Datos de la Unidad")
vehiculo = st.sidebar.selectbox("Vehículo", ["Humvee", "Gaucho", "MB 1720"])
patente = st.sidebar.text_input("NI / Matrícula")

st.header("📋 Checklist de Mantenimiento")

# Secciones del Checklist
aceite = st.radio("Nivel de Aceite", ["OK", "Bajo", "Crítico"], horizontal=True)
luces = st.checkbox("Luces de Marcha Operativas")
frenos = st.select_slider("Estado de Frenos", options=["Malo", "Regular", "Bueno"])
novedades = st.text_area("Novedades detectadas")

if st.button("Registrar Mantenimiento"):
    st.success(f"Registro guardado para la unidad {patente}")
    st.balloons()
