import pandas as pd

def clean_data(data):
    """Clean the dataset by handling missing values and normalizing numerical columns."""
    # Check for missing values
    if data.isnull().sum().any():
        data = data.fillna(data.mean())

    # Normalize numerical columns
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    data[numeric_columns] = (data[numeric_columns] - data[numeric_columns].mean()) / data[numeric_columns].std()
    
    return data

if __name__ == "__main__":
    file_path = "../data/data.csv"
    data = pd.read_csv(file_path)
    cleaned_data = clean_data(data)
    cleaned_data.to_csv("../outputs/cleaned_data.csv", index=False)
    print("Cleaned data saved to outputs/cleaned_data.csv")