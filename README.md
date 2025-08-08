# 🍽️ Plates and Predictions – Forecasting Online Food Orders

**Plates and Predictions** is an interactive data analysis and forecasting web application for online food orders.
It allows restaurants, aggregators, and food delivery platforms to analyze order patterns, predict demand, and track customer loyalty & churn using real order data.

## 🚀 Features

📊 Order Distribution Insights across hour, weekday, and month
📈 Weekly Order Forecasting using Simple Moving Average (SMA)
🛍 Customer Loyalty Analysis based on purchase frequency and restaurant diversity
🏆 Key Metrics Dashboard – delivery times, payment preferences, and peak order times
🍴 Top Restaurants Analysis by order count
🔄 Churn Rate Calculation to identify inactive customers
📉 Visualized insights via an interactive Streamlit dashboard

## 📂 Project Structure

-├── preprocessed_online_food_orders.csv   # Cleaned dataset
-├── prep.py                               # Script for dataset preprocessing
-├── key.py                                # Helper functions for plotting & preprocessing
-├── Streamlit.py                          # Main Streamlit app
-├── README.md                             # Documentation

## 🛠 Tech Stack

- Python
- Pandas – Data manipulation
- Matplotlib & Seaborn – Visualizations
- Streamlit – Web application framework
- NumPy – Numerical computations

## 🔍 How It Works

1. Preprocessing (prep.py)
Loads raw CSV dataset
Cleans and standardizes column names
Extracts hour, weekday, month, and delivery time features
Saves preprocessed dataset for analysis

2. Analysis & Predictions (Streamlit.py)
Order Distribution Analysis: Hourly, daily, and monthly order patterns
Weekly Orders Forecast: Uses SMA for next week prediction
Customer Loyalty Analysis: Scores & categories customers
Key Metrics & Restaurant Insights: Delivery time, payment method, top restaurants
Churn Analysis: Finds customers inactive for 180+ days

## 🖥 How to Run the App

1️⃣ Clone the Repo
git clone https://github.com/yourusername/plates-and-predictions.git
cd plates-and-predictions

2️⃣ Install Requirements
pip install streamlit pandas matplotlib seaborn numpy

3️⃣ Run the Dashboard
streamlit run Streamlit.py

4️⃣ Upload Dataset (CSV) or use the provided preprocessed_online_food_orders.csv

## 💡 Use Cases

-📆 Demand Forecasting for restaurants and delivery platforms
-📊 Customer Retention & Loyalty Tracking
-🏪 Restaurant Performance Monitoring
-📈 Peak Time Identification for staffing and inventory planning
-🔄 Churn Reduction Strategies

## 👩‍💻 Author
**Devadarshini P**  
[🔗 LinkedIn](https://www.linkedin.com/in/devadarshini-p-707b15202/)  
[💻 GitHub](https://github.com/Devadarshini9000)

"Predict tastes. Predict trends. Serve smarter." – Plates and Predictions
