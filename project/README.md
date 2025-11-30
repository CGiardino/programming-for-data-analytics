# Project Description
The aim of this project is to acquire, clean, analyze, and model health-insurance data in order to classify individuals into low, medium, or high insurance-risk categories.  
The project will use the publicly available Health Insurance Charges Dataset (Kaggle), which includes demographic and lifestyle variables (age, BMI, smoker status, sex, region, and number of dependents) along with total medical charges billed to insurance.  
Source: https://www.kaggle.com/datasets/nalisha/health-insurance-charges-dataset.  
The final result is a **Jupyter Notebook** including data acquisition, analysis, modeling, and visualizations. 

The project is structured over a 5-week timeline as follows:

### Week 1 : Data Setup, Cleaning & Preprocessing
1. Review and Load the dataset
2. Define the risk-classification target (low / medium / high)
3. Clean the data (handle types, normalize numeric features, encode categorical)
4. Create risk labels from charges
5. Create an SQLite database and store the cleaned dataset
6. Run simple SQL queries to confirm correct storage and retrieval

### Week 2 : Exploratory Data Analysis
1. Load data from SQLite into pandas
2. Plot distributions (age, BMI, charges, risk classes)
3. Examine correlations
4. Summarize key findings

### Week 3 : Neural Network Model
1. Split data into training and test sets
2. Build and train a neural-network classifier
3. Validate and tune

### Week 4 : Model Evaluation
1. Evaluate accuracy, loss

### Week 5 : Final Review & Submission
1. Re-run all analyses for consistency
2. Improve formatting and clarity
3. Review references
4. Final commit and submission