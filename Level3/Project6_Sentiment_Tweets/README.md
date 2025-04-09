# 💬 Sentiment Analysis on Tweets using NLP

This project was completed as part of the **Coding Samurai Data Science Internship**.

We performed sentiment analysis on social media posts (tweets) using Natural Language Processing techniques to determine if a tweet is **positive** or **negative** in sentiment.

---

## 📌 Objective

To develop a machine learning pipeline that processes raw tweets, cleans and tokenizes the text, extracts features using TF-IDF, and builds a classification model to predict sentiment labels (positive or negative).

---

## 🧠 Problem Statement

Given a large dataset of tweets with sentiment labels (`0 = Negative`, `4 = Positive`), our goal is to:
- Clean and preprocess text data
- Extract features using NLP
- Train a classification model
- Evaluate and visualize model performance

---

## 📁 Dataset Details

- **Source**: [Sentiment140 Dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)
- **Total Samples**: 1.6 Million Tweets  
- **Columns**:  
  - `target` — Sentiment (0 = Negative, 4 = Positive)  
  - `id` — Tweet ID  
  - `date` — Timestamp  
  - `query` — Query type (mostly `NO_QUERY`)  
  - `user` — Username  
  - `tweet` — Raw tweet text

---

## 🛠️ Tools & Libraries

- **Language**: Python 3  
- **IDE**: PyCharm  
- **Libraries**:
  - `pandas`, `numpy` — Data manipulation
  - `re` — Regex for text cleaning
  - `nltk` — Tokenization, stopwords, lemmatization
  - `sklearn` — Vectorization, model building, evaluation
  - `matplotlib`, `seaborn`, `wordcloud` — Visualization

---

## 🔄 Workflow

1. **Data Cleaning**
   - Removed URLs, mentions, hashtags, punctuations, etc.
   - Lowercased all text

2. **Text Preprocessing**
   - Tokenized tweets using `nltk.word_tokenize()`
   - Removed stopwords
   - Lemmatized words using `WordNetLemmatizer`

3. **Feature Engineering**
   - TF-IDF vectorizer used to convert text into numerical format

4. **Model Building**
   - Used Logistic Regression for classification
   - Trained on 80% of data, tested on 20%

5. **Evaluation Metrics**
   - Accuracy: **77.38%**
   - Confusion Matrix:
     ```
     [[120000  39494]
      [ 32888 127618]]
     ```
   - F1-Score: 0.77 (Balanced across classes)

6. **Visualization**
   - Word clouds for positive and negative sentiments
   - Bar plots for class distributions

---

## 📊 Model Performance

- **Precision (Positive)**: 0.76  
- **Recall (Positive)**: 0.80  
- **F1-Score (Positive)**: 0.78  
- **Precision (Negative)**: 0.78  
- **Recall (Negative)**: 0.75  
- **F1-Score (Negative)**: 0.77  

Overall, the model generalizes well with balanced precision and recall.

---

## 🔮 Insights

- The model is able to classify tweets with decent accuracy and robustness.
- Text preprocessing and lemmatization played a major role in improving results.
- TF-IDF helped focus on key keywords related to sentiment.

---

## 🧑‍💻 Author

**Ridhwan S**  
_Data Analyst Intern_  
📍 Coding Samurai - Data Science Internship

---

## 📎 Links

- [Dataset on Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140)
- [LinkedIn Blog Post](https://linkedin.com/in/ridhwan-s)
- [GitHub Repository](https://github.com/ridhwansalim/CODING-SAMURAI-INTERNSHIP-TASK)

---

## ✅ Deliverables

- [x] Cleaned and preprocessed tweet data  
- [x] Exploratory analysis and visualization  
- [x] Logistic Regression classifier  
- [x] Evaluation metrics and confusion matrix  
- [x] PowerPoint presentation  
- [x] LinkedIn blog post  
- [x] README.md  

---

## 🚀 Future Improvements

- Try deep learning models like LSTM or BERT  
- Implement multi-class sentiment (positive, neutral, negative)  
- Train on recent real-time tweet data using the Twitter API

---