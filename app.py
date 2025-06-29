import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("🪑 Furniture Sales Dashboard")

# Load data
df = pd.read_csv("ecommerce_furniture_dataset.csv")

# Data cleaning
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
df['originalPrice'] = df['originalPrice'].replace('[\$,]', '', regex=True).astype(float)
df['discount'] = ((df['originalPrice'] - df['price']) / df['originalPrice']) * 100
df.dropna(inplace=True)

# Sidebar filters
st.sidebar.header("Filter Options")
shipping = st.sidebar.multiselect("Shipping Type", options=df['tagText'].unique(), default=df['tagText'].unique())
price_range = st.sidebar.slider("Price Range", float(df['price'].min()), float(df['price'].max()), (float(df['price'].min()), float(df['price'].max())))

# Apply filters
filtered_df = df[(df['tagText'].isin(shipping)) & (df['price'].between(price_range[0], price_range[1]))]

# Show data
st.subheader("📄 Filtered Data")
st.write(filtered_df.head())

# Charts
st.subheader("📈 Price vs Sold")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=filtered_df, x='price', y='sold', hue='tagText', ax=ax1)
st.pyplot(fig1)

st.subheader("📊 Discount Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_df['discount'], kde=True, bins=20, ax=ax2)
st.pyplot(fig2)

st.markdown("Made with  using Streamlit")
