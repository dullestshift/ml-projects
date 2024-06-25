import streamlit as st
from PIL import Image
def main():
    st.title(":blue[ MENTAL HEALTH TREATMENT PREDICTION ]")
    image = Image.open('pages/shadow.gif')
    st.image(image, width=600)
    st.title("A short intro..")
    st.write("Mental health includes our emotional, psychological, and social well-being."
             " It affects how we think, feel, and act, and helps determine how we handle stress,"
             " relate to others, and make choices.Mental health is important at every stage of life,"
             " from childhood and adolescence through adulthood. Over the course of your life,"
             " if you experience mental health problems, your thinking, mood, and behavior could be affected.")
    st.title("Key points on mental health")
    st.write("> Affordable, effective and feasible strategies exist to promote, protect and restore mental health.")
    st.write("> The need for action on mental health is indisputable and urgent.")
    st.write("> Mental health has intrinsic and instrumental value and is integral to our well-being.")
    st.write("> Mental health is determined by a complex interplay of individual, "
             "social and structural stresses and vulnerabilities.")


main()