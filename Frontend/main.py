# knn_app.py
import streamlit as st
import joblib

# Load the pickled KNN model
knn_model = joblib.load('./knn_model.pkl')

# Streamlit app
st.title('Dropout Analysis')
st.write('This web application is powered by the following models:\n Feel free to choose whichever you like\n ')

# Check if the model has a feature_names_ attribute (for scikit-learn models)
if hasattr(knn_model, 'feature_names_'):
    # Get the feature names
    feature_names = knn_model.feature_names_

    # Display the feature names in Streamlit
    st.title('Model Features')
    st.write('List of Features:')
    st.write(feature_names)
else:
    st.warning('This model does not have feature names.')
