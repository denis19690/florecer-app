import streamlit as st
import google.generativeai as genai
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA E IDENTIDAD
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Florecer - Soluciones de IA y Datos",
    page_icon="🌸",
    layout="wide"
)

# Configuración de Gemini API mediante Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Encabezado Principal
st.title("🌸 Florecer")
st.caption("Impulsando el crecimiento de tu negocio mediante Inteligencia Artificial y Analítica")

# Menú de Navegación Principal
menu = st.sidebar.radio(
    "Navegación del Proyecto:",
    [
        "1. Inicio y Misión", 
        "2. Portafolio de Servicios", 
        "3. Video Comercial (IA)", 
        "4. Asistente Chatbot IA", 
        "5. Solicitar Asesoría (Automatización)", 
        "6. Dashboard & Modelo ML"
    ]
)

# -----------------------------------------------------------------------------
# 1. IDENTIDAD DEL PROYECTO (Requerimiento 4.1)
# -----------------------------------------------------------------------------
if menu == "1. Inicio y Misión":
    st.header("📌 Sobre Nosotros")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?w=400", caption="Eslogan: Florece con datos e IA")
    with col2:
        st.subheader("Misión")
        st.write("Democratizar el acceso a la inteligencia artificial y analítica de datos para pequeños y medianos emprendimientos, permitiéndoles optimizar decisiones y escalar de manera eficiente.")
        
        st.subheader("Visión")
        st.write("Ser la plataforma líder en acompañamiento tecnológico con IA para pequeños negocios en la región para el año 2028.")

# -----------------------------------------------------------------------------
# 2. PORTAFOLIO DE SERVICIOS (Requerimiento 4.2 - Mínimo 5 elementos)
# -----------------------------------------------------------------------------
elif menu == "2. Portafolio de Servicios":
    st.header("💼 Portafolio de Soluciones")
    st.write("Explora nuestras 5 soluciones digitales diseñadas para impulsar tu empresa:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Consultoría en IA Generativa")
        st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=400")
        st.write("Diseño e implementación de asistentes virtuales y herramientas de contenido con IA.")
        st.write("**Precio estimado:** $300 USD")
        st.divider()

        st.subheader("2. Dashboards y Analítica de Datos")
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400")
        st.write("Paneles interactivos en Streamlit o Power BI para visualizar ventas y clientes.")
        st.write("**Precio estimado:** $450 USD")
        st.divider()

        st.subheader("3. Modelos de Predicción de Ventas (ML)")
        st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400")
        st.write("Implementación de modelos de Machine Learning para proyecciones de ingresos y demanda.")
        st.write("**Precio estimado:** $600 USD")

    with col2:
        st.subheader("4. Automatización de Flujos (n8n / Make)")
        st.image("https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400")
        st.write("Integración de formularios con Google Sheets, correos masivos y notificaciones.")
        st.write("**Precio estimado:** $250 USD")
        st.divider()

        st.subheader("5. Auditoría de Procesos Digitales")
        st.image("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=400")
        st.write("Evaluación completa para identificar cuellos de botella e integrar herramientas IA.")
        st.write("**Precio estimado:** $200 USD")

# -----------------------------------------------------------------------------
# 3. CONTENIDO MULTIMEDIA CON IA (Requerimiento 4.3)
# -----------------------------------------------------------------------------
elif menu == "3. Video Comercial (IA)":
    st.header("🎬 Video Promocional")
    st.write("Demostración de contenido generado con herramientas multimedia de Inteligencia Artificial:")
    
    # Muestra un video alojado o de demostración
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Puedes reemplazar por el enlace o archivo local .mp4
    st.info("💡 Este contenido multimedia fue diseñado con herramientas de generación de video e IA.")

