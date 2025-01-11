# data-science-student-performance

This project analyzes student performance data to uncover insights and trends that can help improve educational outcomes. The project is structured to include scripts for data loading, cleaning, analysis, and visualization, with all results saved in an `outputs/` folder.

## Project Structure

```
project/
├── data/
│   ├── data.csv                # Raw dataset file
├── scripts/
│   ├── data_loader.py          # Script to load and inspect the dataset
│   ├── data_cleaner.py         # Script to clean and preprocess the dataset
│   ├── data_analysis.py        # Script to perform statistical analysis
│   ├── data_visualization.py   # Script to generate visualizations
├── outputs/                    # Folder for storing results (e.g., cleaned data, analyzed csv's, etc.)
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

## Usage

1. **Set up the environment**:
   - Install Python (version >= 3.8 recommended).
   - Install dependencies using the command:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the scripts**:
   - Load the data: Run `scripts/data_loader.py` to inspect the dataset.
   - Clean the data: Run `scripts/data_cleaner.py` to clean and preprocess the data.
   - Analyze the data: Run `scripts/data_analysis.py` to perform correlation analysis and generate summary statistics.
   - Visualize the data: Run `scripts/data_visualization.py` to generate visualizations.

3. **View results**:
   - Results such as cleaned data, correlation matrix, summary statistics, and plots will be saved in the `outputs/` folder.

## Requirements

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:

- pandas
- matplotlib
- seaborn

## Acknowledgements

The dataset used in this project is titled "Predict Student Performance Dataset" and was created by **Umair Zia**. The dataset is available on Kaggle at the following link: [Predict Student Performance Dataset](https://www.kaggle.com/datasets/stealthtechnologies/predict-student-performance-dataset).
