🎯 *Predicting Titanic passenger survival with an 81% accuracy logistic regression model as part of my Data Science Internship.*

# 🚢 Titanic Survival Prediction - Logistic Regression

This project is part of the **Coding Samurai Data Science Internship**.

We built a **Logistic Regression model** using Python and Scikit-learn to predict whether a passenger survived the Titanic tragedy based on features like age, sex, ticket class, and more.

---

## 📚 Table of Contents

- [Project Objective](#-project-objective)
- [Dataset](#-dataset)
- [Skills Used](#-skills-used)
- [Workflow](#️-workflow)
- [Model Evaluation](#-model-evaluation)
- [Key Learnings](#-key-learnings)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [Connect with Me](#-connect-with-me)

---
## 📌 Project Objective

To apply classification techniques using Logistic Regression to model survival on the Titanic.

---

## 📂 Dataset

- **Source**: [Kaggle Titanic Dataset](https://www.kaggle.com/competitions/titanic)
- **Features Used**:  
  `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`, `Embarked`

---

## 🧪 Skills Used

- Data cleaning & wrangling (Pandas, NumPy)  
- Data visualization (Matplotlib, Seaborn)  
- Feature engineering  
- Classification with Logistic Regression  
- Model evaluation (Confusion Matrix, Precision, Recall, F1-score)

---

## 🛠️ Workflow

1. **Data Loading**  
2. **Exploratory Data Analysis (EDA)**  
3. **Handling Missing Values**  
4. **Feature Encoding**  
5. **Train-Test Split**  
6. **Model Training with Logistic Regression**  
7. **Evaluation using Accuracy & Confusion Matrix**

---

## 📈 Model Evaluation

- **Accuracy**: `81%`  
- **Confusion Matrix:**
    ```
    [[90 15]
     [19 55]]
    ```
- **Classification Report:**
    ```
              precision    recall  f1-score   support

           0       0.83      0.86      0.84       105
           1       0.79      0.74      0.76        74

    accuracy                           0.81       179
    macro avg       0.81      0.80      0.80       179
    weighted avg    0.81      0.81      0.81       179
    ```

---

## 🧠 Key Learnings

- Logistic regression is highly interpretable for binary classification.
- Data preprocessing & feature engineering significantly affect model performance.
- Model evaluation metrics help reveal deeper insights beyond accuracy.

---

## 📎 Future Improvements

- Use ensemble methods like Random Forest or Gradient Boosting.
- Try cross-validation for stability.
- Perform hyperparameter tuning with GridSearchCV.
- Deal with class imbalance using SMOTE or class weighting.

---

## 🧑‍💻 Author

**Ridhwan S**  
_Data Analyst Intern_  
📍 Coding Samurai - Data Science Internship

---

## 🔗 Connect with Me

[LinkedIn](https://linkedin.com/in/ridhwan-s) | [GitHub](https://GitHub.com/ridhwansalim)