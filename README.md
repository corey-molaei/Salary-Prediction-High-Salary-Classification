Salary Prediction & High-Salary Classification

Machine Learning with Python (scikit-learn)

📌 Project Overview

This project demonstrates an end-to-end machine learning workflow for:

Salary Prediction (Regression)

High-Salary Classification (Binary Classification)

The focus is on model comparison, generalisation, regularisation, and business-aware evaluation, rather than maximising training accuracy.

🎯 Business Motivation

Salary prediction is widely used in HR analytics, recruitment, and workforce planning.

In many real-world scenarios, predicting an exact salary is not sufficient.

Binary decisions such as identifying high-salary candidates are often required for screening and prioritisation.

This project reflects real industry constraints:

Limited and noisy tabular data

Trade-offs between accuracy, robustness, and interpretability

Business-driven metric selection

📁 Project Structure
salary-ml-prediction/
│
├── README.md
├── data/
│   └── age_experience_salary_100.csv
│
├── notebooks/
│   ├── salary_regression.ipynb
│   └── high_salary_classification.ipynb
│
├── requirements.txt
└── .gitignore


Each notebook loads the dataset independently using relative paths to remain
self-contained and reproducible.

📊 Dataset & Features

Regression target: salary

Classification target: high_salary (binary)

Features include:

Age

Years of experience

Other numeric candidate attributes

Basic preprocessing is performed directly in each notebook to keep them
independent and easy to review.

🧪 Notebook 1 — Salary Prediction (Regression)

Notebook: salary_regression.ipynb

Objective

Predict continuous salary values using multiple regression models and select
the best model based on test performance and generalisation.

Models evaluated

Linear Regression (baseline)

Decision Tree Regression

Regularised Decision Tree (depth control)

Random Forest Regression

Gradient Boosting Regression (tuned & regularised)

Key techniques

Train/test split

Bias–variance analysis

Overfitting detection

Regularisation (tree depth, learning rate, subsampling)

Model comparison using:

R²

RMSE

📈 Final Regression Results

Multiple regression models were evaluated and compared using test performance
and generalisation behaviour.

Model	Train R² (approx)	Test R² (approx)	RMSE (approx)
Linear Regression	~0.85	~0.85	~$9–10k
Decision Tree (regularised)	~0.90	~0.75	~$11–12k
Random Forest	~0.93	~0.87	~$8–9k
Gradient Boosting (regularised)	~0.94	~0.91	~$6–7k
Model selection

After tuning and regularisation, Gradient Boosting achieved the strongest
test performance with the lowest RMSE and highest test R² while maintaining a
controlled train–test gap.

Although Random Forest performed well and offered strong robustness,
regularised Gradient Boosting was selected due to its superior generalisation
and lower prediction error.

🧠 Bias–Variance Perspective

Linear models → higher bias, limited flexibility

Deep decision trees → low bias, high variance (overfitting)

Random Forest → variance reduction through averaging

Gradient Boosting → bias reduction through sequential learning

Regularisation was essential to achieve strong generalisation.

🧪 Notebook 2 — High-Salary Classification

Notebook: high_salary_classification.ipynb

Objective

Classify whether a candidate belongs to a high-salary group.

Methodology

Create a binary target high_salary based on a salary threshold

Train classification models

Evaluate using classification-specific metrics

Metrics used

Confusion matrix

Precision

Recall

F1-score

Probability threshold analysis

🎯 Threshold & Metric Reasoning

Precision is important when false positives are costly

Recall is important when missing high-salary candidates is costly

F1-score provides a balanced metric when both errors matter

Different probability thresholds (e.g. 0.6 vs 0.4) are evaluated to align the
model with real-world decision-making rather than relying on a fixed default.

🧠 Key Learnings

Linear models often underperform on non-linear tabular data

Decision trees overfit without regularisation

Random Forest improves stability via variance reduction

Gradient Boosting can achieve higher accuracy when properly regularised

Model selection should be driven by test performance, not training scores

Metric choice must reflect business objectives

🛠 Tools & Technologies

Python

NumPy

Pandas

scikit-learn

Jupyter Notebook

🚀 How to Run
pip install -r requirements.txt


Then open either notebook:

salary_regression.ipynb

high_salary_classification.ipynb

Each notebook loads the dataset independently and can be run on its own.

📌 Conclusion

This project demonstrates practical machine learning skills including:

End-to-end model development

Bias–variance reasoning

Regularisation and tuning

Business-aligned evaluation and decision-making

It reflects how machine learning models are built, evaluated, and selected in
real-world engineering environments.

👤 Author

Corey Molaei
AI Engineer | Python & Machine Learning
