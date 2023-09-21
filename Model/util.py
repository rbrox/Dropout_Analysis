import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def table_heads(tables):
    """
    Prints table heads, return nothing
    """
    for index in len(tables):
        tables[index].head()
        print("\n")


def visualize_data(data):
    """
    Visualize the data.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
    """
    # Perform data visualization
    plt.figure(figsize=(8, 6))
    sns.histplot(data['sales'])
    plt.title('Sales Distribution')
    plt.xlabel('Sales')
    plt.ylabel('Count')
    plt.show()
