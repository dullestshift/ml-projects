import streamlit as st
import pickle
import pandas as pd
import io
def main():
    st.title(" THE DATA SET")
    print()



    df = pd.read_csv("pages\Mental Health Dataset.csv")
    st.write(df)

    st.title(":white[ FEATURES]")
    fet = df.iloc[:,:-1]
    st.write(fet)
    st.title(":white[ TARGET]")
    tar = df.iloc[:,-1]
    st.write(tar)




    st.title(" info of dataset")

    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    st.title("final dataset after label encoding and feature selection")
    with open('pages/accuracy_df_new', 'rb') as file:
        df2 = pickle.load(file)
    st.dataframe(df2)
main()