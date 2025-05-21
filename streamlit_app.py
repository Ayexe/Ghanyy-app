import streamlit as st

st.title("RADITMAXWIN999")
st.write("LIAT INI GANTENG BGT DIA")
st.image("IMG_20250520_145036.jpg", width=2000)

st.title("MAXWIN DI JAMIN GACOR!")
st.header("RADIT INGIN TES KEBERUNTUNGAN ANDA")
angka = st.number_input ("MASUKAN ANGKA BERUNTUNG ANDA!:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} RADIT MEMIKIR... ANDA KURANG BERUNTUNG")
else:
    st.write(f"{angka} RADIT MEMIKIR... ANDA MAXWINNNN GACORRR")
    
    
     
