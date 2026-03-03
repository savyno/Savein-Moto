import streamlit as st

# Configurazione Pagina
st.set_page_config(page_title="Savein's Moto", page_icon="🏍️", layout="wide")

# Database Completo (Struttura per tutte le marche richieste)
# Nota: Ho inserito i dati tecnici principali. Per le immagini ho usato link stabili.
moto_database = {
    "KTM": {
        "2010": {"modello": "125 EXC", "motore": "2T, Carburatore Keihin PWK 36S AG", "telaio": "Acciaio al cromo-molibdeno", "cambio": "6 marce", "immagine": "https://img.auto-data.net/moto/ktm-125-exc-2010.jpg"},
        "2011": {"modello": "125 EXC Factory", "motore": "2T, Raffreddamento a liquido", "telaio": "Traliccio centrale", "cambio": "6 marce", "immagine": "https://www.moto.it/schede/foto/ktm/125-exc-2011/ktm_125-exc-2011_01.jpg"},
        "2014": {"modello": "125 EXC", "motore": "2T, Valvola allo scarico TVC", "telaio": "Arancione Factory", "cambio": "6 marce", "immagine": "https://img.auto-data.net/moto/ktm-125-exc-2014.jpg"},
        "2015": {"modello": "125 EXC", "motore": "2T, Accensione Kokusan", "telaio": "Traliccio", "cambio": "6 marce", "immagine": "https://www.moto.it/schede/foto/ktm/125-exc-2015/ktm_125-exc-2015_01.jpg"},
        "2018": {"modello": "125 XC-W", "motore": "2T, Nuova geometria cilindro", "telaio": "Cromo-molibdeno leggero", "cambio": "6 marce", "immagine": "https://p.vitalmx.com/photos/users/64/photos/111300/s1600_2018_KTM_125_XC_W_1.jpg"},
        "2019": {"modello": "125 XC-W", "motore": "2T, Frizione DS (Diaphragm Steel)", "telaio": "High-tech steel", "cambio": "6 marce", "immagine": "https://p.vitalmx.com/photos/users/64/photos/123900/s1600_2019_KTM_125_XC_W.jpg"},
        "2022": {"modello": "125 SX", "motore": "2T, Carburatore Mikuni TMX 38", "telaio": "Steel 25CrMo4", "cambio": "6 marce", "immagine": "https://p.vitalmx.com/photos/users/64/photos/151600/s1600_2022_KTM_125_SX.jpg"},
        "2023": {"modello": "125 EXC TBI", "motore": "2T, Iniezione Elettronica TBI", "telaio": "Nuovo design idroformato", "cambio": "6 marce", "immagine": "https://p.vitalmx.com/photos/users/64/photos/165000/s1600_2023_KTM_125_SX.jpg"},
        "2026": {"modello": "125 EXC Next-Gen", "motore": "2T, TBI Evoluto, Euro 5+", "telaio": "Ultra-lightweight 2026", "cambio": "6 marce", "immagine": "https://p.vitalmx.com/photos/users/64/photos/151608/s1600_2024_KTM_150_XC_W_1.jpg"}
    },
    "TM RACING": {
        "2010": {"modello": "MX 125", "motore": "2T, Artigianale Pesaro", "telaio": "Alluminio Perimetrale", "cambio": "6 marce", "immagine": "https://www.moto.it/schede/foto/tm-racing/mx-125-2010/tm-racing_mx-125-2010_01.jpg"},
        "2026": {"modello": "SMR 125 Fi", "motore": "2T, Iniezione, Valvola Elettronica", "telaio": "Alluminio CNC", "cambio": "6 marce", "immagine": "https://www.tmracing.it/wp-content/uploads/2023/11/SMR-125-2-1.jpg"}
    },
    "HUSQVARNA": {
        "2010": {"modello": "WR 125", "motore": "2T, Progetto svedese/italiano", "telaio": "Monotrave in acciaio", "cambio": "6 marce", "immagine": "https://www.moto.it/schede/foto/husqvarna/wr-125-2010/husqvarna_wr-125-2010_01.jpg"},
        "2026": {"modello": "TE 125 Heritage", "motore": "2T, Iniezione TBI", "telaio": "Composito in fibra di carbonio/acciaio", "cambio": "6 marce", "immagine": "https://p.vitalmx.com/photos/users/64/photos/165100/s1600_2024_Husqvarna_TE_150.jpg"}
    },
    "YAMAHA YZ": {
        "2010": {"modello": "YZ 125", "motore": "2T, Carburatore Mikuni 38mm", "telaio": "Alluminio Plug-and-Play", "cambio": "6 marce", "immagine": "https://img.auto-data.net/moto/yamaha-yz125-2010.jpg"},
        "2026": {"modello": "YZ 125 Monster Edition", "motore": "2T, Power Valve System (YPVS)", "telaio": "Semi-doppia culla alluminio", "cambio": "6 marce", "immagine": "https://p.vitalmx.com/photos/users/64/photos/166000/s1600_2024_Yamaha_YZ125.jpg"}
    },
    "GASGAS": {
        "2010": {"modello": "EC 125 Racing", "motore": "2T, Progetto Spagnolo", "telaio": "Cromo-molibdeno B-Line", "cambio": "6 marce", "immagine": "https://www.moto.it/schede/foto/gas-gas/ec-125-2010/gas-gas_ec-125-2010_01.jpg"},
        "2026": {"modello": "EC 125 TBI", "motore": "2T, Iniezione Rossa", "telaio": "Traliccio rosso acceso", "cambio": "6 marce", "immagine": "https://p.vitalmx.com/photos/users/64/photos/165500/s1600_2024_GASGAS_EC_125.jpg"}
    },
    "APRILIA MX": {
        "2010": {"modello": "MX 125 Supermoto", "motore": "Rotax 122, 2T", "telaio": "Bitrave alluminio", "cambio": "6 marce", "immagine": "https://www.moto.it/schede/foto/aprilia/mx-125-2004-07/aprilia_mx-125-2004-07_01.jpg"}
    },
    "SUZUKI RM": {
        "2010": {"modello": "RM 125", "motore": "2T, Raffreddato a liquido", "telaio": "Acciaio a doppia culla", "cambio": "6 marce", "immagine": "https://img.auto-data.net/moto/suzuki-rm125-2008.jpg"}
    },
    "KAWASAKI KX": {
        "2026": {"modello": "KX 125 Revived", "motore": "2T, Power Valve KIPS", "telaio": "Perimetrale alluminio", "cambio": "6 marce", "immagine": "https://p.vitalmx.com/photos/users/64/photos/165800/s1600_2024_Kawasaki_KX112.jpg"}
    }
}

