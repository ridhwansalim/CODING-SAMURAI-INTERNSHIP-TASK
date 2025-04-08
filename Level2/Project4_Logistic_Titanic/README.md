# 🚢 Titanic Survival Prediction - Logistic Regression Model

This project is part of my **Coding Samurai Data Science Internship (Project 4)**.  
We build a classification model to predict whether a passenger survived the Titanic disaster based on features like age, gender, ticket class, and fare.

---

## 📌 Project Overview

- **Dataset**: Titanic Dataset from [Kaggle](https://www.kaggle.com/competitions/titanic)
- **Problem Type**: Binary Classification
- **Model Used**: Logistic Regression (Scikit-learn)

---

## 🧠 Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering and encoding
- Train-test splitting
- Logistic Regression model training
- Model evaluation using accuracy, confusion matrix, and classification report

---

## 🧹 Data Preprocessing

- Dropped irrelevant columns: `Cabin`, `Ticket`, `Name`, `PassengerId`
- Filled missing `Age` with median and `Embarked` with mode
- Converted categorical variables (`Sex`, `Embarked`) to numeric
- Used one-hot encoding for multi-class categorical features

---

## 📈 Model Performance

- **Accuracy**: ~81%
- **Confusion Matrix**: [[90 15] [19 55]]
- **Classification Report**:
            precision    recall  f1-score   support

     0       0.83      0.86      0.84       105
     1       0.79      0.74      0.76        74

accuracy                           0.81       179
macro avg 0.81 0.80 0.80 179 weighted avg 0.81 0.81 0.81 179

yaml
Copy
Edit


---

## 📊 Key Visualizations

- Survival by Gender and Passenger Class
- Fare and Age Distributions
- Correlation Heatmap
- Confusion Matrix Heatmap

---

## 🚀 Future Improvements

- Try Random Forest or Gradient Boosting for better performance
- Use grid search for hyperparameter tuning
- Deal with class imbalance (if detected)
- Add feature importance plots

---

## 📁 File Structure

├── titanic_logistic_regression.ipynb ├── README.md ├── presentation.pptx ├── titanic.csv (train dataset)

---

## 🙋‍♂️ Author

**Ridhwan S**  
_Data Analyst Intern @ Coding Samurai_

---

## 🧠 Inspiration

Inspired by the classic Titanic ML challenge from Kaggle. This project helped me deepen my understanding of classification, model evaluation, and feature engineering.

