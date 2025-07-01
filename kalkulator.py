import streamlit as st 
from streamlit_option_menu import option_menu

def konversi_suhu():
    st.title('Kalkulator Hitung Suhu')
    st.image("https://1.bp.blogspot.com/-cBZoS0UFoPA/XO5HS_Aiy5I/AAAAAAAAQ80/WgJj7PgXKUstm0K2tIDr5VKLPJLeBnY6QCLcBGAs/s1600/suhu%2Bdan%2Bperubahannya%2B-%2Bsmp.jpg", width=150)
    st.header("Kalkulator konversi online untuk melakukan konversi satuan suhu, mulai dari Celsius, Fahrenheit, Kelvin, dan Reamur.")


    celcius = st.number_input("Masukan Nilai celcius", 0)   
    hitung_c = st.button("Hitung Celcius")
    reamur = st.number_input("Masukan Nilai reamur", 0)   
    hitung_r = st.button("Hitung reamur")
    fahrenheit = st.number_input("Masukan Nilai fahrenheit", 0)   
    hitung_f = st.button("Hitung fahrenheit")
    kelvin = st.number_input("Masukan Nilai kelvin", 0)   
    hitung_k = st.button("Hitung kelvin")
        
    if hitung_c :
            reamur = (4/5) * celcius
            fahrenheit = ((9/5) * celcius) + 32
            kelvin = celcius + 273
            st.success(f"Suhu dalam reamur adalah = {reamur}")
            st.success(f"Suhu dalam fahrenheit adalah = {fahrenheit}")
            st.success(f"Suhu dalam kelvin adalah = {kelvin}")
            
    if hitung_r :
            celcius = (5/4) * reamur
            fahrenheit = ((9/4) * reamur) + 32
            kelvin = ((5/4) * reamur) + 273
            st.success(f"Suhu dalam celcius adalah = {celcius}")
            st.success(f"Suhu dalam fahrenheit adalah = {fahrenheit}")
            st.success(f"Suhu dalam kelvin adalah = {kelvin}")
            
    if hitung_f :
            celcius = celcius = 5/9 * ((fahrenheit - 32))
            reamur = 4/9 * ((fahrenheit - 32))
            kelvin = 5/9 * (fahrenheit - 32) + 273
            st.success(f"Suhu dalam celcius adalah = {celcius}")
            st.success(f"Suhu dalam reamur adalah = {reamur}")
            st.success(f"Suhu dalam kelvin adalah = {kelvin}")
            
    if hitung_k :
            celcius = kelvin - 273
            fahrenheit = 9/5 * (kelvin - 273) + 32
            reamur = 4/5 * (kelvin - 273)
            st.success(f"Suhu dalam celcius adalah = {celcius}")
            st.success(f"Suhu dalam fahrenheit adalah = {fahrenheit}")
            st.success(f"Suhu dalam reamur adalah = {reamur}")