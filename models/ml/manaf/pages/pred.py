import streamlit as st
import pickle
from PIL import Image
import pandas as pd
import google.generativeai as genai

apikey = st.secrets["api"]["key"]
genai.configure(api_key=apikey)
model_bot = genai.GenerativeModel('gemini-pro')

def main():
    # Set the page configuration
    st.set_page_config(
        page_title="Mental Health Check",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="auto"
    )

    # Title of the Streamlit app
    st.title(":white[DO YOU NEED MEDICAL HELP]")
    image = Image.open('pages/mental1.jpg')
    st.image(image, width=600)

    # Placeholder for the dataframe
    placeholder = st.empty()
    df = pd.read_csv("pages/Mental Health Dataset.csv")
    df = df.head(10)

    if not st.checkbox("Hide dataframe"):
        placeholder.dataframe(df)

    # Selectboxes for user input
    Mood_swings = st.selectbox('Rate of your mood swings?', ('High', 'Low', 'Medium'))
    st.write("You selected:", Mood_swings)
    mood = 2 if Mood_swings == 'High' else 1 if Mood_swings == 'Low' else 0

    Coping_struggles = st.selectbox('Coping struggles?', ('No', 'Yes'))
    st.write("You selected:", Coping_struggles)
    cs = 1 if Coping_struggles == 'No' else 0

    Work_interest = st.selectbox('Is your work interesting?', ('Maybe', 'No', 'Yes'))
    st.write("You selected:", Work_interest)
    wi = 1 if Work_interest == 'Maybe' else 0 if Work_interest == 'No' else 2

    Social_weakness = st.selectbox('Are you weak socially?', ('Maybe', 'No', 'Yes'))
    st.write("You selected:", Social_weakness)
    sw = 2 if Social_weakness == 'Maybe' else 1 if Social_weakness == 'No' else 0

    Mental_health_interview = st.selectbox('Participated in mental health interviews?', ('Maybe', 'No', 'Yes'))
    st.write("You selected:", Mental_health_interview)
    mhi = 0 if Mental_health_interview == 'Maybe' else 1 if Mental_health_interview == 'No' else 2

    Country = st.selectbox('Select your country of origin', ('Australia', 'Belgium', 'Canada', 'India', 'Ireland',
                                                             'Netherlands', 'New Zealand', 'Poland', 'South Africa',
                                                             'Sweden', 'United Kingdom', 'United States'))
    st.write("You selected:", Country)

    original_values = ['Australia', 'Belgium', 'Canada', 'India', 'Ireland', 'Netherlands',
                       'New Zealand', 'Poland', 'South Africa', 'Sweden', 'United Kingdom', 'United States']
    label_values = [11, 7, 0, 2, 10, 8, 9, 6, 5, 3, 1, 4]
    cou = label_values[original_values.index(Country)]

    Self_employed = st.selectbox('Are you self-employed?', ('No', 'Yes'))
    st.write("You selected:", Self_employed)
    self = 0 if Self_employed == 'No' else 1

    Family_history = st.selectbox('Does your family have any mental health history?', ('No', 'Yes'))
    st.write("You selected:", Family_history)
    fam = 1 if Family_history == 'No' else 0

    Changes_habits = st.selectbox('Do you feel like there are changes in your habits?', ('Maybe', 'No', 'Yes'))
    st.write("You selected:", Changes_habits)
    change = 0 if Changes_habits == 'Yes' else 1 if Changes_habits == 'Maybe' else 2

    Care_options = st.selectbox('Are you getting enough care?', ('No', 'Not sure', 'Yes'))
    st.write("You selected:", Care_options)
    care = 0 if Care_options == 'Yes' else 1 if Care_options == 'Not sure' else 2

    features = [cou, self, fam, change, mood, cs, wi, sw, mhi, care]

    st.title(":white[Accuracy of different classification algorithms]")

    with open('pages/accuracy_df', 'rb') as file:
        df3 = pickle.load(file)
    st.dataframe(df3)

    algo = st.selectbox("Which algorithm do you wish to use?", ('AdaBoost Classifier', 'Decision Tree Classifier',
                                                                'Gaussian NB', 'Gradient Boosting Classifier',
                                                                'KNeighbors Classifier', 'Random Forest Classifier',
                                                                'SVC', 'XGB Classifier'))
    st.write("You selected", algo)
    models = ['AdaBoostClassifiermental.sav', 'DecisionTreeClassifiermental.sav', 'GaussianNBmental.sav',
              'GradientBoostingClassifiermental.sav', 'KNeighborsClassifiermental.sav',
              'RandomForestClassifiermental.sav',
              'SVCmental.sav', 'XGBClassifiermental.sav']
    algom = ['AdaBoost Classifier', 'Decision Tree Classifier', 'Gaussian NB', 'Gradient Boosting Classifier',
             'KNeighbors Classifier', 'Random Forest Classifier', 'SVC', 'XGB Classifier']

    model = None
    for i in range(len(models)):
        if algo == algom[i]:
            algm = 'pages/' + models[i]
            model = pickle.load(open(algm, 'rb'))

    if st.button('CHECK'):
        prediction = model.predict([features])
        if prediction == 1:
            image = Image.open('pages/giphy.gif')
            st.image(image, width=400)
            st.write("YOUR MENTAL HEALTH IS FINE. YOU DON'T NEED TREATMENT.")
            st.write("but here are some tips for a healthier lifestyle")
            response = model_bot.generate_content("give ten tips for healthy lifestyle")
            st.write(response.text)
        else:
            image = Image.open('pages/lettalkaboutit.gif')
            st.image(image, width=400)
            st.write("YOU NEED TO VISIT A DOCTOR.")
            st.write(f"HERE ARE SOME OF THE BEST CLINICS IN {Country} you can visit")
            response = model_bot.generate_content(f"i am from{Country} give mental health clinic address")
            st.write(response.text)



main()
