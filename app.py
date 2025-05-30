import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Video Game Sales Analysis")

# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv("vgsales.csv")
    data = data[data['Year'] <= 2015]  # Drop rows with year > 2015
    return data

data = load_data()

st.subheader("Raw Data")
st.dataframe(data.head(50))

# Basic statistics
st.subheader("Basic Statistics")
st.write(data.describe())

# Sales by Genre
st.subheader("Total Global Sales by Genre")
sales_by_genre = data.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)
fig, ax = plt.subplots()
sales_by_genre.plot(kind="bar", ax=ax)
plt.ylabel("Global Sales (millions)")
st.pyplot(fig)

# Sales over Years
st.subheader("Average Global Sales per Year")
yearly_sales = data.groupby("Year")["Global_Sales"].mean()
fig2, ax2 = plt.subplots()
yearly_sales.plot(ax=ax2)
plt.ylabel("Average Global Sales")
plt.xlabel("Year")
st.pyplot(fig2)

# Sales by Platform
st.subheader("Top 10 Platforms by Global Sales")
platform_sales = data.groupby("Platform")["Global_Sales"].sum().sort_values(ascending=False).head(10)
fig3, ax3 = plt.subplots()
platform_sales.plot(kind="bar", ax=ax3)
plt.ylabel("Global Sales (millions)")
st.pyplot(fig3)
