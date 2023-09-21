import pandas as pd
import numpy as np

def test():
    print('Test')
    

def load_data(path = './data/'):
    # Path is the relative file path to the data folder, defaults to data
    """
    Loads the data required .
    
    Returns:
        pd.DataFrame: The loaded data.
    """
    # Load the necessary datasets
    train_data = pd.read_csv( path + 'train.csv')
    test_data = pd.read_csv(path + 'test.csv')
    stores_data = pd.read_csv(path + 'stores.csv')
    oil_data = pd.read_csv(path + 'oil.csv')
    holidays_data = pd.read_csv(path + 'holidays_events.csv')
    
    # Return the loaded data
    return train_data, test_data, stores_data, oil_data, holidays_data

def assess_data(data):
    """
    Report on data health
    
    Return df of the form 
    
    | Number of values | Mean | Number of Unique Values | Number of Null Values | Dtype | Remarks
      
    
    """
    df = pd.DataFrame(data)
   
    # dict to be converted into dataframe
    assess_dict = {} 
    
    # columns 
    columns = list(df.columns)
    
    # iterate over columns
    for col in columns:
        # Basic stats for numeric columns
        if pd.api.types.is_numeric_dtype(df[col]):
            stats = df[col].describe()
            most_frequent_value = df[col].mode().values[0]
            assess_dict[col] = {
                'count': stats['count'],
                'mean': stats['mean'],
                'min': stats['min'],
                'max': stats['max'],
                'std': stats['std'],
                'unique_count': int(df[col].nunique()),
                'null_count': df[col].isnull().sum(),
                'most_frequent_value': most_frequent_value,
                'most_frequent_value_count': (df[col] == most_frequent_value).sum(),
                'dtype': df[col].dtype
            }
        # Statistics for non-numeric columns
        else:
            most_frequent_value = df[col].mode().values[0]
            assess_dict[col] = {
                'count': df[col].count(),
                'most_frequent_value': most_frequent_value,
                'most_frequent_value_count': (df[col] == most_frequent_value).sum(),
                'unique_count': int(df[col].nunique()),
                'null_count': df[col].isnull().sum(),
                'dtype': df[col].dtype
            }

    return pd.DataFrame(assess_dict)

 
def handle_missing_values(data):
    """
    Handle missing values in the data.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        
    Returns:
        pd.DataFrame: The DataFrame with missing values handled.
    """
    # Implement logic to handle missing values (e.g., imputation or removal)
    
    df = pd.DataFrame(data)

    columns = list(df.columns)

    for col in columns:
        if df[col].isnull().sum() > 0:
            #Numeric
            if pd.api.types.is_numeric_dtype(df[col]):
                mean = df[col].mean()
                df[col].fillna(mean, inplace=True)
            
            #Non Numeric
            else:
                most_frequent_value = df[col].mode().values[0]
                df[col].fillna(most_frequent_value, inplace=True)
    
    return df



def feature_engineering(data, one_hot_encode=True, drop_originals=True, top_n=5):
    """
    Perform feature engineering transformations on the data.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        
    Returns:
        pd.DataFrame: The DataFrame with feature engineering transformations applied.
    """
    # Implement logic for feature engineering (e.g., date transformations, categorical encoding, new feature creation)
    
    df = pd.DataFrame(data)
    columns = list(df.columns)
    
    for col in columns:
        
        if col == 'id' and drop_originals:
            df.drop(col, axis=1, inplace=True)
             
        # Extracting from data-time
        elif pd.api.types.is_datetime64_dtype(df[col]):
            df[col + '_year'] = df[col].dt.year
            df[col + '_month'] = df[col].dt.month
            df[col + '_day'] = df[col].dt.day
            if drop_originals:
                df.drop(col, axis=1, inplace=True)
                
    # Categorical encoding (One-Hot Encoding)
        elif df[col].dtype == 'object' and one_hot_encode:
            top_categories = df[col].value_counts().nlargest(top_n).index.tolist()
            df[col] = df[col].apply(lambda x: x if x in top_categories else 'Other')
            df = pd.get_dummies(df, columns=[col], prefix=col)
            
            
            
    return df

def preprocess_data(data):
    """
    Preprocess the data by applying necessary preprocessing steps.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        
    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    data = handle_missing_values(data)
    data = feature_engineering(data)
    # Apply any additional preprocessing steps
    return data

if __name__ == '__main__': 
    test()