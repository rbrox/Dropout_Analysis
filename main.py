# Streamlit UI
import streamlit as st
import pandas as pd
import joblib
from functions import get_all_models, load_model, get_state_data, get_states, clean_user_data, predict



# Streamlit app
st.title('Problem Statement')
st.write(""" ### 📚 Government's Education Goal: ✨ High dropout rates at schools due to poverty and social factors. Analyzing 👇

1. 🏫 School-wise
2. 🌍 Area-wise
3. 👧🧑 Gender-wise
4. 🕊️ Caste-wise
5. 📆 Age/Grade-wise

📊 Benefits: Informed policies, equitable access, social equity, economic growth, prosperity 🚀""")




# Specify model to load
models = get_all_models()

byte_file = st.file_uploader("upload a csv file to get analysis: ")
#data = pd.read_csv('data.csv', delimiter=';')
if byte_file is not None : 
    st.write("file uploaded successfully")
    #read df
    df = pd.read_csv(byte_file, delimiter=",")
    st.write(type(byte_file))
    
    #df = clean_user_data(df)
    st.write(df)
    st.write(df.dtypes)
    
    selected_model = st.selectbox("Select a Model", get_all_models())   
    st.write("Analyzing your data:") 
    model = load_model(selected_model)
    op = model.predict(df)
    st.write(op)






