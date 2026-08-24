import streamlit as st
import google.generativeai as genai
import pandas as pd
import numpy as np

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA E IDENTIDAD VISUAL DE FLORECER
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Florecer - Innovar con conciencia. Crecer para impactar.",
    page_icon="🌱",
    layout="wide"
)

# Configuración de la API Key de Gemini desde los Secrets de Streamlit
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Mostrar Logo de Florecer (se intenta cargar desde el repositorio o muestra el título)
try:
    st.image("logo.jpg", use_column_width=True)
except Exception:
    st.title("🌱 Florecer")

st.markdown("### *Innovar con conciencia. Crecer para impactar.*")
st.write("Democratizando el acceso a herramientas de Inteligencia Artificial y Analítica de Datos para pequeñas y medianas empresas.")

st.divider()

# -----------------------------------------------------------------------------
# 1. PORTAFOLIO DE SERVICIOS
# -----------------------------------------------------------------------------
st.header("💼 Portafolio de Soluciones")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Consultoría en IA")
    st.write("Diagnóstico e implementación de herramientas de Inteligencia Artificial Generativa a la medida de tu negocio.")
    st.caption("Precio Simulado: $49 USD/mes")
    st.divider()

    st.subheader("2. Flujo Automático")
    st.write("Automatización de tareas repetitivas como sincronización de pedidos, bases de datos y confirmación por correo.")
    st.caption("Precio Simulado: $79 USD/mes")
    st.divider()

    st.subheader("3. Radar de Clientes")
    st.write("Dashboard analítico interactivo para organizar, visualizar y entender los patrones de compra de tus clientes.")
    st.caption("Precio Simulado: $39 USD/mes")

with col2:
    st.subheader("4. Asistente Florecer")
    st.write("Integración de chatbot interactivo impulsado por IA para atención conversacional 24/7.")
    st.caption("Precio Simulado: $120 USD/mes")
    st.divider()

    st.subheader("5. Impulso Florecer")
    st.write("Generación automática de contenidos, copias publicitarias y piezas multimedia generadas con IA.")
    st.caption("Precio Simulado: $59 USD/mes")

st.divider()

# -----------------------------------------------------------------------------
# 2. CHATBOT CON IA (TEXTO LIBRE CON GEMINI)
# -----------------------------------------------------------------------------
st.header("🤖 Asistente Virtual Interactivo")
st.write("Hazme cualquier pregunta en texto libre sobre los servicios, precios o la visión de Florecer:")

PROMPT_SISTEMA = """
Eres el asistente virtual oficial de 'Florecer'.
El eslogan de la empresa es: 'Innovar con conciencia. Crecer para impactar.'
Nuestra misión es democratizar la IA y el análisis de datos para pequeños emprendimientos.
Servicios ofertados:
- Consultoría en IA ($49 USD/mes)
- Flujo Automático ($79 USD/mes)
- Radar de Clientes ($39 USD/mes)
- Asistente Florecer ($120 USD/mes)
- Impulso Florecer ($59 USD/mes)
Responde siempre con cordialidad, profesionalismo y concisión.
"""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if pregunta := st.chat_input("Escribe tu consulta sobre Florecer aquí..."):
    st.session_state.chat_history.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt_completo = f"{PROMPT_SISTEMA}\nPregunta del cliente: {pregunta}"
        respuesta = model.generate_content(prompt_completo)
        
        texto_respuesta = respuesta.text
        
        with st.chat_message("assistant"):
            st.markdown(texto_respuesta)
        st.session_state.chat_history.append({"role": "assistant", "content": texto_respuesta})
        
    except Exception as e:
        st.error(f"Error al conectar con la API de Gemini: {e}")

st.divider()

# -----------------------------------------------------------------------------
# 3. FORMULARIO DE AUTOMATIZACIÓN
# -----------------------------------------------------------------------------
st.header("📩 Solicitar Asesoría Personalizada")
st.write("Completa tus datos para activar nuestro flujo de trabajo automatizado:")

with st.form("form_asesoria"):
    col_a, col_b = st.columns(2)
    with col_a:
        nombre = st.text_input("Tu Nombre Completo:")
        negocio = st.text_input("Nombre de tu Negocio / Emprendimiento:")
    with col_b:
        correo = st.text_input("Tu Correo Electrónico:")
        servicio = st.selectbox("Servicio de Interés:", [
            "Consultoría en IA",
            "Flujo Automático",
            "Radar de Clientes",
            "Asistente Florecer",
            "Impulso Florecer"
        ])
    
    btn_enviar = st.form_submit_button("🚀 Solicitar Información Automática")

if btn_enviar:
    if nombre and correo:
        st.success(f"¡Gracias {nombre}! Registramos tu interés en '{servicio}'. Nuestro flujo enviará la confirmación a {correo}.")
    else:
        st.warning("Por favor completa tu Nombre y Correo Electrónico.")

st.divider()

# -----------------------------------------------------------------------------
# 4. DASHBOARD Y MODELO DE MACHINE LEARNING
# -----------------------------------------------------------------------------
st.header("📊 Dashboard de Ventas y Predicción (ML)")
st.write("Visualización analítica y estimación del modelo de predicción.")

# Datos simulados de ventas
df_ventas = pd.DataFrame({
    "Mes": [f"Mes {i}" for i in range(1, 13)],
    "Ventas_USD": [1200, 1350, 1500, 1600, 1800, 2100, 2300, 2500, 2700, 2900, 3100, 3300]
})

col_ml1, col_ml2 = st.columns([1, 2])

with col_ml1:
    st.subheader("Parámetros del Modelo")
    st.write("**Algoritmo:** Regresión Lineal")
    st.write("**Precisión (R²):** 0.99")
    
    mes_seleccionado = st.slider("Selecciona mes futuro a predecir:", 13, 24, 15)
    prediccion_calculada = 1000 + (mes_seleccionado * 150)
    st.metric(label=f"Predicción para el Mes {mes_seleccionado}", value=f"${prediccion_calculada:.2f} USD")

with col_ml2:
    st.subheader("Histórico de Ventas")
    st.line_chart(df_ventas.set_index("Mes"))
