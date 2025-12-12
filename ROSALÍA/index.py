import streamlit as st
import datetime
import base64

# ---- CONFIGURACIÓN BÁSICA ----
st.set_page_config(page_title="Cuenta regresiva", layout="centered")

# ---- CARGAR IMAGEN Y CONVERTIR A BASE64 (sin usar URL) ----
def cargar_imagen(ruta):
    with open(ruta, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = cargar_imagen("ROSALÍA/rosi.jpeg")

# ---- CSS PARA USAR IMAGEN COMO FONDO ----
fondo_css = f"""
<style>
    body {{
        margin: 0;
        padding: 0;
        background-image: url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .fondo {{
        background: rgba(0, 0, 0, 0.55);
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        color: white;
        backdrop-filter: blur(4px);
        box-shadow: 0 0 20px rgba(0,0,0,0.4);
    }}

    h1 {{
        font-size: 32px;
        color: #fff;
    }}

    .tiempo {{
        font-size: 45px;
        font-weight: bold;
        margin-top: 15px;
    }}
</style>
"""

st.markdown(fondo_css, unsafe_allow_html=True)

# ---- CONTENEDOR ----
st.markdown("<div class='fondo'>", unsafe_allow_html=True)

st.markdown("<h1>Faltan para el 19 de Agosto 2026:</h1>", unsafe_allow_html=True)

# ---- LÓGICA DEL CONTADOR ----
objetivo = datetime.datetime(2026, 8, 19, 0, 0, 0)
ahora = datetime.datetime.now()
diferencia = objetivo - ahora

if diferencia.total_seconds() <= 0:
    st.markdown("<div class='tiempo'>¡Llegó el día!</div>", unsafe_allow_html=True)
else:
    dias = diferencia.days
    horas, resto = divmod(diferencia.seconds, 3600)
    minutos, segundos = divmod(resto, 60)

    st.markdown(
        f"<div class='tiempo'>{dias} días {horas} hrs {minutos} min {segundos} s</div>",
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)

# ---- AUTO-REFRESH CADA SEGUNDO ----
st.experimental_rerun()
