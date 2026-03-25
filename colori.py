import streamlit as st

# Configurazione pagina
st.set_page_config(page_title="Codice Colori Resistenze", page_icon="🎨", layout="centered")

st.title("🎨 Calcolatore Codice Colori (4 Bande)")
st.write("Seleziona i colori degli anelli per vedere il valore e la resistenza visiva.")

# 1. Mappe dei dati (Valori, Moltiplicatori, Tolleranze)
colori_cifre = {
    "Nero": 0, "Marrone": 1, "Rosso": 2, "Arancio": 3, "Giallo": 4,
    "Verde": 5, "Blu": 6, "Viola": 7, "Grigio": 8, "Bianco": 9
}

colori_molt = {
    "Nero (x1)": 1, "Marrone (x10)": 10, "Rosso (x100)": 100,
    "Arancio (x1k)": 1000, "Giallo (x10k)": 10000, "Verde (x100k)": 100000,
    "Blu (x1M)": 1000000, "Oro (x0.1)": 0.1, "Argento (x0.01)": 0.01
}

colori_tol = {"Oro (±5%)": "5%", "Argento (±10%)": "10%", "Marrone (±1%)": "1%"}

# Mappa dei colori CSS aggiornata con i nomi esatti dei menu
mappa_colori_css = {
    # Cifre (Banda 1 e 2)
    "Nero": "black", "Marrone": "#8B4513", "Rosso": "red", "Arancio": "orange",
    "Giallo": "yellow", "Verde": "green", "Blu": "blue", "Viola": "purple",
    "Grigio": "gray", "Bianco": "white",

    # Moltiplicatori (Banda 3) - Devono corrispondere a colori_molt.keys()
    "Nero (x1)": "black", "Marrone (x10)": "#8B4513", "Rosso (x100)": "red",
    "Arancio (x1k)": "orange", "Giallo (x10k)": "yellow", "Verde (x100k)": "green",
    "Blu (x1M)": "blue", "Oro (x0.1)": "#FFD700", "Argento (x0.01)": "#C0C0C0",

    # Tolleranze (Banda 4) - Devono corrispondere a colori_tol.keys()
    "Oro (±5%)": "#FFD700", "Argento (±10%)": "#C0C0C0", "Marrone (±1%)": "#8B4513"
}

# 3. Interfaccia di selezione (Colonne)
st.subheader("Seleziona gli Anelli")
c1, c2, c3, c4 = st.columns(4)

with c1:
    b1_nome = st.selectbox("1ª Banda (Cifra)", list(colori_cifre.keys()), index=1)  # Marrone
with c2:
    b2_nome = st.selectbox("2ª Banda (Cifra)", list(colori_cifre.keys()), index=0)  # Nero
with c3:
    mult_nome = st.selectbox("Moltiplicatore", list(colori_molt.keys()), index=2)  # Rosso (x100)
with c4:
    tol_nome = st.selectbox("Tolleranza", list(colori_tol.keys()), index=0)  # Oro

# 4. Calcolo del Valore
cifra1 = colori_cifre[b1_nome]
cifra2 = colori_cifre[b2_nome]
moltiplicatore = colori_molt[mult_nome]
tolleranza = colori_tol[tol_nome]

valore_ohm = (cifra1 * 10 + cifra2) * moltiplicatore

# Formattazione leggibile (Ω, kΩ, MΩ)
if valore_ohm >= 1000000:
    testo_valore = f"{valore_ohm / 1000000:.1f} MΩ"
elif valore_ohm >= 1000:
    testo_valore = f"{valore_ohm / 1000:.1f} kΩ"
else:
    testo_valore = f"{valore_ohm:.1f} Ω"

# 5. Visualizzazione Risultato
st.divider()
st.success(f"## Valore Calcolato: **{testo_valore}**")
st.write(f"Tolleranza: {tolleranza}")

# 6. --- PARTE VISIVA: Disegno della Resistenza ---
st.subheader("Visualizzazione Resistenza")

# Recuperiamo i colori CSS corretti
colore_css_1 = mappa_colori_css[b1_nome]
colore_css_2 = mappa_colori_css[b2_nome]
colore_css_3 = mappa_colori_css[mult_nome]  # Usa il nome completo del selettore
colore_css_4 = mappa_colori_css[tol_nome]  # Usa il nome completo del selettore

# HTML e CSS per disegnare il componente
html_resistenza = f"""
<div style="display: flex; align-items: center; justify-content: center; font-family: sans-serif; margin-top: 20px;">
    <div style="width: 50px; height: 4px; background-color: #aaa;"></div>

    <div style="width: 200px; height: 60px; background-color: #f0e68c; border-radius: 10px; display: flex; justify-content: space-between; padding: 0 15px; box-shadow: 2px 2px 5px rgba(0,0,0,0.2); position: relative;">

        <div style="width: 15px; height: 100%; background-color: {colore_css_1};"></div>
        <div style="width: 15px; height: 100%; background-color: {colore_css_2};"></div>
        <div style="width: 15px; height: 100%; background-color: {colore_css_3};"></div>

        <div style="width: 40px; height: 100%;"></div>

        <div style="width: 15px; height: 100%; background-color: {colore_css_4};"></div>
    </div>

    <div style="width: 50px; height: 4px; background-color: #aaa;"></div>
</div>
"""

# Rendering dell'HTML in Streamlit
st.markdown(html_resistenza, unsafe_allow_html=True)

st.caption("Nota: I colori sono indicativi e possono variare in base allo schermo.")