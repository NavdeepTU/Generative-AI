import streamlit as st
import pandas as pd

st.title("Streamlit Text input")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}")

age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is {age}")

options = ["C", "C++", "Java", "Python"]
choice = st.selectbox("Choose your favourite language:", options)
st.write(f"You selected {choice}.")

data = {
    "Name" : ["Jaskirat", "Mukul", "Navdeep", "Paarth"],
    "Age" : [23, 25, 28, 30],
    "City" : ["Patiala", "Delhi", "Noida", "New York"]
}
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

upladed_file = st.file_uploader("Choose a csv file", type="csv")
if upladed_file is not None:
    df = pd.read_csv(upladed_file)
    st.write(df)