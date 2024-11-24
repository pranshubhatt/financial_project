# Financial Insights Dashboard and Scoring Model

This project involves building a financial insights dashboard and scoring model to analyze family-level and member-level financial health. The project includes data preprocessing, scoring model implementation, visualizations, an API for score calculations, and a Streamlit-based interactive dashboard.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [File Structure](#file-structure)
5. [Setup Instructions](#setup-instructions)
6. [Usage Guide](#usage-guide)
   - [Jupyter Notebook](#jupyter-notebook)
   - [Flask API](#flask-api)
   - [Streamlit Dashboard](#streamlit-dashboard)
7. [Visualizations](#visualizations)
8. [Future Enhancements](#future-enhancements)
9. [Acknowledgements](#acknowledgements)

---

## Introduction

The **Financial Insights Dashboard and Scoring Model** aims to evaluate financial health at the family and member levels. The project provides actionable insights, including category-wise spending, financial health scoring, and recommendations for improvement.

---

## Features

- **Data Preprocessing**: Cleaning and transforming financial data.
- **Scoring Model**: A custom scoring mechanism to evaluate financial health (range: 0–100).
- **Visualizations**:
  - Spending trends over time.![Screenshot 2024-11-24 123238](https://github.com/user-attachments/assets/cf21b2a4-d752-49d3-9826-90c0b9496f7f)
  - 
  - Category-wise spending distribution.
  - Top families by financial scores.
  - Correlation matrix for financial metrics.![Screenshot 2024-11-24 123155](https://github.com/user-attachments/assets/c8856cac-f5c1-4831-98f3-4599a98c3982)
  - 
- **Interactive Simulation**:
  - Users can simulate financial improvements and view updated scores.
- **API**: A Flask API to compute financial scores and provide insights.
- **Streamlit Dashboard**: An interactive interface for users to explore financial insights.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - Data Analysis: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`, `plotly`
  - API Development: `Flask`
  - Interactive Dashboard: `Streamlit`
- **Tools**: Jupyter Notebook, Postman

---

## File Structure

```plaintext
financial_project/
├── app/
│   ├── financial_api.py       # Flask API
├── data/
│   ├── dataset.xlsx           # Dataset
├── notebooks/
│   ├── code.ipynb             # Jupyter Notebook with visualizations and logic
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── setup_instructions.md      # Installation and usage instructions
