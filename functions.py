import streamlit as st
import joblib
import pandas as pd
import streamlit as st
from sklearn.metrics import classification_report


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
    
def get_model_data(model_name):
    models = get_all_models()
    if model_name == models[0]:
        st.write('#### K Nearest Neighbours')
        pass
    elif model_name == models[1]:
        st.write('#### Naive Bayes')
        pass
    else:
        st.write('#### Support Vector Machines')
    
    
    
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
        path = models[0] + '.pkl'
        with open(path, 'rb') as f:
            model = joblib.load(f)
        pass
    elif model_name == models[1]:
        if model_name == models[1]:
            path = models[1] + '.pkl'
        with open(path, 'rb') as f:
            model = joblib.load(f)
        pass
    else:
        if model_name == models[2]:
            path = models[2] + '.pkl'
        with open(path, 'rb') as f:
            model = joblib.load(f)
            
    return model
    # Add more models as needed

def clean_user_data(df):
    
    df.drop("Target", axis = 1,inplace = True)
    return df

def predict(model_name, data):
    paths = ['knn_model.pkl', 'nb_model.pkl', 'svm_model.pkl']
    
    if model_name == 'knn_model':
        model = joblib.load(paths[0])
    elif model_name == 'nb_model':
        model = joblib.load(paths[1])
    else :
        model = joblib.load(paths[2])
        
    return model.predict(data)

def model_analysis(output_list):
    return (output_list.unique().count())
    ...
    
def list_analysis(data):
    
    true_count = data.count(True)
    false_count = data.count(False)
    total_count = len(data)
    
    drop_rate = f"{round(float(true_count/total_count) * 100, 4)} %"
    info = {
        'Dropout Count' : true_count,
        'Graduate Count' : false_count,
        'Total Count': total_count,
        'Dropout Percentage': drop_rate
    }
    
    return info

def main():
    get_state_data('Andhra Pradesh')
    
    
if __name__ == "__main__":
    print('test')
    main()