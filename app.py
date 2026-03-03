import streamlit as st
import random

# Configurazione Pagina - Titolo e Icona nella scheda del browser
st.set_page_config(page_title="Savein's Moto", page_icon="🏍️", layout="wide")

# Database delle moto (Strutturato per annate e modelli - ESEMPIO)
# Per un database completo, considera l'integrazione di un file esterno o un vero database.
moto_database = {
    "KTM": {
        "2010": { "modello": "125 EXC", "immagine": "path/to/ktm_2010.jpg", "motore": "2T, 125cc", "ciclistica": "Telaio tubolare...", "freni": "Brembo..." },
        "2012": { "modello": "125 EXC", "immagine": "path/to/ktm_2012.jpg", "motore": "2T, 125cc", "ciclistica": "Telaio aggiornato...", "freni": "Brembo..." },
        # ... aggiungi altre annate e modelli
        "2026": { "modello": "125 EXC", "immagine": "path/to/ktm_2026.jpg", "motore": "2T TPI, 125cc", "ciclistica": "Nuova generazione...", "freni": "Brembo High Performance..." },
    },
    "TM Racing": {
        "2010": { "modello": "SMR 125", "immagine": "path/to/tm_2010.jpg", "motore": "2T, 125cc", "ciclistica": "Telaio perimetrale...", "freni": "Brembo/Nissin..." },
        "2012": { "modello": "SMR 125", "immagine": "path/to/tm_2012.jpg", "motore": "2T, 125cc", "ciclistica": "Telaio affinato...", "freni": "Brembo/Nissin..." },
        # ... aggiungi altre annate e modelli
        "2026": { "modello": "SMR 125", "immagine": "path/to/tm_2026.jpg", "motore": "2T Iniezione, 125cc", "ciclistica": "Telaio alluminio...", "freni": "Brembo Monoblocco..." },
    },
    # ... aggiungi altre marche: APRILIA MX, HUSQVARNA, YZ, SUZUKI RM, GASGAS, KX
}

# Funzione per generare anni con intervallo di 2
def genera_anni(inizio, fine):
    anni = []
    anno_corrente = inizio
    while anno_corrente <= fine:
        anni.append(str(anno_corrente))
        anni.append(str(anno_corrente + 1))
        anno_corrente += 4  # Salta 2 anni
    return anni

# Genera la lista degli anni validi
anni_validi = genera_anni(2010, 2026)

# Gestione dello stato della pagina (Home o Catalogo)
if 'pagina_corrente' not in st.session_state:
    st.session_state.pagina_corrente = 'home'

