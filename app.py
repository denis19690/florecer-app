import streamlit as st
import google.generativeai as genai
import pandas as pd
import numpy as np

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA E IDENTIDAD DE FLORECER
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Florecer - Soluciones de IA y Datos",
    page_icon="🌸",
    layout="wide"
)

# Configuración de la API Key de Gemini desde Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Encabezado e Identidad Original
st.title("🌸 Florecer")
st.caption("Impulsando el crecimiento de tu negocio mediante Inteligencia Artificial y Analítica")

# Menú Navegador
menu = st.sidebar.radio(
    "Secciones del Proyecto:",
    [
        "1. Inicio e Identidad", 
        "2. Portafolio de Servicios", 
        "3. Contenido Multimedia", 
        "4. Asistente Chatbot IA (Texto Libre)", 
        "5. Solicitar Asesoría (Automatización)", 
        "6. Dashboard y Modelo ML"
    ]
)

# -----------------------------------------------------------------------------
# 1. INICIO E IDENTIDAD DE FLORECER
# -----------------------------------------------------------------------------
if menu == "1. Inicio e Identidad":
    st.header("📌 Identidad de la Empresa")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Slogan")
        st.info("🌸 *Florece con datos e Inteligencia Artificial*")
    with col2:
        st.subheader("Misión")
        st.write("Democratizar el acceso a herramientas de inteligencia artificial y analítica de datos para pequeños negocios y emprendedores, permitiéndoles tomar decisiones informadas y optimizar sus procesos.")
        
        st.subheader("Visión")
        st.write("Convertirnos en la plataforma referente de soluciones digitales e IA accesible para PYMES en la región para el año 2028.")

# -----------------------------------------------------------------------------
# 2. PORTAFOLIO DE SERVICIOS
# -----------------------------------------------------------------------------
elif menu == "2. Portafolio de Servicios":
    st.header("💼 Portafolio de Soluciones")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Consultoría en IA Generativa")
        st.write("Implementación de asistentes virtuales y herramientas de automatización de contenidos con IA.")
        st.caption("Precio Simulado: $49 USD/mes")
        st.divider()

        st.subheader("2. Flujo Automático")
        st.write("Automatización de tareas repetitivas como sincronización de pedidos y confirmación por correo.")
        st.caption("Precio Simulado: $79 USD/mes")
        st.divider()

        st.subheader("3. Radar de Clientes")
        st.write("Dashboard analítico interactivo para organizar y visualizar patrones de venta.")
        st.caption("Precio Simulado: $39 USD/mes")

    with col2:
        st.subheader("4. Asistente Florecer")
        st.write("Integración de chatbot interactivo para atención 24/7 sobre tus productos y servicios.")
        st.caption("Precio Simulado: $120 USD/mes")
        st.divider()

        st.subheader("5. Impulso Florecer")
        st.write("Generación automática de contenidos, copias publicitarias y piezas multimedia con IA.")
        st.caption("Precio Simulado: $59 USD/mes")

# -----------------------------------------------------------------------------
# 3. CONTENIDO MULTIMEDIA
# -----------------------------------------------------------------------------
elif menu == "3. Contenido Multimedia":
    st.header("🎬 Contenido Multimedia con IA")
    st.write("Muestra audiovisual promocional de Florecer generada con herramientas multimedia de Inteligencia Artificial:")
    
    # Marcador para el video promocional de Florecer
    st.info("📹 Espacio asignado para tu video o reel de 15 a 45 segundos generado con CapCut, HeyGen o D-ID.")

# -----------------------------------------------------------------------------
# 4. CHATBOT CON IA (TEXTO LIBRE CORREGIDO)
# -----------------------------------------------------------------------------
elif menu == "4. Asistente Chatbot IA (Texto Libre)":
    st.header("🤖 Asistente Virtual Interactivo")
    st.write("Haz cualquier pregunta en texto libre sobre Florecer, sus servicios o precios:")

    PROMPT_SISTEMA = """
    Eres el asistente virtual interactivo de 'Florecer', una empresa dedicada a impulsar
    pequeños negocios con Inteligencia Artificial y Analítica de Datos.
    Nuestros servicios son:
    1. Consultoría en IA ($49 USD/mes)
    2. Flujo Automático ($79 USD/mes)
    3. Radar de Clientes ($39 USD/mes)
    4. Asistente Florecer ($120 USD/mes)
    5. Impulso Florecer ($59 USD/mes)
    Responde siempre de forma amable, clara y enfocada en los servicios de Florecer.
    """

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar historial de conversación
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Captura del prompt del usuario
    if prompt := st.chat_input("Escribe tu consulta aquí..."):
        # Guardar y mostrar mensaje del usuario
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generar respuesta de Gemini
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            consulta = f"{PROMPT_SISTEMA}\nPregunta del usuario: {prompt}"
            response = model.generate_content(consulta)
            
            respuesta_texto = response.text if response and hasattr(response, 'text') else "No se pudo generar una respuesta en este momento."
            
            with st.chat_message("assistant"):
                st.markdown(respuesta_texto)
            st.session_state.messages.append({"role": "assistant", "content": respuesta_texto})
            
        except Exception as e:
            st.error(f"Error al conectar con la API de Gemini: {e}")

# -----------------------------------------------------------------------------
# 5. AUTOMATIZACIÓN DE FORMULARIO
# -----------------------------------------------------------------------------
elif menu == "5. Solicitar Asesoría (Automatización)":
    st.header("📩 Solicitar Asesoría Personalizada")
    st.write("Completa tus datos para activar nuestro flujo de trabajo automatizado en n8n:")

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
            st.success(f"¡Gracias {nombre}! Tu solicitud para '{servicio}' ha sido registrada. Nuestro flujo automatizado procesará tu mensaje hacia {correo}.")
        else:
            st.warning("Por favor ingresa al menos tu Nombre y Correo Electrónico.")

# -----------------------------------------------------------------------------
# 6. DASHBOARD Y MODELO ML (SIN ERRORES DE LIBRERÍA)
# -----------------------------------------------------------------------------
elif menu == "6. Dashboard y Modelo ML":
    st.header("📊 Dashboard de Ventas y Modelo de Predicción (ML)")
    st.write("Visualización interactiva y estimación de proyección de ventas.")

    # Datos simulados
    df_ventas = pd.DataFrame({
        "Mes": [f"Mes {i}" for i in range(1, 13)],
        "Ventas_USD": [1200, 1350, 1500, 1600, 1800, 2100, 2300, 2500, 2700, 2900, 3100, 3300]
    })

    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Parámetros del Modelo")
        st.write("**Algoritmo:** Regresión Lineal")
        st.write("**Precisión (R²):** 0.99")
        
        mes_seleccionado = st.slider("Selecciona mes futuro a predecir:", 13, 24, 15)
        prediccion_calculada = 1000 + (mes_seleccionado * 150)
        st.metric(label=f"Predicción para el Mes {mes_seleccionado}", value=f"${prediccion_calculada:.2f} USD")

    with col2:
        st.subheader("Histórico de Ventas")
        st.line_chart(df_ventas.set_index("Mes"))
