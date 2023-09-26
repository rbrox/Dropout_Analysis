import streamlit as st
import joblib
import pandas as pd


def get_states():
    path = 'data\dropout_data.csv'
    df = pd.read_csv(path)
    lis = df.iloc[: , 0].values.tolist()
    return lis    

def get_all_state_data():
    path = 'data\dropout_data.csv'
    df = pd.read_csv(path)
    
    return df

def get_state_data(state_code):
    df = get_all_state_data()
    print(df.to_dict())
    return df.to_dict()
    
    
    """
    state_data = df[df['State/UTs'] == state_code]
    state_data = state_data.drop(columns=['State/UTs'])
    print(state_data)
    return state_data
    """

def get_all_models():
    return ['knn_model', 'nb_model', 'svm_model']

def load_model(model_name):
    models = get_all_models()
    if model_name == models[0]:
        
        pass
    elif model_name == models[1]:
        
        pass
    # Add more models as needed

def clean_user_data(path):
    df = pd.read_csv(path)
    #if df.index != 
    if 'Target' in df.index: 
        df.drop("Target", inplace = True)
    df.head()

def predict(model_name, data):
    paths = ['knn_model.pkl', 'nb_model.pkl', 'svm_model.pkl']
    
    if model_name == 'knn_model':
        model = joblib.load(paths[0])
    elif model_name == 'nb_model':
        model = joblib.load(paths[1])
    else :
        model = joblib.load(paths[2])
        
    return model.predict(data)

def main():
    get_state_data('Andhra Pradesh')
    
    
if __name__ == "__main__":
    print('test')
    main()