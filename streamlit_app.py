import streamlit as st

st.title("INDOJAW!")
st.write("!INDOMARET JAWA PRIDE!")
st.image("IMG_20250520_145036.jpg", width=2000)

st.title("Aplikasi Radit pinter ngitung")
st.header("Radit bisa ngitung, coba aja")
angka = st.number_input ("tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan genap")
else:
    st.write(f"{angka} adalah Bilangan ganjil")
    
    
     
