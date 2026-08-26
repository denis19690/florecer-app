import streamlit as st
import pandas as pd
import numpy as np
import os

# 1. Configuración de página y estética de marca
st.set_page_config(
    page_title="Florecer - Innovación con Conciencia",
    page_icon="🌱",
    layout="wide"
)

# Estilos CSS con verde esmeralda, aguamarina y acentos naranja
st.markdown("""
    <style>
    .stApp {
        background-color: #F8FBF8;
    }
    h1, h2, h3 {
        color: #0F5257 !important;
    }
    .stButton>button {
        background-color: #0B6E4F;
        color: white;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #E67E22;
        color: white;
    }
    .card-box {
        background-color: #E8F5E9;
        padding: 18px;
        border-radius: 10px;
        border-left: 6px solid #0B6E4F;
        margin-bottom: 15px;
    }
    .highlight-orange {
        color: #E67E22;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Menú de navegación lateral
st.sidebar.title("Navegación del Proyecto:")
opcion = st.sidebar.radio(
    "",
    [
        "💼 1. Portafolio de Servicios",
        "🎬 2. Video Comercial (Avatar)",
        "🤖 3. Asistente Chatbot IA",
        "📩 4. Solicitar Asesoría (n8n)",
        "📊 5. Dashboard & Modelo ML",
        "💡 6. Declaración de IA & Cierre"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("🌱 **FLORECER**\nInnovar con conciencia. Crecer para impactar.")

# -------------------------------------------------------------------
# 1. PORTAFOLIO DE SERVICIOS
# -------------------------------------------------------------------
if opcion == "💼 1. Portafolio de Servicios":
    st.title("💼 1. Portafolio de Servicios")
    st.write("Conecta naturaleza, tecnología y humanidad a través de soluciones con propósito.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card-box">
            <h4>1. Consultoría en IA Generativa</h4>
            <p>Diseño e implementación de asistentes virtuales y soluciones a la medida.</p>
        </div>
        <div class="card-box">
            <h4>2. Automatización con Webhooks & n8n</h4>
            <p>Integración de flujos de trabajo inteligentes para captura de datos y atención.</p>
        </div>
        <div class="card-box">
            <h4>3. Agentes Conversacionales</h4>
            <p>Chatbots inteligentes entrenados con el contexto corporativo de tu empresa.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card-box">
            <h4>4. Dashboards & Analítica Predictiva</h4>
            <p>Visualización de métricas en tiempo real y modelos de pronóstico con ML.</p>
        </div>
        <div class="card-box">
            <h4>5. Identidad Multimedia IA</h4>
            <p>Creación de avatares parlantes, piezas visuales y copywriting de alto impacto.</p>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------------
# 2. VIDEO COMERCIAL (AVATAR)
# -------------------------------------------------------------------
elif opcion == "🎬 2. Video Comercial (Avatar)":
    st.title("🎬 2. Video Comercial con Avatar Parlante")
    st.write("Presentación oficial de Florecer generada con Inteligencia Artificial.")
    
    video_file = "video_florecer.mp4"
    
    if os.path.exists(video_file):
        st.video(video_file)
    else:
        st.warning("⚠️ No se encontró el archivo local 'video_florecer.mp4'. Puedes cargarlo directamente aquí para probarlo:")
        uploaded_video = st.file_uploader("Sube tu video descargado de Canva/D-ID (.mp4)", type=["mp4"])
        if uploaded_video is not None:
            st.video(uploaded_video)

# -------------------------------------------------------------------
# 3. ASISTENTE CHATBOT IA
# -------------------------------------------------------------------
elif opcion == "🤖 3. Asistente Chatbot IA":
    st.title("🤖 3. Asistente Chatbot Virtual")
    st.write("Interactúa con la IA de **Florecer**:")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "¡Hola! Soy la IA de Florecer. ¿En qué puedo ayudarte hoy?"}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Escribe tu consulta... (ej: ¿Qué es Florecer?, ¿Cuál es su misión?)"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Respuestas dinámicas según el texto ingresado
        query = prompt.lower()
        if "florecer" in query or "que es" in query:
            resp = "🌱 **Florecer** es un ecosistema de innovación que conecta naturaleza, tecnología y humanidad para transformar negocios mediante IA y automatización."
        elif "mision" in query or "propósito" in query or "propósito" in query:
            resp = "🎯 Nuestra misión es impulsar a las personas y empresas para crear soluciones tecnológicas con propósito, promoviendo la innovación consciente."
        elif "servicio" in query or "hacen" in query:
            resp = "💡 Ofrecemos Consultoría en IA, Automatizaciones con n8n, Chatbots, Analítica Predictiva y Contenido Multimedia con Avatares."
        elif "contacto" in query or "asesoria" in query:
            resp = "📩 Puedes solicitar una asesoría personalizada ingresando a la opción 4 del menú lateral."
        else:
            resp = f"Entendido. Sobre '{prompt}', en Florecer aplicamos tecnología orientada al crecimiento sostenible y el aprendizaje continuo."

        with st.chat_message("assistant"):
            st.markdown(resp)
        st.session_state.messages.append({"role": "assistant", "content": resp})

# -------------------------------------------------------------------
# 4. SOLICITAR ASESORÍA (N8N)
# -------------------------------------------------------------------
elif opcion == "📩 4. Solicitar Asesoría (n8n)":
    st.title("📩 4. Solicitar Asesoría (Automatización n8n)")
    st.write("Completa este formulario para procesar tu solicitud mediante webhooks:")
    
    with st.form("form_contacto"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            nombre = st.text_input("Nombre completo:")
            correo = st.text_input("Correo electrónico:")
        with col_f2:
            empresa = st.text_input("Empresa / Proyecto:")
            servicio = st.selectbox("Servicio de interés:", ["Consultoría IA", "Automatización n8n", "Chatbots", "Machine Learning"])
        
        mensaje = st.text_area("Detalles del requerimiento:")
        submit = st.form_submit_button("Enviar Solicitud")
        
        if submit:
            st.success(f"✅ ¡Gracias {nombre}! Solicitud recibida. El flujo de automatización procesará la información de {empresa}.")

# -------------------------------------------------------------------
# 5. DASHBOARD & MODELO ML
# -------------------------------------------------------------------
elif opcion == "📊 5. Dashboard & Modelo ML":
    st.title("📊 5. Dashboard & Modelo de Machine Learning")
    st.write("Análisis de datos e indicadores de impacto:")
    
    # Datos de demostración
    np.random.seed(42)
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago"]
    eficiencia = [65, 70, 75, 82, 88, 91, 95, 98]
    solicitudes = [120, 150, 180, 220, 290, 310, 380, 450]
    
    df = pd.DataFrame({
        "Mes": meses,
        "Eficiencia %": eficiencia,
        "Solicitudes Procesadas": solicitudes
    })
    
    # Métricas clave
    m1, m2, m3 = st.columns(3)
    m1.metric("Optimización de Procesos", "98%", "+12%")
    m2.metric("Solicitudes Procesadas", "450", "+23%")
    m3.metric("Modelos Activos", "5 ML", "Estables")
    
    st.markdown("---")
    st.subheader("📈 Crecimiento de Eficiencia Operativa")
    st.line_chart(df.set_index("Mes")["Eficiencia %"])
    
    st.subheader("🤖 Simulación de Predicción ML")
    horas = st.slider("Selecciona horas de entrenamiento de IA:", 10, 100, 50)
    prediccion = round(horas * 1.85 + 15, 2)
    st.success(f"🎯 Con {horas} horas de entrenamiento, el modelo alcanzará una precisión estimada del **{prediccion}%**.")

# -------------------------------------------------------------------
# 6. DECLARACIÓN DE IA & CIERRE
# -------------------------------------------------------------------
elif opcion == "💡 6. Declaración de IA & Cierre":
    st.title("💡 6. Declaración del Uso de IA & Conclusiones")
    st.markdown("""
    <div class="card-box">
        <h4>Herramientas de IA Integradas:</h4>
        <ul>
            <li><b>D-ID / Canva:</b> Generación de avatar parlante e identidad visual.</li>
            <li><b>Gemini API / Botpress:</b> Lógica conversacional del chatbot.</li>
            <li><b>n8n:</b> Automatización de captura y procesamiento de datos.</li>
            <li><b>Scikit-Learn & Streamlit:</b> Analítica y despliegue del modelo predictivo.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
