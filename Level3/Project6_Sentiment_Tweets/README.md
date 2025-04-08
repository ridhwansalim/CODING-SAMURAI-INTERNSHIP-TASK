# 💬 Sentiment Analysis on Twitter Data Using NLP

This project is part of the **Coding Samurai Data Science Internship**. The goal is to classify tweets as **positive** or **negative** using natural language processing techniques and a machine learning classifier.

---

## 📌 Objective

To build a machine learning model that performs sentiment analysis on tweets using preprocessing, TF-IDF vectorization, and logistic regression.

---

## 📁 Dataset

- **Name:** Sentiment140 Tweets Dataset (`tweets.csv`)
- **Source:** Pre-downloaded CSV based on Sentiment140 structure
- **Size:** 1.6 million tweets
- **Columns:** `target`, `id`, `date`, `query`, `user`, `tweet`

### 📊 Sentiment Labels:
- `0` → Negative  
- `4` → Positive  

---

## 🧠 Skills Applied

- Text cleaning using RegEx
- NLP: Tokenization, Stopword Removal, Lemmatization
- TF-IDF Vectorization
- Supervised Learning (Logistic Regression)
- Evaluation: Accuracy, Confusion Matrix, F1 Score
- Word Cloud Visualization

---

## 🛠️ Tech Stack

- Python 3
- Libraries: pandas, numpy, seaborn, matplotlib, sklearn, nltk, wordcloud

---

## 🔍 Workflow Overview

1. **Data Loading & Inspection**
2. **Data Cleaning** – remove URLs, mentions, special chars
3. **Text Preprocessing** – tokenize, lemmatize, normalize
4. **TF-IDF Vectorization**
5. **Train/Test Split**
6. **Model Training: Logistic Regression**
7. **Evaluation** – confusion matrix, metrics
8. **Visualization** – heatmaps + word clouds

---

## 📊 Model Performance

- **Accuracy:** 77.38%
- **Confusion Matrix:** [[120000 39494] [ 32888 127618]]


- **Classification Report:**

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
|   0   |   0.78    |  0.75  |   0.77   |
|   4   |   0.76    |  0.80  |   0.78   |

---

## 🌩️ Visualizations

- 📉 Confusion Matrix heatmap  
- 📊 Sentiment class distribution  
- ☁️ Word Clouds for Positive & Negative tweets

---

## 📎 Links

- [LinkedIn Blog Post](#) <!-- Update this after publishing -->
- [Slide Deck on LinkedIn](#) <!-- Update this after upload -->

---

## 📌 Conclusion

- Successfully built a sentiment classifier with 77% accuracy
- Preprocessing and TF-IDF played a crucial role in performance
- Word clouds offered visual storytelling for each sentiment class
- This project demonstrates practical NLP and real-world classification

---

## 👨‍💻 Author

**Ridhwan S**  
_Data Analyst Intern at Coding Samurai_  
[LinkedIn](https://linkedin.com/in/ridhwan-s) | [GitHub](https://github.com/ridhwansalim)
