#importing libraries
import os
os.system('pip install plotly')
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
#loading data
df = pd.read_csv("cleaned_data.csv")
#sidebar
st.sidebar.image("th.jfif")
st.write("")
st.sidebar.write("This dashboard is to go deeper in udemy courses data")
year_filter = st.sidebar.select_slider("Year" , df["Year"].unique())
price_cat_filter = st.sidebar.selectbox("Price category" , df["price_category"].unique())



#body
#row1
st.title("Udemy Dashboard")
a1 , a2 , a3 , a4 = st.columns(4)
a1.metric("No. of courses" ,df["course_id"].value_counts().sum())
a2.metric("Total Profit" ,df["profit"].sum())
a3.metric("Average Price" ,df["price"].mean().round(2))
a4.metric("No. of subscribers" ,df["num_subscribers"].sum())

st.write("")

#row2 
b1 , b2 = st.columns(2)
b1.write("subjects vs. no. of subscribers by year")
b2.write("no. of paid/unpaid courses")

filtered_df = df[df["Year"] == year_filter]
grouped_df = filtered_df.groupby("subject")["num_subscribers"].sum()
fig = px.bar( data_frame= grouped_df.reset_index() ,  x = "subject" , 
             y = "num_subscribers")
b1.plotly_chart(fig , use_container_width= True)


paid_counts = df["is_paid"].value_counts().reset_index()
paid_counts.columns = ["is_paid", "count"]
fig2 = px.pie(data_frame= paid_counts , names= "is_paid" , values= "count")
b2.plotly_chart(fig2 , use_container_width= True) 

st.markdown("No. of subscribers in each subject by price category")
filtered_df = df[df['price_category'].eq(price_cat_filter) | (price_cat_filter == 'All Categories')]
fig3 = px.bar(
    data_frame= filtered_df,
    x='subject',               
    y='num_subscribers',        
    color='price_category')

st.plotly_chart(fig3 , use_container_width= True)
