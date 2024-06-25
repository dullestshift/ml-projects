import streamlit as st

import pandas as pd

placeholder = st.empty()
df = pd.read_csv("../manaf/pages/Mental Health Dataset.csv")
# st.dataframe(df)

if not st.checkbox("Hide dataframe"):
    placeholder.dataframe(df)
# st.button('[Click Here](https://stackoverflow.com)')
#
# st.link_button("Go to gallery", "http://localhost:8501/")
st.link_button("Go to test", "pred.py")



