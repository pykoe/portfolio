from datetime import datetime

import pandas as pd
import streamlit as st
import plotly.express as px

import altair as alt

st.write("Read a json file")


st.write("User")
data_root_path = './data/edgeryder/'
df_user = pd.read_json(data_root_path + 'userMap.json', orient='index')
st.dataframe(df_user)

st.write("Post")
df_post = pd.read_json(data_root_path + 'all_posts.json', orient='records')

df_post['created_at'] = pd.to_datetime(df_post['created_at'])
df_post['created_at_date'] = df_post['created_at'].map(lambda x: datetime(x.year, x.month, x.day))
df_post_grouped = df_post.groupby(['created_at_date'])['post_id'].count().reset_index()
st.line_chart(df_post_grouped, x='created_at_date', y="post_id")

#df_post_user_grouped = df_post.groupby(['user_id', 'username'])['post_id'].count().reset_index()
df_post_user_grouped = df_post.groupby(['user_id', 'username']).agg({
    'post_id': 'sum',
    'created_at': ['min', 'max']
}).reset_index()
df_post_user_grouped.columns = ['{}{}'.format(col[0], '' if col[1] == '' else '_' + col[1]) for col in df_post_user_grouped.columns]

print(df_post_user_grouped)
st.dataframe(df_post_user_grouped)
st.line_chart(df_post_user_grouped, x='created_at_min', y="post_id_sum")
# Create a line chart with dots using Plotly Express
st.scatter_chart(df_post_user_grouped, x='created_at_min', y='post_id_sum')
st.dataframe(df_post)


st.write("Codes")
df_codes = pd.read_json(data_root_path + 'codes.json', orient='records')
df_codes['created_at'] = pd.to_datetime(df_codes['created_at'])
df_codes['created_at_date'] = df_codes['created_at'].map(lambda x: datetime(x.year, x.month, x.day))
st.dataframe(df_codes)
df_codes_grouped = df_codes.groupby(['created_at_date'])['id'].count().reset_index()
st.line_chart(df_codes_grouped, x='created_at_date', y="id")

df_codes['updated_at'] = pd.to_datetime(df_codes['updated_at'])
df_codes['updated_at_date'] = df_codes['updated_at'].map(lambda x: datetime(x.year, x.month, x.day))
df_codes_updated_grouped = df_codes.groupby(['updated_at_date'])['id'].count().reset_index()
st.line_chart(df_codes_updated_grouped, x='updated_at_date', y="id")


st.write("Topics")
df_topic = pd.read_json(data_root_path + 'topicPostMap.json', orient='index')
st.dataframe(df_topic)

st.write("Annotation")
df_annotation = pd.read_json(data_root_path + 'annotation.json', orient='records')
df_annotation['created_at'] = pd.to_datetime(df_annotation['created_at'])
df_annotation['Date'] = df_annotation['created_at'].map(lambda x: datetime(x.year, x.month, x.day))
df_annotation_grouped = df_annotation.groupby(['Date'])['id'].count().reset_index()
st.line_chart(df_annotation_grouped, x='Date', y="id")
st.dataframe(df_annotation)