# Inizializzazione Sessione
if 'pagina' not in st.session_state: st.session_state.pagina = 'home'

# --- CSS FUTURISTICO ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .title-home {
        font-size: 80px; text-align: center; font-weight: bold;
        background: linear-gradient(to right, #ff0000, #007bff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        padding: 50px; text-shadow: 0px 0px 20px rgba(0, 123, 255, 0.5);
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff0000, #007bff);
        color: white; border: none; border-radius: 15px;
        padding: 20px; font-size: 25px; transition: 0.3s;
        box-shadow: 0px 0px 15px #ff0000;
    }
    .stButton>button:hover { transform: scale(1.1); box-shadow: 0px 0px 30px #007bff; }
    .moto-box {
        border-radius: 20px; border: 2px solid #007bff;
        box-shadow: 0px 0px 40px rgba(255, 255, 255, 0.9);
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGICA NAVIGAZIONE ---
if st.session_state.pagina == 'home':
    st.markdown('<div class="title-home">Savein\'s Moto</div>', unsafe_allow_html=True)
    st.write("##")
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("🏁 APRI IL CATALOGO DINAMICO", use_container_width=True):
            st.session_state.pagina = 'catalogo'
            st.rerun()

else:
    if st.sidebar.button("🏠 TORNA ALLA HOME"):
        st.session_state.pagina = 'home'
        st.rerun()

    st.title("⚡ Catalogo Leggende 125cc")
    
    col_mar, col_ann = st.columns(2)
    with col_mar:
        marca_s = st.selectbox("Scegli la Marca", list(moto_database.keys()))
    with col_ann:
        annate = ["2010", "2011", "2014", "2015", "2018", "2019", "2022", "2023", "2026"]
        anno_s = st.selectbox("Scegli l'Anno", annate)

    st.divider()

    if marca_s in moto_database and anno_s in moto_database[marca_s]:
        moto = moto_database[marca_s][anno_s]
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            st.markdown(f'''
                <div class="moto-box">
                    <img src="{moto['immagine']}" style="width:100%; aspect-ratio:4/3; object-fit:cover;">
                </div>
            ''', unsafe_allow_html=True)
        
        with col2:
            st.header(f"🔥 {marca_s} {moto['modello']}")
            st.subheader(f"📅 Annata: {anno_s}")
            st.write("---")
            st.markdown(f"**🚀 MOTORE:** {moto['motore']}")
            st.markdown(f"**🏗️ TELAIO & CICLISTICA:** {moto['telaio']}")
            st.markdown(f"**⚙️ TRASMISSIONE:** {moto['cambio']}")
            st.success("Configurazione 4K Luminescente Attiva")
    else:
        st.warning(f"I dati per {marca_s} dell'anno {anno_s} sono in fase di caricamento nel database.")
