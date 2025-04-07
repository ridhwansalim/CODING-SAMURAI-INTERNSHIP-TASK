# 🚢 Project 3: Logistic Regression on Titanic Dataset

## 📌 Objective
The goal of this project is to build a binary classification model to predict whether a passenger survived the Titanic disaster based on various features such as age, class, sex, fare, and more.

## 🧠 Problem Statement
Given the Titanic passenger data, we aim to predict the survival outcome (0 = did not survive, 1 = survived) using supervised learning techniques, specifically logistic regression.

## 🗂️ Dataset Information
- **Dataset Name:** Titanic - Machine Learning from Disaster
- **Source:** [Kaggle - Titanic Dataset](https://www.kaggle.com/competitions/titanic/data)
- **Rows:** 891  
- **Columns:** 12  
- **Target Variable:** Survived  
- **Key Features:** Pclass, Sex, Age, SibSp, Parch, Fare, Embarked

## 🛠️ Tech Stack
- **Language:** Python 3
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn

## 🔍 Exploratory Data Analysis
- Visualized survival rates by gender and passenger class
- Handled missing values (especially in 'Age' and 'Embarked')
- Converted categorical features into numeric using Label Encoding
- Explored feature correlations

## 🧪 Model Building
- Used logistic regression as the baseline model
- Split data into training and testing sets (80/20)
- Evaluated model using accuracy, precision, recall, and F1-score
- Used confusion matrix and classification report for diagnostics

## 📊 Evaluation Metrics
- **Accuracy:** 81%
- **Confusion Matrix:** [[90 15] [19 55]]


- **Classification Report:**

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.83      | 0.86   | 0.84     | 105     |
| 1     | 0.79      | 0.74   | 0.76     | 74      |

**Macro Avg:** Precision 0.81 | Recall 0.80 | F1-Score 0.80  
**Weighted Avg:** Precision 0.81 | Recall 0.81 | F1-Score 0.81


## 📈 Visualizations
- Confusion matrix heatmap  
- Survival rate by gender and class  
- Feature importance chart (optional)  

## 📁 Folder Structure

Project_3_Titanic_Classification  
├── Project3_Slides.pdf  
├── README.md  
├── Titanic_Classifier.ipynb  
├── image.png  
├── test.csv  
└── train.csv  


## 📎 Links
- [Kaggle Dataset](https://www.kaggle.com/competitions/titanic)
- [LinkedIn Blog Post](https://www.linkedin.com/posts/ridhwan-s_internship-logisticregression-machinelearning-activity-7314919885023690753-YilI?utm_source=share&utm_medium=member_desktop&rcm=ACoAADgcWwYBA84L3SH9WeTjVFF7wNrT2eTPdTw)
- [Slide Deck](https://www.linkedin.com/posts/ridhwan-s_titanic-survival-prediction-using-logistic-activity-7314905809400778752-yy9g?utm_source=share&utm_medium=member_desktop&rcm=ACoAADgcWwYBA84L3SH9WeTjVFF7wNrT2eTPdTw)

## 📌 Conclusion
This project demonstrates how logistic regression can be used to make binary predictions on real-world datasets. Key learnings include:
- Data cleaning and EDA are critical before modeling
- Categorical variables need to be encoded properly
- Model performance depends heavily on balanced data and relevant features

