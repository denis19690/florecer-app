import streamlit as st
import pandas as pd
from PIL import Image
import os
import requests

# 1. Configuración de la página web
st.set_page_config(
    page_title="Florecer - Soluciones Inteligentes con IA",
    page_icon="🌱",
    layout="wide"
)

# Estilos CSS personalizados para forzar la paleta institucional de Florecer
st.markdown("""
    <style>
    /* Fondo general beige suave */
    .stApp {
        background-color: #FDFBF7 !important;
    }
    
    /* Textos generales y títulos */
    h1, h2, h3, h4, h5, h6, p, label, span, div {
        color: #212121 !important;
    }

    .main-title {
        color: #FF7043 !important;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0px;
    }
    
    .slogan {
        color: #26A69A !important;
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin-bottom: 20px;
    }

    /* Cajas de texto e insumos del formulario en blanco con borde agua marina */
    div[data-baseweb="input"] > div, 
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border: 1.5px solid #26A69A !important;
        border-radius: 8px !important;
    }

    input {
        color: #212121 !important;
        background-color: #FFFFFF !important;
    }

    /* Opciones del menú desplegable */
    div[data-baseweb="popover"], 
    ul[data-baseweb="menu"] {
        background-color: #FFFFFF !important;
    }

    li[role="option"] {
        background-color: #FFFFFF !important;
        color: #212121 !important;
    }

    /* Botón de envío Terracota */
    div.stButton > button, div[data-testid="stFormSubmitButton"] > button {
        background-color: #FF7043 !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 16px !important;
        padding: 10px 24px !important;
        width: 100% !important;
    }

    div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        background-color: #26A69A !important;
        color: #FFFFFF !important;
    }

    /* Tarjetas de servicios */
    .card-florecer {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #26A69A;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }

    .card-florecer h4 {
        color: #FF7043 !important;
        margin-top: 0;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Encabezado e Identidad de Marca
col_logo, col_text = st.columns([1, 2])

logo_encontrado = None
posibles_nombres = ['logo.png.jpg', 'logo.jpg', 'logo.png', 'logo.jpeg']
for nombre in posibles_nombres:
    if os.path.exists(nombre):
        logo_encontrado = nombre
        break

with col_logo:
    if logo_encontrado:
        logo_img = Image.open(logo_encontrado)
        st.image(logo_img, width=260)
    else:
        st.warning("Coloca la imagen del logo en la carpeta.")

with col_text:
    st.markdown('<p class="main-title">FLORECER</p>', unsafe_allow_html=True)
    st.markdown('<p class="slogan">Innovar con conciencia. Crecer para impactar.</p>', unsafe_allow_html=True)
    st.write("""
        **Misión:** Acercar la inteligencia artificial y la tecnología a pequeños negocios de forma práctica, accesible y sostenible.  
        **Visión:** Ser el puente digital que impulse a los emprendedores locales a optimizar sus procesos y escalar con propósito.
    """)

st.divider()

# 3. Menú de Navegación por Pestañas
tab_servicios, tab_modelo, tab_chatbot = st.tabs([
    "🛍️ Portafolio de Soluciones", 
    "🧠 Decisiones Florecer (ML)", 
    "🤖 Asistente Florecer"
])

# --- PESTAÑA 1: PORTAFOLIO Y FORMULARIO ---
with tab_servicios:
    st.markdown("<h3 style='color: #FF7043;'>Nuestras 5 Soluciones Tecnológicas</h3>", unsafe_allow_html=True)
    st.write("Demostración de capacidades diseñadas para potenciar pequeños negocios:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card-florecer">
            <h4>🤖 1. Asistente Florecer</h4>
            <p>Chatbot interactivo con IA para atención a clientes 24/7 y orientación de servicios.</p>
            <small style="color: #26A69A;"><b>Precio Simulado: $49 USD/mes</b></small>
        </div>
        <div class="card-florecer">
            <h4>⚙️ 2. Flujo Automático</h4>
            <p>Automatización de tareas repetitivas como sincronización de pedidos y confirmación por correo.</p>
            <small style="color: #26A69A;"><b>Precio Simulado: $79 USD/mes</b></small>
        </div>
        <div class="card-florecer">
            <h4>📊 3. Radar de Clientes</h4>
            <p>Dashboard analítico interactivo para organizar y visualizar patrones de venta.</p>
            <small style="color: #26A69A;"><b>Precio Simulado: $99 USD/mes</b></small>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card-florecer">
            <h4>🧠 4. Decisiones Florecer</h4>
            <p>Modelo predictivo de Machine Learning para clasificar clientes y predecir oportunidades.</p>
            <small style="color: #26A69A;"><b>Precio Simulado: $120 USD/mes</b></small>
        </div>
        <div class="card-florecer">
            <h4>🌱 5. Impulso Florecer</h4>
            <p>Generación automática de contenidos, copys publicitarios y piezas multimedia con IA.</p>
            <small style="color: #26A69A;"><b>Precio Simulado: $59 USD/mes</b></small>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    
    # FORMULARIO DE CONTACTO
    st.markdown("<h3 style='color: #FF7043;'>📩 Solicitar Asesoría Personalizada</h3>", unsafe_allow_html=True)
    st.write("Completa tus datos para activar nuestro flujo de trabajo automatizado en n8n:")

    WEBHOOK_URL = "https://denisgreenway.app.n8n.cloud/webhook/florecer-contacto"

    with st.form("form_contacto_n8n"):
        c_nombre, c_correo = st.columns(2)
        with c_nombre:
            nombre = st.text_input("Tu Nombre Completo:")
        with c_correo:
            email = st.text_input("Tu Correo Electrónico:")

        c_empresa, c_servicio = st.columns(2)
        with c_empresa:
            empresa = st.text_input("Nombre de tu Negocio / Emprendimiento:")
        with c_servicio:
            servicio_interes = st.selectbox(
                "Servicio de Interés:", 
                ["Asistente Florecer", "Flujo Automático", "Radar de Clientes", "Decisiones Florecer", "Impulso Florecer"]
            )

        boton_enviar = st.form_submit_button("🚀 Solicitar Información Automática")

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
                    st.success("✨ ¡Solicitud enviada con éxito! Revisa tu bandeja de entrada de correo electrónico.")
                else:
                    st.warning("⚠️ La solicitud se envió pero n8n devolvió un estado. Verifica que el nodo Webhook esté en ejecución.")
            except Exception as e:
                st.error(f"Error al conectar con la automatización: {e}")
        else:
            st.warning("Por favor completa los campos de Nombre, Correo y Negocio.")

# --- PESTAÑA 2: MACHINE LEARNING ---
with tab_modelo:
    st.markdown("<h3 style='color: #FF7043;'>🧠 Decisiones Florecer (Machine Learning)</h3>", unsafe_allow_html=True)
    st.write("Diagnóstico para la clasificación y adopción de tecnología e inteligencia artificial en MiPyMEs.")
    
    col_graph, col_desc = st.columns([2, 1])
    
    with col_graph:
        grafica_encontrada = None
        posibles_graficas = ['grafica_model_florecer.png', 'grafica.png', 'modelo.png']
        for g in posibles_graficas:
            if os.path.exists(g):
                grafica_encontrada = g
                break
                
        if grafica_encontrada:
            st.image(Image.open(grafica_encontrada), use_container_width=True)
        else:
            st.info("📌 Guarda la imagen 'grafica_model_florecer.png' en esta misma carpeta para mostrar el gráfico.")
            
    with col_desc:
        st.markdown("<h4 style='color: #26A69A;'>Diagnóstico del Modelo</h4>", unsafe_allow_html=True)
        st.write("""
        - **Alto Impacto (Naranja):** Negocios con alto volumen de trabajo manual y buena presencia digital. Listos para IA.
        - **Impacto Medio (Agua Marina):** Negocios en transición que requieren automatizaciones por etapas.
        - **Impacto Bajo (Gris/Amarillo):** Requieren capacitación digital básica prioritaria.
        """)

# --- PESTAÑA 3: CHATBOT ---
with tab_chatbot:
    st.markdown("<h3 style='color: #FF7043;'>🤖 Asistente Florecer</h3>", unsafe_allow_html=True)
    st.write("Consulta nuestra base de conocimiento interactiva sobre la visión y servicios de Florecer:")
    
    preguntas_respuestas = {
        "¿Qué es Florecer?": "Es una plataforma de soluciones tecnológicas impulsadas por IA que ayuda a pequeños negocios a digitalizarse y crecer de forma consciente.",
        "¿A quién ayuda Florecer?": "A emprendedores y pequeños negocios que buscan modernizar sus procesos y ahorrar tiempo.",
        "¿Qué problema busca resolver?": "Elimina la brecha tecnológica y la sobrecarga de trabajo manual transformando tareas en flujos inteligentes.",
        "¿Cómo funciona el modelo de Machine Learning?": "Analiza las horas en tareas repetitivas y el nivel digital del negocio para clasificar su oportunidad de adopción de IA.",
        "¿Por qué Florecer une tecnología y sostenibilidad?": "Porque la tecnología debe optimizar recursos, reducir el desperdicio de tiempo y ayudar a prosperar con propósito."
    }
    
    opcion_seleccionada = st.radio(
        "Selecciona una pregunta de la lista:",
        list(preguntas_respuestas.keys())
    )
    
    st.markdown("---")
    if opcion_seleccionada:
        st.info(f"**Respuesta:** {preguntas_respuestas[opcion_seleccionada]}")