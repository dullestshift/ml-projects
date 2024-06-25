import streamlit as st
import pickle
from PIL import Image
import pandas as pd


def main():
    st.title(":white[ DO YOU NEED MEDICAL HELP]")
    image = Image.open('../../manaf/pages/mental1.jpg')
    st.image(image, width=600)


    placeholder = st.empty()
    df = pd.read_csv("Mental Health Dataset.csv")

    if not st.checkbox("Hide dataframe"):
        placeholder.dataframe(df)


    Country = st.selectbox('select your country of origin',('Australia', 'Belgium' ,'Canada', 'India' ,'Ireland',
                                                            'Netherlands',
    'New Zealand' ,'Poland', 'South Africa' ,'Sweden' ,'United Kingdom',
    'United States'))
    st.write("you selected : ",Country )

    Self_employed = st.selectbox('are you self employed',('No' ,'Yes'))
    st.write("you selected : ",Self_employed )
    if Self_employed=='No':
        self =0
    else:
        self = 1
    Family_history = st.selectbox('does your family members has any mental health history',('No', 'Yes'))
    st.write("you selected : ",Family_history )

    if Family_history=='No':
        fam =1
    else:
        fam = 0

    Changes_habits = st.selectbox('do you feel like there are changes in your habits',('Maybe' ,'No', 'Yes'))
    st.write("you selected : ",Changes_habits)

    if Changes_habits=='Yes':
        change =0
    elif Changes_habits=='Maybe':
        change = 1
    else:
        change = 2

    Care_options = st.selectbox('are you getting enough care',('No', 'Not sure', 'Yes'))
    st.write("you selected : ",Care_options )

    if Care_options == 'Yes':
        care = 0
    elif Care_options == 'Not sure':
        care = 1
    else:
        care = 2

    c =['Australia', 'Belgium', 'Canada', 'India', 'Ireland', 'Netherlands',
     'New Zealand', 'Poland', 'South Africa', 'Sweden', 'United Kingdom',
     'United States']

    cc =[11 , 7,  0,  2, 10,  8,  9,  6,  5,  3,  1,  4]
    for i in range(12):
        if Country == c[i]:
            cou = cc[i]

    features=[	cou,self,fam,change,care]
    model=pickle.load(open('../mental (1).sav', 'rb'))
    # scaler=pickle.load(open('lung-scaler.sav','rb'))
    pred = st.button('CHECK')
    if pred:
        prediction=model.predict([features])


        if prediction==1:

            image = Image.open('fine.jfif')
            st.image(image, width=400)

            st.write(" YOU DO NOT IMMEDIATE TREATMENT")

        else:
            image = Image.open('helpmental.jfif')
            st.image(image, width=400,)
            st.write("YOU NEED TO VIST A DOCTOR")



main()

# if st.button("Home"):
#     st.switch_page("C:\Users\manaf\PycharmProjects\pythonProject\models\mental\home.py")