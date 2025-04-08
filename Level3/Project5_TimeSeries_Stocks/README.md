# 📈 Time Series Forecasting of Apple Inc. (AAPL) Stock Prices Using ARIMA

## 🧠 Project Overview

This project applies Time Series Analysis using the ARIMA model to forecast the closing stock prices of Apple Inc. (AAPL). The goal is to build a robust forecasting model, evaluate its performance, and visualize future stock price trends.

This project was completed as part of the **Coding Samurai Data Science Internship** to fulfill the requirements of the **Time Series Forecasting** module.
## 🚀 Objective

- Analyze historical stock prices of Apple Inc.
- Test for stationarity and transform data accordingly.
- Identify ARIMA parameters using ACF and PACF.
- Fit an ARIMA model to the data.
- Forecast future stock prices with confidence intervals.
- Evaluate model residuals for randomness and distribution.
## 🧰 Technologies Used

- **Language**: Python 3
- **IDE**: PyCharm
- **Libraries**:
  - `pandas`, `numpy` – For data manipulation and preprocessing
  - `matplotlib`, `seaborn` – For visualizing trends and diagnostics
  - `statsmodels` – For ARIMA modeling and statistical tests
  - `yfinance` – To fetch stock price data directly from Yahoo Finance
  - `warnings`, `datetime` – Utility tools to manage outputs and date ranges
## 📚 Dataset

The dataset was directly downloaded using the `yfinance` API:

```python
import yfinance as yf
data = yf.download('AAPL', start='2020-01-01', end='2025-01-01')
- **Ticker**: AAPL (Apple Inc.)
- **Time Frame**: January 2020 to January 2025
- **Frequency**: Daily stock data (Open, High, Low, Close, Volume)

> 🔍 The analysis specifically focuses on the **'Close'** prices of AAPL for forecasting purposes.
## 🔍 Exploratory Data Analysis

- Visualized the daily closing prices to observe overall trends.
- Checked for missing values and handled them using forward-fill.
- Observed general upward movement with periodic volatility.
- No drastic outliers were detected in the raw data.
## 📉 Stationarity Check

- Applied the Augmented Dickey-Fuller (ADF) test on the original closing price series.
- The test indicated non-stationarity (p-value > 0.05).
- Differenced the series once (d = 1) to stabilize the mean.
- Re-ran the ADF test on the differenced series:
  - ADF Test Statistic: -49.20
  - p-value: 0.00
- Result: The differenced series is stationary.
## 🔢 Parameter Selection

- Used **Autocorrelation Function (ACF)** and **Partial Autocorrelation Function (PACF)** plots to identify suitable ARIMA parameters.
- Observed:
  - ACF cut off slowly after lag 1
  - PACF showed a significant spike at lag 1
- Based on the visual cues and model performance, selected:
  - **ARIMA(1, 1, 0)** → AR = 1, differencing = 1, MA = 0
## 🧠 Model Fitting

- Built and trained an **ARIMA(1, 1, 0)** model on the differenced 'Close' price series.
- Utilized `statsmodels`' `ARIMA` class for model training.
- Achieved:
  - **Log-Likelihood**: -5544.78
  - **AIC**: 11093.57
  - **BIC**: 11105.28

The model successfully converged, indicating a good fit with minimal overfitting or underfitting.
## 📊 Residual Diagnostics

- Plotted residuals to visually assess their distribution.
- Performed statistical tests to confirm assumptions:
  - **Ljung-Box Test**: No significant autocorrelation (p > 0.05).
  - **Jarque-Bera Test**: Residuals show slight non-normality (common in financial time series).
  - **Heteroskedasticity Test (H-test)**: Detected presence of volatility clustering.
- **Conclusion**: Residuals are close to white noise, making the ARIMA model appropriate for short-term forecasting.
