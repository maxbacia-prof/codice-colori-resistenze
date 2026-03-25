import streamlit as st

st.set_page_config(page_title="Codice Colori", page_icon="🎨")

st.title("🎨 Calcolatore Codice Colori")
st.write("Seleziona i colori degli anelli per calcolare il valore della resistenza.")

# 1. Definizione dei dati con Emoji per richiamare il colore
colori_cifre = {
    "🟤 Marrone (1)": 1, "🔴 Rosso (2)": 2, "🟠 Arancio (3)": 3,
    "🟡 Giallo (4)": 4, "🟢 Verde (5)": 5, "🔵 Blu (6)": 6,
    "🟣 Viola (7)": 7, "⚪ Bianco (9)": 9, "⚫ Nero (0)": 0, "🔘 Grigio (8)": 8
}

colori_molt = {
    "⚫ Nero (x1)": 1, "🟤 Marrone (x10)": 10, "🔴 Rosso (x100)": 100,
    "🟠 Arancio (x1k)": 1000, "🟡 Giallo (x10k)": 10000, "🟢 Verde (x100k)": 100000,
    "🔵 Blu (x1M)": 1000000, "🟡 Oro (x0.1)": 0.1, "⚪ Argento (x0.01)": 0.01
}

colori_tol = {"🟡 Oro (±5%)": "5%", "⚪ Argento (±10%)": "10%", "🟤 Marrone (±1%)": "1%"}

# 2. Interfaccia a colonne
st.subheader("Configurazione Resistenza")
c1, c2, c3, c4 = st.columns(4)

with c1:
    b1 = st.selectbox("1ª Banda", list(colori_cifre.keys()), index=0)
with c2:
    b2 = st.selectbox("2ª Banda", list(colori_cifre.keys()), index=8)
with c3:
    mult = st.selectbox("Moltiplicatore", list(colori_molt.keys()), index=2)
with c4:
    tol = st.selectbox("Tolleranza", list(colori_tol.keys()), index=0)

# 3. Calcolo logico
valore = (colori_cifre[b1] * 10 + colori_cifre[b2]) * colori_molt[mult]

# Formattazione Kilo / Mega
if valore >= 1000000:
    risultato = f"{valore/1000000:.1f} MΩ"
elif valore >= 1000:
    risultato = f"{valore/1000:.1f} kΩ"
else:
    risultato = f"{valore:.1f} Ω"

# 4. Visualizzazione Risultato con fascia colorata
st.divider()
st.info(f"### Valore: {risultato}")
st.write(f"**Tolleranza:** {colori_tol[tol]}")

# Nota didattica
st.caption("Usa le emoji nel menu per orientarti con i colori reali della resistenza.")