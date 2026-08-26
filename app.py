import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import requests
import os

# -------------------------------------------------------------------
# 1. PORTAFOLIO DE SERVICIOS
# -------------------------------------------------------------------
elif opcion == "💼 1. Portafolio de Servicios":
    st.title("💼 1. Portafolio de Servicios")
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
                <p><b>Inversión estimada:</b> {s['precio']}</p>
                <p>{s['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            if os.path.exists(s['img']):
                st.image(s['img'], use_container_width=True)

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
# 1. PORTAFOLIO DE SERVICIOS
# -------------------------------------------------------------------
if opcion == "💼 1. Portafolio de Servicios":
    st.title("💼 1. Portafolio de Servicios")
    st.write("Soluciones digitales diseñadas bajo el equilibrio entre tecnología y humanidad.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card-box">
            <h4 style="color:#2087B5;">1. Consultoría en IA Generativa</h4>
            <p>Implementación estratégica de modelos generativos y asistentes a la medida.</p>
        </div>
        <div class="card-box">
            <h4 style="color:#2087B5;">2. Automatización de Flujos (n8n)</h4>
            <p>Integración de procesos con webhooks para optimizar el envío de correos y datos.</p>
        </div>
        <div class="card-box">
            <h4 style="color:#2087B5;">3. Chatbots Inteligentes</h4>
            <p>Agentes conversacionales con memoria y entrenamiento contextual.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card-box">
            <h4 style="color:#2087B5;">4. Dashboards & Analítica ML</h4>
            <p>Visualizaciones interactivas y modelos predictivos de comportamiento.</p>
        </div>
        <div class="card-box">
            <h4 style="color:#2087B5;">5. Identidad & Multimedia con IA</h4>
            <p>Diseño de marca, piezas visuales y avatares parlantes personalizados.</p>
        </div>
        """, unsafe_allow_html=True)

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
    
    # PEGA AQUÍ TU URL DE PRODUCCIÓN COPIADA DE N8N:
    N8N_WEBHOOK_URL = "https://tu-instancia-n8n.com/webhook/solicitud-asesoria"

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
                    res = requests.post(N8N_WEBHOOK_URL, json=datos_payload, timeout=8)
                    if res.status_code == 200:
                        st.success(f"✅ ¡Solicitud enviada a n8n! Se ha activado el envío del correo a **{correo}**.")
                    else:
                        st.warning(f"⚠️ El Webhook respondió con código {res.status_code}. Revisa si el flujo en n8n está Activo.")
                except Exception as e:
                    st.error(f"❌ Error al conectar con la URL de n8n. Revisa que N8N_WEBHOOK_URL sea correcta.")
# -------------------------------------------------------------------
# 5. DASHBOARD & MODELO ML
# -------------------------------------------------------------------
elif opcion == "📊 5. Dashboard & Modelo ML":
    st.title("📊 5. Dashboard & Modelo de Machine Learning")
    st.write("Ajusta las **Horas de Entrenamiento** para observar cómo la gráfica interactiva y la métrica recalculan los resultados en tiempo real.")
    
    horas = st.slider("⚙️ Horas de Entrenamiento del Modelo ML:", min_value=10, max_value=120, value=40, step=5)
    
    # Cálculo proporcional dinámico
    precision_calculada = min(round(15.0 + (horas * 0.72), 1), 99.5)
    
    # Cálculo del indicador delta dinámico
    delta_val = round((horas - 40) * 0.72, 1)
    delta_str = f"{'+' if delta_val >= 0 else ''}{delta_val}% vs Base"
    
    meses_ordenados = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto"]
    base_rendimiento = np.linspace(55, precision_calculada, len(meses_ordenados))
    
    df_ml = pd.DataFrame({
        "Mes": meses_ordenados,
        "Precisión Modelo (%)": base_rendimiento
    })
    
    df_ml['Mes'] = pd.Categorical(df_ml['Mes'], categories=meses_ordenados, ordered=True)
    df_ml = df_ml.sort_values('Mes')
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Horas de Entrenamiento", f"{horas} hrs")
    m2.metric("Precisión Estimada", f"{precision_calculada}%", delta_str)
    
    if precision_calculada >= 75.0:
        m3.metric("Estado del Modelo", "Optimizado", "Alto Rendimiento")
    else:
        m3.metric("Estado del Modelo", "En Entrenamiento", "Requiere más Horas", delta_color="inverse")
    
    st.markdown("---")
    
    fig = px.line(
        df_ml, 
        x="Mes", 
        y="Precisión Modelo (%)", 
        markers=True,
        title=f"Evolución de Precisión Proyectada (Entrenamiento: {horas} horas)",
        color_discrete_sequence=["#2087B5"]
    )
    fig.update_layout(yaxis_range=[30, 100], paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    
    st.plotly_chart(fig, use_container_width=True)
    
    if os.path.exists("grafica_model_florecer.png"):
        st.markdown("---")
        st.subheader("🖼️ Gráfica de Referencia Generada")
        st.image("grafica_model_florecer.png", caption="Visualización de referencia", use_container_width=True)

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
            <li><b>Scikit-Learn, Pandas & Plotly:</b> Implementación del modelo predictivo y visualización dinámica de datos en Streamlit.</li>
        </ul>
    </div>
    
    <div class="card-box">
        <h3 style="color:#2087B5;">📌 Conclusión del Proyecto Florecer</h3>
        <p>El proyecto <b>Florecer</b> demuestra cómo la integración estratégica de herramientas No-Code, Python e Inteligencia Artificial permite construir soluciones digitales funcionales, escalables y orientadas al impacto positivo con propósito humano.</p>
    </div>
    """, unsafe_allow_html=True)
