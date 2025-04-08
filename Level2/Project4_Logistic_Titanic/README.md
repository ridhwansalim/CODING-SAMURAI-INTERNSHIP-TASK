# 🚢 Titanic Survival Prediction - Classification Model

This project is part of my **Coding Samurai Data Science Internship** - **Project 4**.

We built a **logistic regression classifier** to predict whether a passenger survived the Titanic disaster, using Python, pandas, and Scikit-learn.

---

## 📁 Dataset

- Source: [Kaggle Titanic Dataset](https://www.kaggle.com/competitions/titanic)
- Training file used: `train.csv`

---

## 🎯 Objective

To predict passenger survival using logistic regression by analyzing key features like age, sex, ticket class, and fare.

---

## 🔧 Tools & Technologies

- Python
- Pandas
- NumPy
- Seaborn & Matplotlib
- Scikit-learn

---

## 📊 Key Steps

1. **Data Loading & Exploration**  
   - Checked missing values, feature types, and overall structure.

2. **EDA & Visualization**  
   - Explored survival rates based on gender, class, and age.
   - Plotted distribution of numerical features.

3. **Data Cleaning**  
   - Dropped irrelevant columns.
   - Handled missing values in `Age`, `Embarked`, and `Cabin`.

4. **Feature Engineering**  
   - Encoded categorical features (`Sex`, `Embarked`).
   - Scaled features for better model performance.

5. **Model Building**  
   - Used `LogisticRegression` from Scikit-learn.
   - Performed train-test split and trained the classifier.

6. **Model Evaluation**  
   - Evaluated using **Accuracy**, **Precision**, **Recall**, **F1-Score**, and **Confusion Matrix**.

---

## 📈 Results

- **Accuracy**: ~81%
- **Precision/Recall/F1**: Balanced scores
- Confusion matrix visualized to assess classification performance.

---

## 🔮 Future Work

- Experiment with different classifiers (e.g., Random Forest, SVM)
- Hyperparameter tuning
- Better feature engineering
- Handle class imbalance

---

## 🧠 Key Learnings

- Gained hands-on experience with classification problems.
- Learned the importance of preprocessing and feature selection.
- Understood how to evaluate model performance using various metrics.

---

## 📌 Conclusion

Logistic Regression provided a solid baseline for survival prediction. With more tuning and feature engineering, performance can go even higher 🚀

---