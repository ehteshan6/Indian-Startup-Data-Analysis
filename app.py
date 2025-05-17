import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Indian Startup Funding Analysis", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data\\cleaned_startup.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month_name'] = df['date'].dt.strftime('%B')
    return df

df = load_data()

# Title and description
st.title("🚀 Indian Startup Funding Dashboard")
st.markdown("""
This dashboard provides insights into the Indian startup ecosystem from 2015 to 2017.
You can explore funding trends, top cities, industries, and investors.
""")

# Sidebar filters
st.sidebar.header("📅 Filter by:")
years = st.sidebar.multiselect("Select Year(s):", options=df['year'].unique(), default=df['year'].unique())
df = df[df['year'].isin(years)]

# KPI Metrics
total_funding = df['Amount in USD'].sum()
total_investments = df.shape[0]
unique_startups = df['Startup Name'].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Funding (USD)", f"${total_funding:,.0f}")
col2.metric("📊 Number of Deals", total_investments)
col3.metric("🚀 Unique Startups", unique_startups)

st.markdown("---")

# Funding by Year
st.subheader("📈 Funding Over the Years")
funding_by_year = df.groupby('year')['Amount in USD'].sum()
st.bar_chart(funding_by_year)

# Top Industries
st.subheader("🏭 Top 10 Funded Industries")
top_industries = df.groupby('Industry Vertical')['Amount in USD'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_industries)

# Top Cities
st.subheader("📍 Top 10 Cities by Funding")
top_cities = df.groupby('City  Location')['Amount in USD'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_cities)

# Top Investors
st.subheader("💼 Top 10 Investors")
top_investors = df.groupby('Investors Name')['Amount in USD'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_investors)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Ehteshan Alam")
st.markdown("Waiting for her..")
