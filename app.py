import streamlit as st
import google.generativeai as genai
import pandas as pd
from PIL import Image
import os
import requests
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

# -----------------------------------------------------------------------------
# 1. CONFIGURACIÓN DE PÁGINA E IDENTIDAD VISUAL DE FLORECER
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Florecer - Soluciones de IA y Datos",
    page_icon="🌸",
    layout="wide"
)

# Estilos CSS con la Paleta de Colores Oficial de Florecer
st.markdown("""
    <style>
    /* Fondo General Crema */
    .stApp {
        background-color: #F5EFE3 !important;
    }
    
    /* Títulos Principales en Agua Marina */
    h1, h2, h3 {
        color: #206785 !important;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Textos Generales */
    p, label, span, div {
        color: #212121 !important;
        font-family: 'Lato', sans-serif;
    }
    
    .main-title {
        color: #206785 !important;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0px;
    }

    .slogan {
        color: #7BC9BF !important;
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin-bottom: 20px;
    }

    /* Tarjetas del Portafolio */
    .card-florecer {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #7BC9BF;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }

    .card-florecer h4 {
        color: #FFB268 !important;
        margin-top: 0;
    }

    /* Botones en Naranja Pastel */
    div.stButton > button, div[data-testid="stFormSubmitButton"] > button {
        background-color: #FFB268 !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 16px !important;
        padding: 10px 24px !important;
        width: 100% !important;
    }

    div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        background-color: #206785 !important;
        color: #FFFFFF !important;
    }

    /* Inputs y Formularios */
    div[data-baseweb="input"] > div {
        background-color: #FFFFFF !important;
        border: 1.5px solid #7BC9BF !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Configuración de Gemini API mediante Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# -----------------------------------------------------------------------------
# 2. ENCABEZADO E IDENTIDAD DEL PROYECTO (Requerimiento 4.1)
# -----------------------------------------------------------------------------
col_logo, col_text = st.columns([1, 2])

logo_encontrado = None
posibles_nombres = ['logo.png', 'logo.jpg', 'logo.jpeg', 'logo.png.jpg']
for nombre in posibles_nombres:
    if os.path.exists(nombre):
        logo_encontrado = nombre
        break

with col_logo:
    if logo_encontrado:
        st.image(Image.open(logo_encontrado), width=240)
    else:
        st.warning("📌 Sube la imagen 'logo.png' a la carpeta del proyecto.")

with col_text:
    st.markdown('<p class="main-title">FLORECER</p>', unsafe_allow_html=True)
    st.markdown('<p class="slogan">Innovar con conciencia. Crecer para impactar.</p>', unsafe_allow_html=True)
    st.write("""
    **Misión:** Democratizar el acceso a la inteligencia artificial y la analítica de datos para pequeñas empresas, permitiéndoles optimizar decisiones y escalar de forma consciente y eficiente[cite: 2].
    
    **Visión:** Ser el puente digital sostenible que conecta ideas, personas y tecnología para transformar negocios locales al año 2028[cite: 2].
    """)

st.divider()

# -----------------------------------------------------------------------------
# 3. NAVEGACIÓN PRINCIPAL
# -----------------------------------------------------------------------------
menu = st.sidebar.radio(
    "Navegación del Proyecto:",
    [
        "💼 1. Portafolio de Servicios",
        "🎬 2. Video Comercial (IA)",
        "🤖 3. Asistente Chatbot IA",
        "📩 4. Solicitar Asesoría (n8n)",
        "📊 5. Dashboard & Modelo ML",
        "💡 6. Declaración de IA Generativa"
    ]
)

# -----------------------------------------------------------------------------
# SECCIÓN 1: PORTAFOLIO DE SERVICIOS (Requerimiento 4.2)
# -----------------------------------------------------------------------------
if menu == "💼 1. Portafolio de Servicios":
    st.header("💼 Portafolio de Soluciones Inteligentes")
    st.write("Explora nuestras 5 soluciones digitales diseñadas para impulsar tu negocio[cite: 2]:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card-florecer">
            <h4>🤖 1. Asistente Florecer</h4>
            <p>Chatbot interactivo conversacional 24/7 con la API de Gemini para atención a clientes y captación de oportunidades.</p>
            <small style="color: #206785;"><b>Precio Simulado: $120 USD/mes</b></small>
        </div>
        <div class="card-florecer">
            <h4>⚙️ 2. Flujo Automático</h4>
            <p>Automatización de tareas repetitivas mediante n8n (sincronización de pedidos, bases de datos y correos).</p>
            <small style="color: #206785;"><b>Precio Simulado: $79 USD/mes</b></small>
        </div>
        <div class="card-florecer">
            <h4>📊 3. Radar de Clientes</h4>
            <p>Dashboard analítico e interactivo en Streamlit para organizar y visualizar patrones de venta en tiempo real.</p>
            <small style="color: #206785;"><b>Precio Simulado: $39 USD/mes</b></small>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card-florecer">
            <h4>🧠 4. Decisiones Florecer</h4>
            <p>Modelo predictivo de Machine Learning (Regresión Lineal) para realizar estimaciones e ingresos futuros.</p>
            <small style="color: #206785;"><b>Precio Simulado: $99 USD/mes</b></small>
        </div>
        <div class="card-florecer">
            <h4>🌱 5. Impulso Florecer</h4>
            <p>Generación automática de contenidos publicitarios, copys y piezas multimedia con herramientas de IA.</p>
            <small style="color: #206785;"><b>Precio Simulado: $59 USD/mes</b></small>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SECCIÓN 2: CONTENIDO MULTIMEDIA CON IA (Requerimiento 4.3)
# -----------------------------------------------------------------------------
elif menu == "🎬 2. Video Comercial (IA)":
    st.header("🎬 Video Comercial Promocional")
    st.write("Demostración de contenido publicitario de 15 a 45 segundos generado con IA Generativa[cite: 2]:")

    # Si tienes el archivo local subido lo carga, si no muestra un placeholder informativo
    if os.path.exists("video_florecer.mp4"):
        st.video("video_florecer.mp4")
    else:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.info("💡 Coloca tu archivo 'video_florecer.mp4' (generado en CapCut AI / HeyGen) en la carpeta raíz para reemplazar el video de demostración[cite: 2].")

# -----------------------------------------------------------------------------
# SECCIÓN 3: CHATBOT CON IA CONVERSACIONAL (Requerimiento 4.4)
# -----------------------------------------------------------------------------
elif menu == "🤖 3. Asistente Chatbot IA":
    st.header("🤖 Asistente Virtual Interactivo")
    st.write("Haz cualquier consulta en texto libre sobre los servicios, precios o la visión de Florecer[cite: 2]:")

    PROMPT_SISTEMA = """
    Eres el asistente virtual interactivo de 'Florecer', una empresa dedicada a impulsar
    pequeños negocios mediante herramientas de Inteligencia Artificial y Análisis de Datos.
    Paleta de marca: Naranja Pastel, Agua Marina, Verde Suave, Lavanda y Crema.
    Ofrecemos 5 servicios: Asistente Florecer ($120 USD), Flujo Automático ($79 USD),
    Radar de Clientes ($39 USD), Decisiones Florecer ($99 USD) e Impulso Florecer ($59 USD).
    Tus respuestas deben ser siempre amables, claras, motivadoras y breves.
    """

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Escribe tu consulta aquí..."):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt_completo = f"{PROMPT_SISTEMA}\nPregunta del usuario: {prompt}"
            response = model.generate_content(prompt_completo)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            st.error(f"Error al conectar con la API de Gemini. Asegúrate de configurar GEMINI_API_KEY en secrets.toml. Detalles: {e}")

# -----------------------------------------------------------------------------
# SECCIÓN 4: AUTOMATIZACIÓN (Requerimiento 4.5)
# -----------------------------------------------------------------------------
elif menu == "📩 4. Solicitar Asesoría (n8n)":
    st.header("📩 Solicitar Asesoría Personalizada")
    st.write("Completa el formulario para activar el flujo automatizado a través de n8n[cite: 2]:")

    WEBHOOK_URL = "https://denisgreenway.app.n8n.cloud/webhook/florecer-contacto"

    with st.form("form_contacto_n8n"):
        c_nombre, c_correo = st.columns(2)
        with c_nombre:
            nombre = st.text_input("Tu Nombre Completo:")
        with c_correo:
            email = st.text_input("Tu Correo Electrónico:")

        c_empresa, c_servicio = st.columns(2)
        with c_empresa:
            empresa = st.text_input("Nombre de tu Negocio:")
        with c_servicio:
            servicio_interes = st.selectbox(
                "Servicio de Interés:", 
                ["Asistente Florecer", "Flujo Automático", "Radar de Clientes", "Decisiones Florecer", "Impulso Florecer"]
            )

        boton_enviar = st.form_submit_button("🚀 Enviar Solicitud Automatizada")

    if boton_enviar:
        if nombre and email and empresa:
            datos_payload = {
                "nombre": nombre,
                "email": email,
                "empresa": empresa,
                "servicio_interes": servicio_interes
            }
            try:
                respuesta = requests.post(WEBHOOK_URL, json=datos_payload)
                if respuesta.status_code in [200, 201]:
                    st.success("✨ ¡Solicitud enviada con éxito! La automatización en n8n ha procesado tus datos[cite: 2].")
                else:
                    st.warning("⚠️ Solicitud enviada. Verifica que el Webhook en n8n esté activo[cite: 2].")
            except Exception as e:
                st.error(f"Error en la conexión con n8n: {e}")
        else:
            st.warning("Por favor completa los campos obligatorios antes de enviar.")

# -----------------------------------------------------------------------------
# SECCIÓN 5: MODELO DE MACHINE LEARNING Y DASHBOARD (Requerimiento 4.7)
# -----------------------------------------------------------------------------
elif menu == "📊 5. Dashboard & Modelo ML":
    st.header("📊 Dashboard & Modelo Predictivo de Ventas (ML)")
    st.write("Proyección de ingresos mediante Regresión Lineal entrenada con datos históricos[cite: 2]:")

    # Dataset simulado
    np.random.seed(42)
    meses = np.array(range(1, 13)).reshape(-1, 1)
    ventas = 1000 + (meses.flatten() * 180) + np.random.randint(-120, 120, size=12)
    df = pd.DataFrame({"Mes": meses.flatten(), "Ventas_USD": ventas})

    # Entrenamiento del Modelo
    model_ml = LinearRegression()
    model_ml.fit(meses, ventas)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("⚙️ Parámetros del Modelo")
        st.write(f"**Algoritmo:** Regresión Lineal (`scikit-learn`)[cite: 2]")
        st.write(f"**Precisión ($R^2$):** `{round(model_ml.score(meses, ventas), 2)}`")
        
        st.divider()
        mes_pred = st.slider("Selecciona el mes futuro a predecir:", 13, 24, 15)
        prediccion = model_ml.predict(np.array([[mes_pred]]))[0]
        st.metric(label=f"Predicción de Ventas (Mes {mes_pred})", value=f"${round(prediccion, 2)} USD")

    with col2:
        fig = px.scatter(
            df, x="Mes", y="Ventas_USD", 
            title="Tendencia de Ventas Históricas y Proyección",
            trendline="ols",
            color_discrete_sequence=["#206785"]
        )
        st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------------------------------
# SECCIÓN 6: DECLARACIÓN DE USO DE IA GENERATIVA (Requerimiento 4.6)
# -----------------------------------------------------------------------------
elif menu == "💡 6. Declaración de IA Generativa":
    st.header("💡 Uso de IA Generativa en el Proyecto")
    st.write("Declaración transparente del uso de herramientas de IA durante la creación de Florecer[cite: 2]:")

    st.markdown("""
    * **1. Generación de Código:** Uso de modelos LLM (Gemini / ChatGPT) para la arquitectura de la app web en Python y Streamlit[cite: 2].
    * **2. Generación de Texto y Prompting:** Configuración de prompts de sistema para el chatbot conversacional `gemini-1.5-flash`[cite: 2].
    * **3. Generación de Identidad e Imágenes:** Creación del concepto visual, marca y logo utilizando herramientas de IA Generativa[cite: 2].
    * **4. Generación de Video Comercial:** Producción multimedia con herramientas de avatares/video de IA para la promoción del servicio[cite: 2].
    """)
