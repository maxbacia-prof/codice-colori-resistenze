import streamlit as st

st.title("🎨 Calcolatore Codice Colori")
st.write("Seleziona i colori delle bande per determinare il valore della resistenza.")

# Dizionari per i valori
colori_cifre = {
    "Nero (0)": 0, "Marrone (1)": 1, "Rosso (2)": 2, "Arancio (3)": 3,
    "Giallo (4)": 4, "Verde (5)": 5, "Blu (6)": 6, "Viola (7)": 7,
    "Grigio (8)": 8, "Bianco (9)": 9
}

colori_molt = {
    "Nero (x1)": 1, "Marrone (x10)": 10, "Rosso (x100)": 100,
    "Arancio (x1k)": 1000, "Giallo (x10k)": 10000, "Verde (x100k)": 100000,
    "Blu (x1M)": 1000000, "Oro (x0.1)": 0.1, "Argento (x0.01)": 0.01
}

colori_tol = {"Oro (±5%)": "5%", "Argento (±10%)": "10%", "Marrone (±1%)": "1%"}

# Interfaccia a colonne
c1, c2, c3, c4 = st.columns(4)

with c1:
    b1 = st.selectbox("1ª Banda", list(colori_cifre.keys()), index=1)
with c2:
    b2 = st.selectbox("2ª Banda", list(colori_cifre.keys()), index=0)
with c3:
    mult = st.selectbox("Moltiplicatore", list(colori_molt.keys()), index=2)
with c4:
    tol = st.selectbox("Tolleranza", list(colori_tol.keys()), index=0)

# Calcolo del valore
valore = (colori_cifre[b1] * 10 + colori_cifre[b2]) * colori_molt[mult]

# Formattazione leggibile (Kilo, Mega)
if valore >= 1000000:
    risultato = f"{valore/1000000:.1f} MΩ"
elif valore >= 1000:
    risultato = f"{valore/1000:.1f} kΩ"
else:
    risultato = f"{valore:.1f} Ω"

st.success(f"### Valore: {risultato} (Tolleranza {colori_tol[tol]})")