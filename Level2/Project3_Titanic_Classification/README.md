# 🚢 Project 3: Exploratory Data Analysis (EDA) on Titanic Dataset

## 🧠 Objective
The goal of this project is to perform a detailed Exploratory Data Analysis (EDA) on the Titanic dataset. We'll uncover insights into survival patterns, clean the data, handle missing values, and visualize key relationships between features.

This project is part of my Data Science Internship at **Coding Samurai**.

---

## 📂 Dataset Overview

- **Dataset:** Titanic - Machine Learning from Disaster  
- **Source:** [Kaggle Titanic Competition](https://www.kaggle.com/competitions/titanic)  
- **Rows:** 891  
- **Columns:** 12  
- **Target Variable:** `Survived` (0 = No, 1 = Yes)

---

## 🔍 Key Questions Explored

- What factors influenced survival rates on the Titanic?
- Did gender, age, or passenger class impact survival?
- How are features correlated with each other?
- How can we clean and prepare the data for modeling?

---

## 🛠️ Tools & Libraries

- **Language:** Python 3  
- **Libraries:** pandas, numpy, matplotlib, seaborn  

---

## 📊 EDA Highlights

### ✅ Data Cleaning:
- Dropped unnecessary columns: `Cabin`, `Name`, `Ticket`, `PassengerId`
- Handled missing values in `Age` (filled with median) and `Embarked` (filled with mode)

### 📈 Visual Analysis:
- Countplots to show survival by gender and class  
- Histograms of Age and Fare  
- Boxplots to compare Fare across classes  
- Correlation heatmap of numeric features

### 🔢 Feature Encoding:
- Converted `Sex` to binary format (0 = male, 1 = female)
- Applied one-hot encoding on `Embarked` with `get_dummies()`

---

## 📌 Key Insights

- **Females** had a significantly higher survival rate than males
- **Higher-class** passengers (Pclass 1) were more likely to survive
- **Fare** and **age** distributions showed survival advantages for higher-paying and younger passengers
- `Sex`, `Pclass`, and `Fare` showed strong correlations with the `Survived` column

--- 

## 📁 Folder Structure

Project_3_Titanic_Classification  
├── Project3_Slides.pdf  
├── README.md  
├── Titanic_Classifier.ipynb  
├── image.png  
├── test.csv  
└── train.csv  


---

## 📎 Useful Links

- 🔗 [Kaggle Dataset](https://www.kaggle.com/competitions/titanic)
- 🧠 [Blog Post](https://www.linkedin.com/posts/ridhwan-s_datascience-internship-titaniceda-activity-7315026177813884930-ok0T?utm_source=share&utm_medium=member_desktop&rcm=ACoAADgcWwYBA84L3SH9WeTjVFF7wNrT2eTPdTw)
- 📽️ [Slide Deck](https://www.linkedin.com/posts/ridhwan-s_titanic-dataset-survival-analysis-with-eda-activity-7315023344540565505-aSJn?utm_source=share&utm_medium=member_desktop&rcm=ACoAADgcWwYBA84L3SH9WeTjVFF7wNrT2eTPdTw)

---

## 🙌 Conclusion

This project showcased the power of **exploratory data analysis** in understanding a real-world dataset. EDA is the **first and most critical** step before any machine learning modeling. It helps spot trends, detect outliers, and build strong domain intuition.

**Next Step?** This cleaned dataset is now ready for building a predictive model (e.g., logistic regression or random forest).

---