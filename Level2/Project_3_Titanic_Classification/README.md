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
- **Confusion Matrix:**
- [[90 15] [19 55]]

- **Classification Report:**
- Precision: 0.83 (Class 0), 0.79 (Class 1)
- Recall: 0.86 (Class 0), 0.74 (Class 1)
- F1-Score: 0.84 (Class 0), 0.76 (Class 1)

## 📈 Visualizations
- Confusion matrix heatmap  
- Survival rate by gender and class  
- Feature importance chart (optional)  

## 📁 Folder Structure
- Project_3_Titanic_Classification/
- ├── Titanic_Classifier.ipynb         # Logistic regression and evaluation
- ├── train.csv                        # Training dataset
- ├── test.csv                         # Test dataset
- ├── image.png                        # Visual asset for blog/LinkedIn
- ├── Project3_Slides.pdf              # Final presentation slides
- ├── README.md                        # Project README

## 📎 Links
- [Kaggle Dataset](https://www.kaggle.com/competitions/titanic)
- [LinkedIn Blog Post](#)
- [Slide Deck](#)

## 📌 Conclusion
This project demonstrates how logistic regression can be used to make binary predictions on real-world datasets. Key learnings include:
- Data cleaning and EDA are critical before modeling
- Categorical variables need to be encoded properly
- Model performance depends heavily on balanced data and relevant features

