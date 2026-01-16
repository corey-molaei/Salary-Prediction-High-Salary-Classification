# Salary Prediction & High-Salary Classification

**Machine Learning with Python (scikit-learn)**

## 📌 Project Overview

This project demonstrates an end-to-end machine learning workflow for:

1. **Salary Prediction (Regression)**
2. **High-Salary Classification (Binary Classification)**

The goal is to build, evaluate, and compare multiple models while focusing on **generalisation**, **bias–variance trade-off**, and **business-driven model selection** rather than just maximising training accuracy.

---

## 🎯 Business Motivation

* Salary estimation is a common problem in HR, recruitment, and workforce planning.
* In addition to predicting exact salary values, many real-world systems require **classification**, e.g.:

  * Identifying **high-salary candidates**
  * Screening candidates for senior roles
* This project mirrors real industry constraints:

  * Limited data
  * Noisy features
  * Trade-offs between accuracy, robustness, and interpretability

---

## 🧠 What I Learned (Key Takeaways)

* How linear models struggle with non-linear relationships
* How decision trees overfit without regularisation
* How ensemble models reduce variance and improve generalisation
* How to tune Gradient Boosting using **regularisation**, not guesswork
* How to choose a model based on **test performance**, not training score
* How evaluation metrics map to **business decisions**

---

## 📊 Dataset & Features

* **Target (Regression):** Salary
* **Target (Classification):** High salary (binary)
* **Features include:**

  * Age
  * Years of experience
  * Other candidate attributes (numeric)

Data preprocessing includes:

* Feature selection
* Train/test split
* Avoiding data leakage

---

## 🧪 Models & Methodology

### 1️⃣ Baseline — Linear Regression

* Used as a benchmark
* Pros: simple, stable
* Cons: limited ability to capture non-linear patterns

---

### 2️⃣ Decision Tree Regression

* Initially achieved near-perfect training performance
* Severe overfitting observed
* Controlled using `max_depth`

**Key lesson:**

> High training accuracy does not mean a good model.

---

### 3️⃣ Random Forest Regression

* Reduced variance by averaging multiple constrained trees
* Strong improvement in test performance
* Robust and stable default for tabular data

---

### 4️⃣ Gradient Boosting Regression (Tuned & Regularised)

Gradient Boosting was tuned using:

* Shallow trees (`max_depth = 2`)
* Learning rate vs number of estimators trade-off
* Subsampling
* Minimum samples per leaf

**Final configuration achieved:**

* **Test R² ≈ 0.915**
* **RMSE ≈ $6.9k**
* Strong generalisation with controlled overfitting

**Engineering decision:**
Although Random Forest performed well, **regularised Gradient Boosting** was selected due to superior test performance and acceptable stability.

---

## 📈 Final Regression Results

| Model                         | Train R² |   Test R² |      RMSE |
| ----------------------------- | -------: | --------: | --------: |
| Linear Regression             |    ~0.85 |     ~0.85 |    ~9–10k |
| Decision Tree (depth=4)       |     0.90 |      0.76 |    ~11.5k |
| Random Forest                 |     0.93 |      0.87 |     ~8.4k |
| **Gradient Boosting (tuned)** | **0.94** | **0.915** | **~6.9k** |

---

## 🧠 Bias–Variance Perspective

* Linear models → **high bias**
* Deep trees → **high variance**
* Random Forest → variance reduction via averaging
* Gradient Boosting → bias reduction via sequential learning

**Regularisation** (depth, learning rate, subsampling) was essential to prevent overfitting.

---

## 🔍 High-Salary Classification

In addition to regression, the project includes **binary classification**:

* Target: `high_salary` (1 = high, 0 = not high)
* Models evaluated using:

  * Precision
  * Recall
  * Confusion matrix
  * Threshold tuning

### Metric reasoning:

* Recall prioritised when missing high-salary candidates is costly
* Precision prioritised when false positives are costly

This mirrors **real HR screening trade-offs**.

---

## 🛠 Tools & Technologies

* Python
* NumPy
* Pandas
* scikit-learn
* Jupyter Notebook

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
```

Open notebooks in order:

1. `01_exploration.ipynb`
2. `02_regression_models.ipynb`
3. `03_classification_high_salary.ipynb`

---

## 📌 Conclusion

This project demonstrates:

* End-to-end ML thinking
* Model comparison and selection
* Practical regularisation
* Business-aligned evaluation

It reflects how machine learning is applied in **real-world engineering**, not just academic settings.

---

## 👤 Author

**Corey Molaei**
