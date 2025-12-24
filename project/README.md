# Health Insurance Risk Classifier

Analyze health insurance data and classify individuals into low, medium, or high insurance-risk categories using machine learning.

## Dataset
**Health Insurance Charges Dataset** from Kaggle, containing:
- Demographics: age, sex, region
- Health metrics: BMI, smoker status, number of dependents
- Medical charges billed to insurance

**Source:** https://www.kaggle.com/datasets/nalisha/health-insurance-charges-dataset

## Repository Contents

- **`health_insurance_risk_classifier.ipynb`** - Complete analysis pipeline:
  - Data loading, cleaning, and preprocessing
  - Exploratory data analysis with 11 visualizations
  - Rule-based risk classification
  - Neural network model training (TensorFlow/Keras)
  - Model evaluation and performance metrics

- **`data/`** - Dataset files:
  - `health_insurance_data.csv` - Raw data with features (age, BMI, children, sex, smoker, region, charges)
  - `health_insurance.db` - SQLite database with processed data

- **`plots/`** - Generated visualization files (11 plots)

- **`requirements.txt`** - Python dependencies

- **`PROJECT_PLAN.md`** - 5-week project timeline

## Quick Start

### 1. Setup Environment

```bash
cd project
pip install -r requirements.txt
```

### 2. Run the Notebook

```bash
jupyter notebook health_insurance_risk_classifier.ipynb
```

Or open directly in PyCharm (supports Jupyter notebooks).

### 3. Execute Analysis

Run all cells (Cell → Run All) or step by step:

- **Steps 1-4**: Data loading, cleaning, encoding, and normalization
- **Steps 5-7**: Risk classification and database storage
- **Steps 8-12**: Exploratory data analysis and visualizations
- **Steps 13-14**: Neural network training and evaluation
- **Step 15**: Conclusions and key findings

## Model Architecture

**Neural Network:**
- Input: 9 features (age, BMI, children, sex, smoker, 4 regions)
- Hidden layer: 16 neurons with ReLU activation
- Dropout: 30% regularization
- Output: 3 classes (Low/Medium/High risk) with softmax

**Training:**
- Adam optimizer with learning rate 0.01
- Early stopping (patience=50 epochs)
- 80/20 train-test split

## Output

The notebook generates:
- Distribution plots for age, BMI, charges, and risk categories
- Correlation heatmap showing feature relationships
- Classification report with precision, recall, F1-scores
- Confusion matrix (counts and percentages)
- Per-class performance metrics

## Key Findings

- **Smoking status** is the strongest predictor of insurance risk
- Age and BMI positively correlate with risk categories
- Neural network achieves high accuracy in risk classification
- Sex and region have minimal impact on risk

See `PROJECT_PLAN.md` for detailed timeline.

