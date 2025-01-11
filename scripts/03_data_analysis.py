import pandas as pd

def analyze_data(data):
    """Perform basic analysis on the dataset."""
    correlation_matrix = data.corr()
    print("Correlation Matrix:\n", correlation_matrix)
    summary_statistics = data.describe()
    print("Summary Statistics:\n", summary_statistics)
    return correlation_matrix, summary_statistics

if __name__ == "__main__":
    file_path = "../outputs/cleaned_data.csv"  # Adjust path if needed
    data = pd.read_csv(file_path)
    corr_matrix, summary_stats = analyze_data(data)
    corr_matrix.to_csv("../outputs/correlation_matrix.csv")
    summary_stats.to_csv("../outputs/summary_statistics.csv")
    print("Analysis results saved to outputs/")

# Perform analysis on dataset
    # Correlation matrix
    # Summary statistics
    # Use .corr() and .describe()
# Save both to csv in outputs/

# Use pandas as temp DF