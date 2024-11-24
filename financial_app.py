import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (replace with your dataset file path)
df = pd.read_excel('dataset.xlsx')

# App title
st.title("Financial Insights Dashboard")

# Family Selection
family_ids = df['Family ID'].unique()
selected_family = st.selectbox("Select a Family ID", family_ids)

# Display Family Data
st.header("Family Transactions")
family_data = df[df['Family ID'] == selected_family]
st.dataframe(family_data)

# Visualizations
st.header("Spending Distribution")
spending_by_category = family_data.groupby('Category')['Amount'].sum().reset_index()
fig, ax = plt.subplots()
sns.barplot(data=spending_by_category, x='Category', y='Amount', ax=ax)
ax.set_title("Spending by Category")
st.pyplot(fig)

# Financial Score API Integration
st.header("Financial Scoring Model")
if st.button("Get Financial Score"):
    # Send request to Flask API
    response = requests.post(
        "http://127.0.0.1:5000/financial-score",  # Replace with your API URL
        json={"family_id": selected_family}
    )
    if response.status_code == 200:
        data = response.json()
        st.write(f"Financial Score for {selected_family}: {data['financial_score']}")
        st.write("Insights:")
        for insight in data['insights']:
            st.write(f"- {insight}")
    else:
        st.error("Error fetching financial score.")

