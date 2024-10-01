import pandas as pd
import streamlit as st
import plotly.express as px

# laoding the dataset in the dataframe
df = pd.read_csv('vehicles_us.csv')
#the app header
st.header("Used Vehicles Data")
# calculating lower and upper outliers
lower = df['price'].quantile(0.5)
upper = df['price'].quantile(0.95)

#using checkbox to excludes the outliers
exclude_outliers = st.checkbox("if you don't wanna see outliers from price distribution")

if exclude_outliers:
    #filter the data to exclude outliers
    filtered_df = df[(df['price'] >= lower) & (df['price'] <= upper)]
    st.write(f'Outliers excluded. Showing prices between ${lower:.2f} and ${upper:.2f}.')

else:
    filtered_df = df

# histogram for the price colum
hist = px.histogram(filtered_df, x='price', title='Cars Price Distribution')

#displaying the histogram through streamlit
if st.checkbox("Show Histogram: Price Distribution"):
    st.plotly_chart(hist)

#creating a scatter plot for price vs mileage
scatter_plot = px.scatter(filtered_df, x='price', y='odometer', title='Price Vs Mileage')
#displaying the chart below

if st.checkbox("Show Scatter_plot: Price vs Mileage"):
    st.plotly_chart(scatter_plot)
#showing raw data
if st.checkbox("Raw data"):
    st.write(filtered_df)


