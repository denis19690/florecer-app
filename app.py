import streamlit as st
import os

# Configuración inicial de la página
st.set_page_config(
    page_title="Florecer - Proyecto Integrador IA",
    page_icon="🌱",
    layout="wide"
)

# Menú de Navegación con los 6 puntos exactos
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
    st.title("💼 1. Portafolio de Servicios de IA")
    st.write("Soluciones digitales impulsadas por Inteligencia Artificial y datos.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Consultoría en IA Generativa")
        st.write("Implementación de modelos a medida para automatizar tareas complejas.")
        st.subheader("2. Automatización con Webhooks & n8n")
        st.write("Flujos de trabajo integrados para capturar clientes y enviar alertas.")
        st.subheader("3. Asistentes Virtuales 24/7")
        st.write("Chatbots inteligentes para atención al cliente y soporte.")
    with col2:
        st.subheader("4. Analítica Predictiva & ML")
        st.write("Predicción de tendencias de negocio con Python y Scikit-learn.")
        st.subheader("5. Identidad Multimedia IA")
        st.write("Creación de avatares parlantes, piezas visuales y contenido de marca.")

# -------------------------------------------------------------------
# 2. VIDEO COMERCIAL (AVATAR)
# -------------------------------------------------------------------
elif opcion == "🎬 2. Video Comercial (Avatar)":
    st.title("🎬 2. Video Comercial con Avatar Parlante")
    st.write("Presentación oficial de Florecer generada con IA.")
    
    video_file = "video_florecer.mp4"
    if os.path.exists(video_file):
        st.video(video_file)
    else:
        st.info("📌 Coloca el archivo 'video_florecer.mp4' en la carpeta de tu proyecto para visualizarlo aquí.")

# -------------------------------------------------------------------
# 3. ASISTENTE CHATBOT IA
# -------------------------------------------------------------------
elif opcion == "🤖 3. Asistente Chatbot IA":
    st.title("🤖 3. Asistente Chatbot Virtual")
    st.write("Interactúa con el Oráculo de Florecer:")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "¡Hola! Soy la IA de Florecer. ¿En qué puedo ayudarte?"}]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Escribe tu consulta..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        resp = f"Gracias por tu consulta sobre '{prompt}'. En Florecer conectamos tecnología y propósito."
        with st.chat_message("assistant"):
            st.markdown(resp)
        st.session_state.messages.append({"role": "assistant", "content": resp})

# -------------------------------------------------------------------
# 4. SOLICITAR ASESORÍA (N8N)
# -------------------------------------------------------------------
elif opcion == "📩 4. Solicitar Asesoría (n8n)":
    st.title("📩 4. Solicitar Asesoría (Automatización n8n)")
    st.write("Déjanos tus datos para procesar tu solicitud automáticamente:")
    
    with st.form("formulario_n8n"):
        nombre = st.text_input("Nombre completo:")
        correo = st.text_input("Correo electrónico:")
        mensaje = st.text_area("¿En qué proyecto necesitas ayuda?")
        submit = st.form_submit_button("Enviar solicitud")
        
        if submit:
            st.success(f"¡Gracias {nombre}! Solicitud enviada correctamente mediante el webhook de n8n.")

# -------------------------------------------------------------------
# 5. DASHBOARD & MODELO ML
# -------------------------------------------------------------------
elif opcion == "📊 5. Dashboard & Modelo ML":
    st.title("📊 5. Dashboard & Modelo de Machine Learning")
    st.write("Visualización de datos y modelo predictivo.")
    st.info("Espacio para los gráficos de Pandas / Matplotlib y las predicciones de Scikit-learn.")

# -------------------------------------------------------------------
# 6. DECLARACIÓN DE IA & CIERRE
# -------------------------------------------------------------------
elif opcion == "💡 6. Declaración de IA & Cierre":
    st.title("💡 6. Declaración del Uso de IA & Conclusiones")
    st.markdown("""
    * **Herramientas de IA utilizadas:** D-ID/Canva (Avatar Parlante), Gemini API / Botpress (Chatbot), n8n (Automatización), Scikit-Learn (Machine Learning).
    * **Impacto:** Innovación con conciencia para impulsar soluciones sostenibles y eficientes.
    """)