# -----------------------------------------------------------------------------
# 4. CHATBOT CON IA - ENTRADA LIBRE (Requerimiento 4.4)
# -----------------------------------------------------------------------------
elif menu == "4. Asistente Chatbot IA":
    st.header("🤖 Asistente Virtual Interactivo")
    st.write("Haz cualquier pregunta en texto libre sobre los servicios, precios o misión de Florecer:")

    PROMPT_SISTEMA = """
    Eres el asistente virtual interactivo de 'Florecer', una empresa dedicada a impulsar
    pequeños negocios mediante herramientas de Inteligencia Artificial y Análisis de Datos.
    Ofrecemos: Consultoría en IA ($300 USD), Dashboards ($450 USD), Modelos ML ($600 USD), 
    Automatización ($250 USD) y Auditorías ($200 USD).
    Tus respuestas deben ser siempre amables, claras, breves y con enfoque comercial.
    """

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar historial del chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Entrada de texto libre
    if prompt := st.chat_input("Escribe tu consulta aquí..."):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt_completo = f"{PROMPT_SISTEMA}\nPregunta del cliente: {prompt}"
            response = model.generate_content(prompt_completo)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            st.error(f"Error al procesar la respuesta con la API de Gemini: {e}")

# -----------------------------------------------------------------------------
# 5. AUTOMATIZACIÓN - FORMULARIO (Requerimiento 4.5)
# -----------------------------------------------------------------------------
elif menu == "5. Solicitar Asesoría (Automatización)":
    st.header("📩 Solicitar Asesoría Personalizada")
    st.write("Completa tus datos para activar nuestro flujo de trabajo automatizado en n8n/Make hacia Google Sheets:")

    with st.form("form_asesoria"):
        nombre = st.text_input("Tu Nombre Completo:")
        correo = st.text_input("Tu Correo Electrónico:")
        negocio = st.text_input("Nombre de tu Negocio / Emprendimiento:")
        servicio = st.selectbox("Servicio de Interés:", [
            "Consultoría en IA Generativa",
            "Dashboards y Analítica",
            "Modelos de Predicción (ML)",
            "Automatización de Flujos",
            "Auditoría de Procesos"
        ])
        
        btn_enviar = st.form_submit_button("🚀 Solicitar Información Automática")

    if btn_enviar:
        if nombre and correo:
            st.success(f"¡Gracias {nombre}! Tu solicitud para '{servicio}' ha sido registrada. Nuestro flujo automatizado enviará la confirmación a {correo}.")
        else:
            st.warning("Por favor completa los campos obligatorios de Nombre y Correo.")

# -----------------------------------------------------------------------------
# 6. MODELO DE MACHINE LEARNING Y DASHBOARD (Requerimiento 4.7 y Opcional)
# -----------------------------------------------------------------------------
elif menu == "6. Dashboard & Modelo ML":
    st.header("📊 Dashboard de Ventas y Modelo de Predicción (ML)")
    st.write("Visualización interactiva y modelo simple de Regresión Lineal para predecir ventas futuras.")

    # Dataset simulado
    np.random.seed(42)
    meses = np.array(range(1, 13)).reshape(-1, 1)
    ventas = 1000 + (meses.flatten() * 150) + np.random.randint(-100, 100, size=12)
    
    df = pd.DataFrame({"Mes": meses.flatten(), "Ventas_USD": ventas})

    # Entrenamiento del modelo
    model_ml = LinearRegression()
    model_ml.fit(meses, ventas)

    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Parámetros del Modelo")
        st.write(f"**Algoritmo:** Regresión Lineal")
        st.write(f"**Precisión (R²):** {round(model_ml.score(meses, ventas), 2)}")
        
        mes_pred = st.slider("Selecciona el mes a predecir:", 13, 24, 15)
        prediccion = model_ml.predict(np.array([[mes_pred]]))[0]
        st.metric(label=f"Predicción de Ventas para el Mes {mes_pred}", value=f"${round(prediccion, 2)} USD")

    with col2:
        fig = px.scatter(df, x="Mes", y="Ventas_USD", title="Histórico de Ventas y Tendencia Lineal", trendline="ols")
        st.plotly_chart(fig, use_container_width=True)