# --- STILE CSS PERSONALIZZATO (Futuristico) ---
st.markdown("""
<style>
    /* Sfondo e colori globali */
    .stApp {
        background-color: #0d1117; /* Nero profondo */
        color: #e6edf3; /* Bianco sporco */
        font-family: 'Exo 2', sans-serif; /* Font futuristico */
    }

    /* Titolo Home */
    .home-title {
        font-family: 'Orbitron', sans-serif; /* Font molto futuristico */
        font-size: 6em;
        font-weight: bold;
        text-align: center;
        margin-top: 10vh;
        background: linear-gradient(90deg, #ff0000, #007bff, #ff0000); /* Sfumatura rosso-blu-rosso */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: neon 2s ease-in-out infinite alternate;
    }

    @keyframes neon {
        from { text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000, 0 0 30px #ff0000; }
        to { text-shadow: 0 0 20px #007bff, 0 0 30px #007bff, 0 0 40px #007bff; }
    }

    /* Contenitore pulsante Home */
    .home-button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 50vh;
        position: relative;
    }

    /* Pulsante dinamico animato */
    .stButton>button {
        background: linear-gradient(45deg, #ff0000, #007bff); /* Sfumatura rosso-blu */
        border: none;
        border-radius: 10px;
        padding: 20px 40px;
        font-size: 2em;
        font-weight: bold;
        color: #ffffff;
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s, background-position 0.5s;
        box-shadow: 0 5px 15px rgba(255, 0, 0, 0.4), 0 5px 15px rgba(0, 123, 255, 0.4);
        background-size: 200% auto;
        animation: glow 1.5s ease-in-out infinite alternate, pulsa 2s infinite;
    }

    .stButton>button:hover {
        transform: scale(1.1);
        box-shadow: 0 10px 30px rgba(255, 0, 0, 0.6), 0 10px 30px rgba(0, 123, 255, 0.6);
        background-position: right center;
    }

    @keyframes glow {
        from { box-shadow: 0 0 10px rgba(255, 0, 0, 0.6), 0 0 10px rgba(0, 123, 255, 0.6); }
        to { box-shadow: 0 0 20px rgba(255, 0, 0, 1), 0 0 20px rgba(0, 123, 255, 1); }
    }

    @keyframes pulsa {
        0% { transform: scale(1); }
        50% { transform: scale(1.03); }
        100% { transform: scale(1); }
    }

    /* Decorazioni a tema intorno al pulsante */
    .decoration-1 { position: absolute; top: -20px; left: -30px; font-size: 3em; color: #ff0000; animation: ruota 5s linear infinite; }
    .decoration-2 { position: absolute; top: -30px; right: -20px; font-size: 3em; color: #007bff; animation: ruota-inversa 5s linear infinite; }
    .decoration-3 { position: absolute; bottom: -30px; left: -20px; font-size: 3em; color: #007bff; animation: ruota-inversa 5s linear infinite; }
    .decoration-4 { position: absolute; bottom: -20px; right: -30px; font-size: 3em; color: #ff0000; animation: ruota 5s linear infinite; }

    @keyframes ruota { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    @keyframes ruota-inversa { from { transform: rotate(0deg); } to { transform: rotate(-360deg); } }

    /* Immagini nel Catalogo (Effetto 4K High Luminescence) */
    .catalogue-image img {
        border-radius: 15px;
        box-shadow: 0 0 30px rgba(255, 255, 255, 0.7); /* Luminescenza massima */
        transition: transform 0.3s, box-shadow 0.3s;
        aspect-ratio: 4 / 3; /* Forza l'aspect ratio 4:3 */
        object-fit: cover; /* Adatta l'immagine senza distorsioni */
    }

    .catalogue-image img:hover {
        transform: scale(1.05);
        box-shadow: 0 0 40px rgba(255, 255, 255, 0.9);
    }

    /* Titolo Catalogo */
    .catalogue-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 3em;
        text-align: center;
        margin-bottom: 20px;
        color: #007bff; /* Blu futuristico */
    }

    /* Stile per le specifiche */
    .spec-category { font-weight: bold; color: #ff0000; margin-top: 10px; }
    .spec-value { color: #e6edf3; margin-left: 10px; }

</style>
""", unsafe_allow_html=True)

# --- PAGINA HOME ---
if st.session_state.pagina_corrente == 'home':
    st.markdown('<h1 class="home-title">Savein\'s Moto</h1>', unsafe_allow_html=True)

    # Contenitore per il pulsante e le decorazioni
    st.markdown('<div class="home-button-container">', unsafe_allow_html=True)
    
    # Decorazioni
    st.markdown('<div class="decoration-1">⚙️</div>', unsafe_allow_html=True)
    st.markdown('<div class="decoration-2">⚡</div>', unsafe_allow_html=True)
    st.markdown('<div class="decoration-3">🏍️</div>', unsafe_allow_html=True)
    st.markdown('<div class="decoration-4">🔥</div>', unsafe_allow_html=True)

    # Pulsante centrale
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 APRI CATALOGO", use_container_width=True):
            st.session_state.pagina_corrente = 'catalogo'
            st.rerun() # Ricarica per mostrare il catalogo

    st.markdown('</div>', unsafe_allow_html=True) # Fine contenitore pulsante

