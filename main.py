# Streamlit UI
import streamlit as st
import pandas as pd
import joblib
from functions import get_all_models, load_model, get_state_data, get_states, clean_user_data, predict, get_model_data, list_analysis



# Streamlit app
st.title('🏆Acheivers')
st.write(""" ### Government's Education Goal: 
        High dropout rates at schools due to poverty and social factors. Analyzing 

#### Features(For Prediction)
1. 🏫 School-wise
2. 🌍 Area-wise
3. 👧 Gender-wise
4. 🕊️ Caste-wise
5. 📆 Age/Grade-wise

#### Benefits:
1. Dropout Statistics and Management
2. Tailored Policy making

""")

st.write("---")
st.title('⚙️Model Info')
# Model Info
selected_model = st.selectbox("See Model data", get_all_models())   
get_model_data(selected_model)

st.write("---")
st.title("🚀Use the Model")
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
    
    op = model.predict(df).tolist()
    st.write(list_analysis(op))
    st.write(op)
   

st.write("---")
st.title('☁︎ Cloud Deployment')
st.image('./QR.jpg', caption='Our App', use_column_width=True)

st.write("---")
st.title(' Team Members')
st.write("""
         
        1. Sreethi
        2. Mallika
        3. Rishav
        4. Shahshank
        5. Rishika
        6. Vidhisha
         """)



