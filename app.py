import streamlit as st
import random

# Configurazione Pagina
st.set_page_config(page_title="Savein's Moto", page_icon="🏍️", layout="wide")

# Database semplificato per test (Puoi espanderlo seguendo questo schema)
moto_database = {
    "KTM": {
        "2010": {"modello": "125 EXC", "immagine": "https://img.auto-data.net/moto/ktm-125-exc-2010.jpg", "motore": "2T, 124.8 cc", "telaio": "Cromo-molibdeno", "cambio": "6 marce"},
        "2026": {"modello": "125 EXC TBI", "immagine": "https://p.vitalmx.com/photos/users/64/photos/151608/s1600_2024_KTM_150_XC_W_1.jpg", "motore": "2T iniezione TBI", "telaio": "Nuovo design 2026", "cambio": "6 marce"}
    },
    "TM Racing": {
        "2024": {"modello": "SMR 125", "immagine": "https://www.tmracing.it/wp-content/uploads/2023/11/SMR-125-2-1.jpg", "motore": "2T valvola elettronica", "telaio": "Alluminio", "cambio": "6 marce"}
    }
}

# Gestione navigazione
if 'pagina_corrente' not in st.session_state:
    st.session_state.pagina_corrente = 'home'

# --- STILE CSS ---
st.markdown("""
<style>
    .stApp { background-color: #050505; color: white; }
    .home-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 5em;
        text-align: center;
        background: linear-gradient(90deg, #ff0000, #007bff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff0000, #007bff);
        color: white; border: none; padding: 15px 30px;
        font-size: 1.5em; border-radius: 50px;
        box-shadow: 0 0 20px rgba(255, 0, 0, 0.5);
    }
    .moto-img img {
        border: 2px solid #007bff;
        border-radius: 20px;
        box-shadow: 0 0 40px rgba(255, 255, 255, 0.8); /* Effetto luminescenza */
    }
</style>
""", unsafe_allow_html=True)

# --- LOGICA PAGINE ---
if st.session_state.pagina_corrente == 'home':
    st.markdown('<p class="home-title">Savein\'s Moto</p>', unsafe_allow_html=True)
    st.write("##")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 ENTRA NEL CATALOGO", use_container_width=True):
            st.session_state.pagina_corrente = 'catalogo'
            st.rerun()

elif st.session_state.pagina_corrente == 'catalogo':
    if st.button("⬅️ HOME"):
        st.session_state.pagina_corrente = 'home'
        st.rerun()

    st.title("📂 Catalogo 125cc")
    
    col_m, col_a = st.columns(2)
    with col_m:
        marca = st.selectbox("Marca", ["KTM", "TM Racing", "HUSQVARNA", "GASGAS", "YAMAHA YZ", "SUZUKI RM", "KAWASAKI KX"])
    with col_a:
        anno = st.selectbox("Anno", ["2010", "2011", "2014", "2015", "2018", "2019", "2022", "2023", "2026"])

    st.divider()

    if marca in moto_database and anno in moto_database[marca]:
        moto = moto_database[marca][anno]
        c1, c2 = st.columns([1.2, 1])
        
        with c1:
            # Qui ho inserito l'effetto 4:3 e luminescenza tramite HTML
            st.markdown(f'''
                <div class="moto-img">
                    <img src="{moto['immagine']}" style="width:100%; aspect-ratio:4/3; object-fit:cover;">
                </div>
            ''', unsafe_allow_html=True)
        
        with c2:
            st.header(f"{marca} {moto['modello']}")
            st.subheader(f"Anno: {anno}")
            st.info(f"🔥 **Motore:** {moto['motore']}")
            st.info(f"🏗️ **Telaio:** {moto['telaio']}")
            st.info(f"⚙️ **Cambio:** {moto['cambio']}")
            st.write("---")
            st.write("Dati tecnici completi aggiornati per il modello selezionato.")
    else:
        st.warning("Dati non ancora inseriti per questa combinazione. Prova KTM 2010 o 2026!")