# --- PAGINA CATALOGO ---
elif st.session_state.pagina_corrente == 'catalogo':
    st.markdown('<h1 class="catalogue-title">Catalogo Moto 125</h1>', unsafe_allow_html=True)

    # Pulsante per tornare alla Home
    if st.button("⬅️ Torna alla Home"):
        st.session_state.pagina_corrente = 'home'
        st.rerun()

    st.write("---")

    # Filtri di selezione (Marca, Anno)
    col1, col2 = st.columns(2)
    with col1:
        marche_disponibili = list(moto_database.keys())
        marca_scelta = st.selectbox("Seleziona la Marca", marche_disponibili)
    with col2:
        # Usa solo gli anni validi per il database (potrebbe essere vuoto per certe marche/anni)
        anni_disponibili_marca = list(moto_database[marca_scelta].keys())
        anno_scelto = st.selectbox("Seleziona l'Annata", anni_disponibili_marca)

    st.write("---")

    # Visualizzazione dei dettagli della moto selezionata
    if marca_scelta and anno_scelto in moto_database[marca_scelta]:
        moto_selezionata = moto_database[marca_scelta][anno_scelto]

        # Titolo della moto e Annata
        st.markdown(f"## {marca_scelta} {moto_selezionata['modello']} ({anno_scelto})")

        col1, col2 = st.columns([1, 1.5]) # Immagine a sinistra, specifiche a destra

        # Immagine con effetto 4K ad alta luminescenza
        with col1:
            # Sostituisci "path/to/ktm_2010.jpg" con l'URL effettivo dell'immagine
            # st.image(moto_selezionata['immagine'], use_column_width=True, clamp=True, output_format='PNG', className='catalogue-image')
            
            # Per mostrare l'effetto luminescenza, usiamo HTML direttamente
            # Assicurati di avere l'URL corretto dell'immagine
            immagine_url = "https://via.placeholder.com/640x480.png?text=Moto+4:3+Sample" # Placeholder
            if moto_selezionata['immagine'] != "path/to/image.jpg": # Controlla se è un placeholder nel DB
                 immagine_url = moto_selezionata['immagine'] # Usa l'url del database

            st.markdown(f'<div class="catalogue-image"><img src="{immagine_url}" alt="{marca_scelta} {moto_selezionata["modello"]}" width="100%"></div>', unsafe_allow_html=True)


        # Specifiche dettagliate
        with col2:
            st.markdown("### 📊 Specifiche Tecniche Dettagliate")

            # ESEMPIO: Aggiungi molte più specifiche dettagliate nel database!
             specifiche_placeholder = {
                "🚀 MOTORE": ["Tipo", "Cilindrata", "Alesaggio/Corsa", "Compressione", "Potenza Max", "Coppia Max", "Alimentazione", "Avviamento", "Frizione", "Cambio", "Trasmissione Finale"],
                "🏗️ CICLISTICA": ["Telaio", "Sospensione Anteriore", "Escursione Anteriore", "Sospensione Posteriore", "Escursione Posteriore", "Pneumatico Anteriore", "Pneumatico Posteriore", "Altezza Sella", "Interasse", "Peso (a secco)"],
                "🛑 FRENI": ["Freno Anteriore", "Diametro Anteriore", "Pinza Anteriore", "Freno Posteriore", "Diametro Posteriore", "Pinza Posteriore", "ABS (se presente)"],
                "🔋 ELETTRONICA": ["Centralina", "Mappe Motore", "Traction Control", "Launch Control", "Quickshifter (se presente)"]
            }

            for categoria, campi in specifiche_placeholder.items():
                st.markdown(f"<p class='spec-category'>{categoria}:</p>", unsafe_allow_html=True)
                for campo in campi:
                    # Cerca se il campo esiste nel database per la moto selezionata
                    # Se non esiste, mostra un placeholder
                    # (Dovrai popolare il database con questi campi!)
                    valore = moto_selezionata.get(campo.lower(), "Dati non disponibili") # Usa get() con default
                    st.markdown(f"<p class='spec-value'>• **{campo}:** {valore}</p>", unsafe_allow_html=True)
            
            # Esempio di come usare i dati esistenti nel DB:
            # st.markdown(f"<p class='spec-category'>MOTORE (Base):</p><p class='spec-value'>{moto_selezionata['motore']}</p>", unsafe_allow_html=True)
            # st.markdown(f"<p class='spec-category'>CICLISTICA (Base):</p><p class='spec-value'>{moto_selezionata['ciclistica']}</p>", unsafe_allow_html=True)
            # st.markdown(f"<p class='spec-category'>FRENI (Base):</p><p class='spec-value'>{moto_selezionata['freni']}</p>", unsafe_allow_html=True)


    else:
         st.warning("Seleziona una marca e un'annata valida per visualizzare i dettagli.")

# --- FOOTER ---
st.write("---")
st.caption("Savein's Moto - App Catalogo Moto 125cc (Simulazione - Versione Streamlit)")
