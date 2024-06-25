import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the page configuration
st.set_page_config(
    page_title="Mental Health Insights",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="auto"
)

# Title of the Streamlit app
st.title(":green[Occupation Distribution Pie Chart]")

# Load the dataset
df = pd.read_csv("pages/Mental Health Dataset.csv")

# Plot the occupation distribution pie chart
fig = plt.figure(figsize=(5, 5), facecolor='lightgray')
df['Occupation'].value_counts().plot.pie(autopct='%1.1f%%', colors=['skyblue', 'lightcoral', 'blue', 'yellow', 'red', 'green'])
plt.title('Occupation Distribution')
plt.ylabel('')  # Hide the y-label for better visual

# Display the pie chart in Streamlit
st.pyplot(fig)

# Title for count plots
st.title(":green[Count Plot of All Columns in Dataset]")

# Plot count plots for all columns
for column in df.columns:
    fig2 = plt.figure(figsize=(7, 3))
    df[column].value_counts().plot(kind='bar', color='blue')
    plt.xlabel(column)
    plt.title(f"Count of Values in {column}")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig2)
