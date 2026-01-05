Customer Churn Analysis

End-to-End Data Science Project (MySQL to Machine Learning)

Overview

This project is an end-to-end Customer Churn Analysis that simulates a real-world company workflow.
Instead of starting from a static CSV file, the project begins at the database level, reflecting how data is commonly generated, stored, and processed in an enterprise environment.

The workflow covers database creation, data generation, data extraction, exploratory data analysis, feature engineering, and machine learning modeling using LightGBM.

Workflow Summary

Generate data and store it in MySQL

Extract data from MySQL into CSV

Perform EDA and feature engineering

Train a LightGBM classification model

Generate churn predictions

Database and Data Generation

Data is generated using Python and stored in a MySQL database to simulate production data.

Key characteristics:

10,000 customers

20,000 transactions

Relational structure (customers and transactions)

Tools:

MySQL

Python

Faker

VS Code

The data generation process is implemented in generateddummy.py, which connects to MySQL, truncates existing tables to avoid duplication, and inserts new customer and transaction records.

Data Extraction

After populating the database:

5,000 rows are queried from MySQL

Data is exported to CSV format

The extracted file is used as the modeling dataset

File:

dataset.csv

Exploratory Data Analysis (EDA)

EDA focuses on understanding customer behavior and churn patterns, including:

Customer demographic distribution

Transaction behavior analysis

Churn vs non-churn comparison

Summary statistics and correlations

All analysis steps are documented in the notebook.

Feature Engineering

Feature engineering is performed to improve model performance by:

Aggregating transaction-level data into customer-level features

Creating behavioral metrics such as frequency and total spending

Encoding categorical variables

Selecting relevant features

Output:

feature_importance.csv

Machine Learning Model

Model:

LightGBM (LGBM) Classifier

Objective:

Predict whether a customer will churn based on demographic and transactional behavior

Output:

churn_predictions.csv

Repository Structure
├── LICENSE
├── README.md
├── churn_predictions.csv
├── dataset.csv
├── feature_importance.csv
├── generateddummy.py
├── kode.ipynb

Tech Stack

Python

MySQL

Pandas

NumPy

Matplotlib

Seaborn

LightGBM

Faker

Jupyter Notebook

VS Code

Key Takeaways

Simulates a real-world data workflow starting from a relational database

Demonstrates database handling, data analysis, and machine learning modeling

Covers the complete data science pipeline from data generation to prediction

Suitable for Data Analyst and Data Scientist portfolios
