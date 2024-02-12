import streamlit as st
import pandas as pd
from selen import get_data
import json

st.title('Homework 1 - Scraping Data from Tokopedia')
title = st.text_input(
        "Cari Produk",
        ""
    )
pages = st.slider('Jumlah Halaman yang ingin dicari', 0, 50, 1)

if st.button('Cari'):
    with st.spinner("Fetching Data, Please Wait <3"):
        dtFrame = get_data(title,pages)
    st.subheader('Data Product')
    st.write("Jumlah data: ",len(dtFrame))
    st.write(dtFrame)
    json_data = json.dumps(dtFrame, indent=2)
    df = pd.DataFrame(json.loads(json_data)).T
    st.write(df)