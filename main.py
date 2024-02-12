import streamlit as st
from scrap import cek_data, get_data, clean_data

st.title('Homework 1 - Scraping Data from Tokopedia')
# st.image('https://images.tokopedia.net/img/cache/200-square/VqbcmM/2024/2/10/86ea9d63-72a9-426e-8f45-4df982894406.jpg')
title = st.text_input(
        "Cari Produk",
        ""
    )

if title:
    with st.spinner("Fetching Data, Please Wait <3"):
        dtFrame = clean_data(title)
    st.subheader('Data Product')
    st.write(dtFrame)