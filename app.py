import streamlit as st
import random

# Configurazione Pagina
st.set_page_config(page_title="Catalogo 125 Enduro/Motard", page_icon="🏍️")

# Database delle moto (Esempio strutturato)
moto_data = [
    {
        "marca": "KTM",
        "modello": "125 EXC",
        "anno": "2023",
        "tipo": "Enduro",
        "motore": "Monocilindrico 2 tempi, scarico a valvola",
        "cambio": "6 marce",
        "ciclistica": "Telaio a traliccio in acciaio al cromo-molibdeno, Forcella WP XPLOR",
        "freni": "Disco anteriore 260mm, posteriore 220mm Brembo"
    },
    {
        "marca": "GASGAS",
        "modello": "EC 125",
        "anno": "2024",
        "tipo": "Enduro",
        "motore": "Monocilindrico 2 tempi, iniezione TBI",
        "cambio": "6 marce",
        "ciclistica": "Telaio a traliccio, Sospensioni WP XACT",
        "freni": "Impianto frenante Braktec"
    },
    {
        "marca": "TM Racing",
        "modello": "SMR 125",
        "anno": "2024",
        "tipo": "Motard",
        "motore": "2 tempi con valvola elettronica, artigianale",
        "cambio": "6 marce",
        "ciclistica": "Telaio perimetrale in alluminio, Forcella Kayaba 48mm",
        "freni": "Pinza Brembo radiale, Disco 320mm"
    },
    # Aggiungi qui tutte le altre marche (Fantic, Husqvarna, Beta, ecc.)
]

# Interfaccia Utente
st.title("🏍️ 125cc Selector")
st.subheader("Trova la tua prossima moto Enduro o Motard")

st.write("---")

# Il Tasto Centrale
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 SCOPRI UNA MOTO CASUALE", use_container_width=True):
        scelta = random.choice(moto_data)
        
        # Visualizzazione Risultato
        st.balloons()
        st.success(f"Ecco la tua moto: **{scelta['marca']} {scelta['modello']} ({scelta['anno']})**")
        
        # Tabella Specifiche
        st.markdown(f"### 📊 Specifiche Tecniche")
        st.info(f"**Categoria:** {scelta['tipo']}")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"**🔥 Motore:** \n{scelta['motore']}")
            st.markdown(f"**⚙️ Cambio:** \n{scelta['cambio']}")
        with col_b:
            st.markdown(f"**🏗️ Ciclistica:** \n{scelta['ciclistica']}")
            st.markdown(f"**🛑 Freni:** \n{scelta['freni']}")
    else:
        st.info("Clicca il tasto sopra per generare una categoria e una moto!")

st.write("---")
st.caption("Database aggiornato alle ultime versioni KTM, GASGAS, TM e altre.")