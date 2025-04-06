import os

projects = {
    "Project1_Sales_Analysis": {
        "title": "📊 Sales Data Analysis",
        "description": "Perform EDA on a sales dataset to find revenue patterns and business insights.",
    },
    "Project2_Linear_Regression": {
        "title": "📈 Linear Regression Model",
        "description": "Build a simple regression model to predict continuous values.",
    },
    "Project3_EDA_Titanic": {
        "title": "🚢 Titanic Dataset EDA",
        "description": "Explore Titanic survival data using visualization.",
    },
    "Project4_Logistic_Titanic": {
        "title": "🧮 Titanic Logistic Regression",
        "description": "Predict passenger survival using classification.",
    },
    "Project5_TimeSeries_Stocks": {
        "title": "📉 Stock Price Time Series Forecasting",
        "description": "Use time series techniques to forecast stock prices.",
    },
    "Project6_Sentiment_Tweets": {
        "title": "💬 Twitter Sentiment Analysis",
        "description": "Use NLP to analyze the sentiment of tweets.",
    },
}

base_path = os.getcwd()

for level in ["Level1", "Level2", "Level3"]:
    level_path = os.path.join(base_path, level)
    for project in os.listdir(level_path):
        project_info = projects.get(project)
        if project_info:
            project_path = os.path.join(level_path, project)
            readme_path = os.path.join(project_path, "README.md")
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(f"# {project_info['title']}\n\n")
                f.write(f"## 📌 Objective\n{project_info['description']}\n\n")
                f.write("## 📁 Dataset\n- Source: [Add link here]\n- Format: CSV or Excel\n\n")
                f.write("## 🔧 Tools Used\n- Python\n- Pandas, Matplotlib, Scikit-learn, etc.\n\n")
                f.write("## 🧠 Highlights\n- Add key findings here\n\n")
                f.write("## 🖼️ Visuals\n- Include screenshots or graphs\n\n")
                f.write("## 📂 Files\n- Notebook/script\n- Presentation slides\n\n")
                f.write("## 📎 References\n- [Add resources]\n")
