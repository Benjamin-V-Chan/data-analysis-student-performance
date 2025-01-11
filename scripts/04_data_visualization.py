import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data):
    """Generate visualizations for the dataset."""
    # Pairplot
    sns.pairplot(data)
    plt.savefig("../outputs/pairplot.png")
    plt.close()
    
    # Heatmap of correlations
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("../outputs/correlation_heatmap.png")
    plt.close()

if __name__ == "__main__":
    file_path = "../outputs/cleaned_data.csv"
    data = pd.read_csv(file_path)
    visualize_data(data)
    print("Visualizations saved to outputs/")