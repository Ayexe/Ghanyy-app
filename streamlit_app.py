import streamlit as st

st.title("RADIT PINTER")
st.write("LIAT INI GANTENG BGT DIA")
st.image("IMG_20250520_145036.jpg", width=2000)

st.title("Aplikasi Radit pinter ngitung")
st.header("Radit bisa ngitung, coba aja")
angka = st.number_input ("coba tulis angka apa aja, si didits mah jago:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} Kata Radit itu adalah Bilangan genap")
else:
    st.write(f"{angka} Kata Radit itu adalah Bilangan ganjil")
    
    
     
