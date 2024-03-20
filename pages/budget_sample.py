from datetime import datetime
import pandas as pd
import streamlit as st
import os
import plotly.express as px

import streamlit as st

def data_processing():
   data_root_path = './data/budget/'
   files = os.listdir(data_root_path)
   df = pd.DataFrame()
   for f in files:
      if 'pyk' in f and 'csv' in f:
         data_path = data_root_path + f
         df_csv = pd.read_csv(data_path)
         df_csv = df_csv[['Date', 'Magasin', 'Objet', 'Montant', 'Catégorie', 'Remarque']]
         df_csv = df_csv[df_csv['Date'].notnull()]
         df = pd.concat([df, df_csv])


   df['Date'] = pd.to_datetime(df['Date'])

   df['year'] = df['Date'].dt.year
   df['month'] = df['Date'].dt.month
   df['day'] = df['Date'].dt.day

   df['Montant'] = pd.to_numeric(df['Montant'].str.replace(',', ''), errors='coerce')
   df['YearMonth'] = df['Date'].map(lambda x: datetime(x.year, x.month, 1))
   return df


def eda(df, container): # TODO separate data preoess and viz
   with st.sidebar:

      year_list = list(df.year.unique())[::-1]

      selected_year = st.selectbox('Select a year', year_list, index=len(year_list) - 1)
      df_selected_year = df[df.year == selected_year]
      df_selected_year_sorted = df_selected_year.sort_values(by="Montant", ascending=False)

      month_list = list(df.month.unique())[::-1]
      selected_month = st.selectbox('Select a month', month_list, index=len(month_list) - 1)
      df_selected_month = df[df.month == selected_month]
      df_selected_month_sorted = df_selected_month.sort_values(by="Date", ascending=True)
      df_selected_month_sorted['cumsum_sales'] = df_selected_month_sorted.groupby(['Catégorie'])['Montant'].cumsum()


   container.dataframe(df_selected_month_sorted)

   container.line_chart(df_selected_month_sorted, x="Date", y="cumsum_sales", color="Catégorie")
   container.area_chart(df_selected_month_sorted, x="Date", y="cumsum_sales", color="Catégorie")

   # Group by 'Category' and sum the values
   grouped_data = df_selected_month_sorted.groupby('Catégorie')['Montant'].sum().reset_index()
   # Create a pie chart using Plotly Express
   fig = px.pie(grouped_data, values='Montant', names='Catégorie', title='Pie Chart with GroupBy')

   # Display the pie chart in Streamlit
   container.plotly_chart(fig, use_container_width=True)

   # Group by 'Category' and sum the values
   all_grouped_data = df.groupby(['YearMonth', 'year', 'month', 'Catégorie'])['Montant'].sum().reset_index()
   # Create a pie chart using Plotly Express
   container.dataframe(all_grouped_data)
   container.line_chart(all_grouped_data, x='YearMonth', y="Montant", color="Catégorie")
   container.area_chart(all_grouped_data, x="YearMonth", y="Montant", color="Catégorie")

   import altair as alt

   c = (
      alt.Chart(all_grouped_data)
      .mark_circle()
      .encode(x="YearMonth", y="Montant", color="Catégorie")
   )
   container.altair_chart(c, use_container_width=True)


st.title('Budget Forcast - My Machine Learning Experiment')
st.subheader('*... under construction...*')

df = data_processing()

# Create tabs
tab_titles = ['Data Preprocessing', 'EDA', 'Model Training', 'Model Evaluation', 'Results Visualization']
tabs = st.tabs(tab_titles)

# Add content to each tab
with tabs[0]:
   st.header('Data Preprocessing')
   st.write('Here we preprocess the data...')
   st.table(df)

with tabs[1]:
   st.header('EDA')
   st.write('Here we make the EDA...')
   st.write("Here's our first attempt at using data to create a table:")

eda(df, tabs[1])

with tabs[2]:
   st.header('Model Training')
   st.write('Here we train the model...')
   st.write("Here's our first attempt at using data to create a table:")

with tabs[3]:
   st.header('Model Evaluation')
   st.write('Here we evaluate the model...')

with tabs[4]:
   st.header('Results Visualization')
   st.write('Here we visualize the results...')






