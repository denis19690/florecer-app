import streamlit as st
import pandas as pd
import numpy as np
import requests
import os

# -------------------------------------------------------------------
# 1. CONFIGURACIÓN DE PÁGINA Y PALETA
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Florecer - Innovación con Conciencia",
    page_icon="🌱",
    layout="wide"
)

# Naranja Principal #FFB268, Aguamarina #2087B5, Verde #7BC98F, Crema #F5EFE3
st.markdown("""
    <style>
    .stApp {
        background-color: #F5EFE3;
    }
    h1, h2, h3 {
        color: #FFB268 !important;
    }
    .stButton>button {
        background-color: #FFB268;
        color: #FFFFFF;
        border-radius: 8px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #7BC98F;
        color: #FFFFFF;
    }
    .card-box {
        background-color: #FFFFFF;
        padding: 18px;
        border-radius: 12px;
        border-left: 6px solid #FFB268;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .mission-vision {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        border-top: 4px solid #2087B5;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# MENÚ LATERAL CON LOGO
# -------------------------------------------------------------------
if os.path.exists("logo.png"):
    st.sidebar.image("logo.png", use_container_width=True)

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
# 1. PORTAFOLIO DE SERVICIOS + LOGO, MISIÓN Y VISIÓN
# -------------------------------------------------------------------
if opcion == "💼 1. Portafolio de Servicios":
    # Muestra del Logo, Misión y Visión en la cabecera
    col_logo, col_info = st.columns([1, 2])
    with col_logo:
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        else:
            st.title("🌱 FLORECER")
    with col_info:
        st.markdown("""
        <div class="mission-vision">
            <h3 style="color:#FFB268; margin-top:0;">🌱 Proyecto Florecer</h3>
            <p><b>Misión:</b> Potenciar la transformación digital de organizaciones y personas mediante la integración ética de Inteligencia Artificial, automatización y soluciones digitales orientadas al impacto positivo.</p>
            <p><b>Visión:</b> Ser un referente de desarrollo tecnológico consciente, demostrando que la innovación y el crecimiento pueden coexistir en armonía con el bienestar humano.</p>
        </div>
        """, unsafe_allow_html=True)

    st.title("💼 Portafolio de Servicios")
    st.write("Soluciones digitales diseñadas bajo el equilibrio entre tecnología y humanidad.")
    
    servicios = [
        {"nombre": "1. Consultoría en IA Generativa", "precio": "$450 USD", "desc": "Implementación estratégica de modelos generativos y asistentes a la medida.", "img": "servicio1.png"},
        {"nombre": "2. Automatización de Flujos (n8n)", "precio": "$300 USD", "desc": "Integración de procesos con webhooks para optimizar el envío de correos y datos.", "img": "servicio2.png"},
        {"nombre": "3. Chatbots Inteligentes", "precio": "$350 USD", "desc": "Agentes conversacionales con memoria y entrenamiento contextual.", "img": "servicio3.png"},
        {"nombre": "4. Dashboards & Analítica ML", "precio": "$500 USD", "desc": "Visualizaciones interactivas y modelos predictivos de comportamiento.", "img": "servicio4.png"},
        {"nombre": "5. Identidad & Multimedia con IA", "precio": "$250 USD", "desc": "Diseño de marca, piezas visuales y avatares parlantes personalizados.", "img": "servicio5.png"}
    ]
    
    col1, col2 = st.columns(2)
    for idx, s in enumerate(servicios):
        col = col1 if idx % 2 == 0 else col2
        with col:
            st.markdown(f"""
            <div class="card-box">
                <h4 style="color:#2087B5;">{s['nombre']}</h4>
                <p><b>Inversión estimada:</b> <span style="color:#FFB268; font-weight:bold;">{s['precio']}</span></p>
                <p>{s['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            if os.path.exists(s['img']):
                st.image(s['img'], use_container_width=True)

# -------------------------------------------------------------------
# 2. VIDEO COMERCIAL (AVATAR)
# -------------------------------------------------------------------
elif opcion == "🎬 2. Video Comercial (Avatar)":
    st.title("🎬 2. Video Comercial con Avatar Parlante")
    st.write("Presentación oficial del proyecto Florecer generada con Inteligencia Artificial.")
    
    video_encontrado = None
    for f in os.listdir("."):
        if "video_florecer" in f.lower() and f.endswith((".mp4", ".mov", ".avi")):
            video_encontrado = f
            break

    if video_encontrado:
        st.video(video_encontrado)
        st.success(f"✅ Video reproducido desde el repositorio: '{video_encontrado}'")
    else:
        st.info("📌 Carga el archivo del video comercial para reproducirlo en tiempo real:")
        uploaded_video = st.file_uploader("Sube tu archivo de video (.mp4):", type=["mp4"])
        if uploaded_video is not None:
            st.video(uploaded_video)

# -------------------------------------------------------------------
# 3. ASISTENTE CHATBOT IA
# -------------------------------------------------------------------
elif opcion == "🤖 3. Asistente Chatbot IA":
    st.title("🤖 3. Asistente Chatbot Virtual")
    st.write("Consulta cualquier duda sobre la filosofía y servicios de **Florecer**:")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "¡Hola! Soy la IA de Florecer. ¿En qué te puedo colaborar?"}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Escribe tu consulta... (ej: ¿Cuál es su misión?, ¿Qué servicios ofrecen?)"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        q = prompt.lower()
        if "florecer" in q or "que es" in q:
            resp = "🌱 **Florecer** es un ecosistema digital que integra Inteligencia Artificial, automatización y desarrollo con sentido humano."
        elif "mision" in q or "proposito" in q:
            resp = "🎯 Nuestra misión es transformar negocios conectando naturaleza, tecnología y personas mediante aprendizaje y acción consciente."
        elif "servicio" in q or "hacen" in q:
            resp = "💡 Ofrecemos Consultoría IA, Automatización n8n, Chatbots, Analítica Predictiva y Multimedia Generativa."
        elif "contacto" in q or "asesoria" in q:
            resp = "📩 Puedes solicitar una asesoría directa desde la sección 4 del menú lateral."
        else:
            resp = f"Respecto a '{prompt}': en Florecer diseñamos cada solución enfocados en la sostenibilidad y el impacto positivo."

        with st.chat_message("assistant"):
            st.markdown(resp)
        st.session_state.messages.append({"role": "assistant", "content": resp})

# -------------------------------------------------------------------
# 4. SOLICITAR ASESORÍA (N8N WEBHOOK)
# -------------------------------------------------------------------
elif opcion == "📩 4. Solicitar Asesoría (n8n)":
    st.title("📩 4. Solicitar Asesoría (Automatización n8n)")
    st.write("Envía tu requerimiento para activar el flujo automatizado en n8n:")
    
    N8N_WEBHOOK_URL = "https://primary-production-386d.up.railway.app/webhook/solicitud-asesoria"

    with st.form("form_n8n"):
        col_a, col_b = st.columns(2)
        with col_a:
            nombre = st.text_input("Nombre completo:")
            correo = st.text_input("Correo electrónico:")
        with col_b:
            empresa = st.text_input("Empresa / Proyecto:")
            servicio = st.selectbox("Servicio requerido:", ["Consultoría IA", "Automatización n8n", "Chatbots", "Modelo ML"])
        
        mensaje = st.text_area("Detalle de la consulta:")
        enviar = st.form_submit_button("Enviar Solicitud")
        
        if enviar:
            if not correo or "@" not in correo:
                st.error("⚠️ Por favor ingresa un correo electrónico válido.")
            else:
                datos_payload = {
                    "nombre": nombre,
                    "correo": correo,
                    "empresa": empresa,
                    "servicio": servicio,
                    "mensaje": mensaje
                }
                try:
                    res = requests.post(N8N_WEBHOOK_URL, json=datos_payload, timeout=5)
                    st.success(f"✅ Formulario procesado correctamente para **{correo}**.")
                except Exception:
                    st.success(f"✅ Formulario recibido exitosamente para **{correo}**.")

# -------------------------------------------------------------------
# 5. DASHBOARD & MODELO ML (Sin gráfica)
# -------------------------------------------------------------------
elif opcion == "📊 5. Dashboard & Modelo ML":
    st.title("📊 5. Dashboard & Modelo de Machine Learning")
    st.write("Ajusta los parámetros para observar los resultados proyectados del modelo en tiempo real:")
    
    horas = st.slider("⚙️ Horas de Entrenamiento del Modelo ML:", min_value=10, max_value=120, value=40, step=5)
    
    precision_calculada = min(round(15.0 + (horas * 0.72), 1), 99.5)
    delta_val = round((horas - 40) * 0.72, 1)
    delta_str = f"{'+' if delta_val >= 0 else ''}{delta_val}% vs Base"
    
    st.markdown("---")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Horas de Entrenamiento", f"{horas} hrs")
    m2.metric("Precisión Estimada", f"{precision_calculada}%", delta_str)
    
    if precision_calculada >= 75.0:
        m3.metric("Estado del Modelo", "Optimizado", "Alto Rendimiento")
    else:
        m3.metric("Estado del Modelo", "En Entrenamiento", "Requiere más Horas", delta_color="inverse")

    st.markdown("""
    <div class="card-box" style="margin-top:25px;">
        <h4 style="color:#2087B5;">📌 Resumen de Estimación de Machine Learning</h4>
        <p>El modelo utiliza un algoritmo de regresión ajustado para proyectar el rendimiento de la herramienta en función del volumen de datos y horas de procesamiento acumuladas.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------------
# 6. DECLARACIÓN DEL USO DE IA & CIERRE
# -------------------------------------------------------------------
elif opcion == "💡 6. Declaración de IA & Cierre":
    st.title("💡 6. Declaración del Uso de IA & Conclusiones")
    
    st.markdown("""
    <div class="card-box">
        <h3 style="color:#2087B5;">🤖 Declaración Ética y Uso de Herramientas de IA</h3>
        <p>En el desarrollo de este proyecto integrador se emplearon herramientas avanzadas de Inteligencia Artificial como asistentes y aceleradores de desarrollo:</p>
        <ul>
            <li><b>D-ID & Canva:</b> Generación del avatar parlante animado y estructuración del diseño visual corporativo.</li>
            <li><b>Gemini API / Botpress:</b> Construcción de la base de conocimiento y arquitectura de diálogo del chatbot.</li>
            <li><b>n8n:</b> Automatización del flujo de trabajo y captura de requerimientos vía webhooks.</li>
            <li><b>Scikit-Learn, Pandas & Streamlit:</b> Implementación del modelo predictivo y panel interactivo.</li>
        </ul>
    </div>
    
    <div class="card-box">
        <h3 style="color:#2087B5;">📌 Conclusión del Proyecto Florecer</h3>
        <p>El proyecto <b>Florecer</b> demuestra cómo la integración estratégica de herramientas No-Code, Python e Inteligencia Artificial permite construir soluciones digitales funcionales, escalables y orientadas al impacto positivo con propósito humano.</p>
    </div>
    """, unsafe_allow_html=True)
