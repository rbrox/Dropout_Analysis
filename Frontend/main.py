# Streamlit UI
import streamlit as st

import joblib
from functions import get_all_models, load_model, get_state_data, get_states



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

uploaded_file = st.file_uploader("Upload a CSV file to get analysis", type=["csv"])

if uploaded_file is not None:
    st.write("File upload Sucessfull!")
    
    data = uploaded_file.read()
    st.write("Analyzing you data:") 

selected_model = st.selectbox("Select a Model", get_all_models())




