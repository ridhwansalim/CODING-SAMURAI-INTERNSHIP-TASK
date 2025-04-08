# 📈 Time Series Forecasting of Apple Inc. (AAPL) Stock Prices Using ARIMA

## 🧠 Project Overview

This project applies Time Series Analysis using the ARIMA model to forecast the closing stock prices of Apple Inc. (AAPL). The objective is to build a reliable predictive model, validate its assumptions, and provide clear visual insights into future trends. 

This project was completed as part of the **Coding Samurai Data Science Internship** to fulfill the requirements of the **Time Series Forecasting** module.

---

## 🚀 Objective

- Analyze historical stock prices of Apple Inc.
- Test and ensure the stationarity of the time series data.
- Identify optimal ARIMA parameters using ACF and PACF plots.
- Train an ARIMA model to forecast closing stock prices.
- Evaluate model residuals and verify forecasting accuracy.
- Generate a 30-day forward forecast with confidence intervals.

---

## 🧰 Technologies Used

- **Language**: Python 3.x  
- **IDE**: PyCharm  
- **Libraries**: 
  - pandas, numpy – For data wrangling
  - matplotlib, seaborn – For visualizations
  - statsmodels – For statistical modeling and ARIMA
  - yfinance – For downloading stock data
  - warnings, datetime – For handling environment and utilities

---

## 📚 Dataset

- **Ticker**: AAPL (Apple Inc.)
- **Time Frame**: January 2020 to January 2025
- **Frequency**: Daily stock data (Open, High, Low, Close, Volume)

The analysis specifically focuses on the **'Close' prices** of AAPL for forecasting purposes.

---

## 🔍 Exploratory Data Analysis

- Visualized the daily closing prices to observe trends and volatility.
- Checked for missing values and applied forward filling to handle them.
- Identified overall upward trends, seasonality hints, and sudden price movements.

---

## 📉 Stationarity Check

- Applied the Augmented Dickey-Fuller (ADF) test to the original 'Close' price series.
- Found non-stationarity in the original series (high p-value).
- Performed first-order differencing to stabilize the mean and remove trends.
- Re-ran ADF test and achieved stationarity (p-value ≈ 0.0), confirming readiness for ARIMA modeling.

---

## 🔢 Parameter Selection (p, d, q)

- Used **ACF (AutoCorrelation Function)** and **PACF (Partial AutoCorrelation Function)** plots.
- Determined the differencing order **d = 1**.
- Based on autocorrelation behavior, selected **p = 1** and **q = 0**.
- Chose final model configuration: **ARIMA(1, 1, 0)**.

---

## 🧠 Model Training

- Trained the ARIMA model using the differenced, stationary time series.
- Verified model convergence and inspected summary statistics.
- Achieved a solid AIC value indicating good model fit.
- Inspected model coefficients and ensured statistical significance.

---

## 📊 Residual Diagnostics

- Checked residual plots to ensure no patterns remained.
- Conducted the Ljung-Box test → Residuals showed white noise characteristics.
- Validated that the model assumptions (normality, homoscedasticity, independence) were met.

---

## 📈 Forecasting

- Generated forecasts for the next 30 business days.
- Plotted predicted closing prices with 95% confidence intervals.
- Forecast trend aligned with recent historical trends, indicating slight variability but overall stable projections.

---

## 📝 Conclusion

- ARIMA(1, 1, 0) effectively captured the dynamics of AAPL's stock closing prices.
- Forecasting results were stable and interpretable, with acceptable error levels.
- The model is easily scalable for other stocks or similar time series problems.
- This approach demonstrates practical application of statistical modeling in financial forecasting.

---

## ✅ Deliverables

- 📓 Jupyter Notebook with step-by-step explanations
- 📊 Forecast plots and residual diagnostics
- 🧾 README.md file
- 📝 LinkedIn blog post draft
- 📽️ PowerPoint presentation

---

## 🧑‍💻 Author

**Ridhwan Salim**  
*Data Analyst Intern @ Coding Samurai*  
🔗 [LinkedIn Profile](https://linkedin.com/in/ridhwan-s)

---
``
