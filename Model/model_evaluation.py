import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_model(model, X, y):
    """
    Evaluate the performance of the sales forecasting model using metrics like MAE and RMSE.
    
    Args:
        model: The trained sales forecasting model.
        X (pd.DataFrame): The input features for evaluation.
        y (pd.Series): The target variable for evaluation.
        
    Returns:
        dict: A dictionary of evaluation metrics.
    """
    predictions = model.predict(X)
    
    evaluation_metrics = {
        'MAE': mean_absolute_error(y, predictions),
        'RMSE': np.sqrt(mean_squared_error(y, predictions)),
        'r2_score': r2_score(y, predictions)
    }
    
    return evaluation_metrics
