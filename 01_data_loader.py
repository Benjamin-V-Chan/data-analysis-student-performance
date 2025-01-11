import pandas as pd

def load_data(file_path):
    """Load the dataset and print basic information."""
    data = pd.read_csv(file_path)
    print("Shape of the dataset:", data.shape)
    print("Columns:", data.columns)
    print("Missing values:\n", data.isnull().sum())
    print("Sample data:\n", data.head())
    return data

if __name__ == "__main__":
    file_path = "../data/data.csv"
    data = load_data(file_path)