import streamlit as st
import joblib
import pandas as pd


def get_states():
    path = 'data\dropout_data.csv'
    df = pd.read_csv(path)
    lis = df.iloc[: , 0].values.tolist()
    return lis

def get_state_data():
    path = 'Frontend\data\dropout_data.csv'
    df = pd.read_csv(path)
    
    return df


def get_all_models():
    return ['knn_model', 'nb_model', 'svm_model']

def load_model(model_name):
    models = get_all_models()
    if model_name == models[0]:
        
        pass
    elif model_name == models[1]:
        
        pass
    # Add more models as needed


def main():
    ...
    
    
if __name__ == "__main__":
    print('test')
    main()