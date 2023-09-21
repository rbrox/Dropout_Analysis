import pandas as pd
from model_evaluation import evaluate_model 
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def select_model(model_type='random_forest'):
    """
    Select the appropriate regression model.
    
    Args:
        model_type (str): Type of regression model, either 'linear' or 'random_forest'.
    
    Returns:
        model: The selected regression model.
    """
    if model_type == 'linear':
        return LinearRegression()
    elif model_type == 'random_forest':
        return RandomForestRegressor()
    else:
        raise ValueError("Invalid model_type. Supported options are 'linear' and 'random_forest'.")

def hyperparameter_tuning(model, param_grid):
    """
    Perform hyperparameter tuning of the selected model using Grid Search.
    
    Args:
        model: The selected regression model.
        param_grid (dict): Dictionary containing hyperparameter values for Grid Search.
        
    Returns:
        model: The tuned regression model.
    """
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3)
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_

def train_model(data, model_type='random_forest', param_grid=None, target = 'target'):
    """
    Train the regression model on the provided data.
    
    Args:
        data (pd.DataFrame): The input DataFrame containing the training data.
        model_type (str): Type of regression model, either 'linear' or 'random_forest'.
        param_grid (dict, optional): Dictionary containing hyperparameter values for Grid Search.
        
    Returns:
        model: The trained regression model.
    """
    print('Training model...')
    y = data[target].copy()
    X = data.drop(target, axis=1)
    print('Sucessfully droped target col')
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = select_model(model_type=model_type)
    
    if param_grid:
        model = hyperparameter_tuning(model, param_grid)
    
    model.fit(X_train, y_train)
    
    df = evaluate_model(model, X_val, y_val)
    
    print(df)
    
    return model, X_val, y_val
