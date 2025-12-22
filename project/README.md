# Health Insurance Risk Classifier

The aim of this project is to acquire, clean, analyze, and model health-insurance data in order to classify individuals into low, medium, or high insurance-risk categories.

## Dataset
The project uses the publicly available Health Insurance Charges Dataset from Kaggle, which includes:
- Demographic variables: age, sex, region
- Lifestyle variables: BMI, smoker status, number of dependents
- Medical charges billed to insurance

**Source:** https://www.kaggle.com/datasets/nalisha/health-insurance-charges-dataset


## What This Repository Contains

- **`health_insurance_risk_classifier.ipynb`** - Main Jupyter notebook with complete analysis pipeline including:
  - Data loading and preprocessing
  - Exploratory data analysis with visualizations
  - Risk classification logic
  - Neural network model training using TensorFlow/Keras
  - Model evaluation and performance metrics

- **`data/health_insurance_data.csv`** - Dataset containing health insurance information with features:
  - Age, BMI, children, sex, smoker status, region, and charges

- **`requirements.txt`** - Python package dependencies

- **`PROJECT_PLAN.md`** - Detailed 5-week project timeline and milestones

## How to Use

### 1. Setup Environment

```bash
# Navigate to the project directory
cd project

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Notebook

Open the Jupyter notebook in PyCharm or Jupyter:

```bash
jupyter notebook health_insurance_risk_classifier.ipynb
```

Or open directly in PyCharm (supports Jupyter notebooks natively).

### 3. Execute the Analysis

Run all cells in sequence (Cell → Run All) or execute step by step:

- **Step 1-3**: Data loading and preprocessing
- **Step 4**: Data normalization
- **Step 5**: Risk classification
- **Step 6**: Exploratory data analysis and visualizations
- **Step 7**: Neural network model training
- **Step 8**: Model evaluation and predictions

### 4. Understanding the Output

The notebook will generate:
- Distribution plots for age, BMI, and risk categories
- Correlation heatmap
- Classification report with precision, recall, and F1-scores
- Confusion matrix showing prediction accuracy per class
- Comparison table of actual vs predicted risk categories

## Model Evaluation

The TensorFlow neural network model achieves high accuracy in classifying insurance risk. Performance metrics are displayed in the final cells of the notebook.

## Notes

- The model uses a Sequential neural network with one hidden layer (8 nodes) and dropout regularization
- Training includes early stopping to prevent overfitting
- Class imbalance is handled through weighted training

For detailed project timeline and methodology, see `PROJECT_PLAN.md`.
