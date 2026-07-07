# Stock Market Trend Forecasting using LSTM

## Overview

This project predicts the next day's stock closing price using a Long Short-Term Memory (LSTM) neural network trained on historical Apple stock prices.

## Features

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Data normalization using MinMaxScaler
- LSTM-based prediction model
- Performance evaluation
- Visualization of training loss
- Actual vs Predicted stock prices

## Technologies

- Python
- TensorFlow
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Dataset

Apple stock historical data from the Kaggle Price & Volume dataset.

## Project Structure

```
Stock-Market-LSTM
│
├── data
├── graphs
├── models
├── notebooks
├── src
├── README.md
├── requirements.txt
└── .gitignore
```

## Results

The model successfully learns historical price trends and predicts future closing prices with low prediction error.

## Future Improvements

- GRU model comparison
- Hyperparameter tuning
- Multi-stock forecasting
- Attention-based LSTM