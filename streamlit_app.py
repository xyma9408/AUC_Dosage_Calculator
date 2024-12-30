import streamlit as st
from math import log
from math import exp

st.title("AUC-DOSAGE CALCULATOR")
st.write(
    "Given PK paramaters, this calculator returns estimated dosage required for each administration."
)
cmax = st.slider("Cmax (nM)", 0, 20000, 10)
Tmax = st.slide("Tmax (h)", 0, 4, 1)
Thalf = st.slider("T-half (h)", 0, 24, 1)
Vd = st.slider("Vd (L)", 0, 2000, 10)
F = st.slider("Bioavailability (%)", 0, 100, 1)
MW = st.slider("Molecular weight (Da)", 1, 
AUC = 1/2 * cmax * Tmax + cmax * Thalf/log(2) * exp(-log(2) * Tmax/Thalf)
Dose_nmole = AUC * Vd / (F * Thalf * log(2))
Dose_mg = Dose_nmole * MW / 1000000

st.write(f"AUC in nM*h = {AUC}")
st.write(f"Dose in nmoles = {Dose_nmole}")
st.write(f"Dose in mg = {Dose_mg}")
