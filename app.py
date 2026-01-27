import streamlit as st

st.title('🎯 My First Streamlit App')

st.write('Welcome to Streamlit!')

# Simple slider
age = st.slider('How old are you?', 0, 100, 25)
st.write(f'You are {age} years old')

# Simple button
if st.button('Click me'):
    st.write('Button clicked!')

# Text input
name = st.text_input('What is your name?')
st.write(f'Hello, {name}!')

# Number
age = st.number_input('Age', min_value=0, max_value=120)
st.write(f'You are {age} years old')

# Slider
budget = st.slider('Budget ($)', 0, 10000, 5000)
st.write(f'Budget: ${budget}')

# Selectbox
country = st.selectbox('Country', ['USA', 'Korea', 'UK', 'Japan'])
st.write(f'Country: {country}')

# Multiselect
interests = st.multiselect('Interests',
['Finance', 'Data Science', 'Web Dev', 'AI'])
st.write(f'Interests: {interests}')

# Sidebar
st.sidebar.header('Filters')
year_filter = st.sidebar.slider('Select Year', 2020, 2025, 2023)
category_filter = st.sidebar.selectbox('Category',
        ['All', 'A', 'B', 'C'])

# Main content with columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Total Sales', '$125K', '+12%')
with col2:
    st.metric('Orders', '1,234', '+5%')
with col3:
    st.metric('Customers', '567', '+8%')

# Two-column layout for charts
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader('Chart 1')
    st.write('Chart will go here')
with chart_col2:
    st.subheader('Chart 2')
    st.write('Another chart here')

import pandas as pd
import plotly.express as px

# Using Plotly's built-in datasets
iris = px.data.iris() # Iris flowers
tips = px.data.tips() # Restaurant tips
stocks = px.data.stocks() # Stock prices

@st.cache_data
def load_data():
    return pd.read_csv('USA Housing Dataset.csv')
df = load_data()

st.write(f'Shape: {df.shape}')
st.dataframe(df.head())
st.write(df.describe())

df = px.data.tips()

st.bar_chart(df.groupby('day')['total_bill'].sum())
st.line_chart(df.groupby('day')['tip'].mean())
st.scatter_chart(df[['total_bill', 'tip']])

df = px.data.tips()

# Interactive scatter
fig = px.scatter(df, x='total_bill', y='tip',
                    color='time', size='size')
st.plotly_chart(fig, use_container_width=True)

# Interactive bar
fig = px.bar(df.groupby('day').agg({'total_bill': 'sum'}))
st.plotly_chart(fig, use_container_width=True)

df = px.data.tips()
# Filters
selected_day = st.sidebar.multiselect('Day', df['day'].unique(),
                                default=df['day'].unique())
selected_time = st.sidebar.selectbox('Time', ['All', 'Lunch', 'Dinner'])

# Apply filters
filtered = df[df['day'].isin(selected_day)]
if selected_time != 'All':
    filtered = filtered[filtered['time'] == selected_time]

st.metric('Records', len(filtered))
fig = px.scatter(filtered, x='total_bill', y='tip', color='time')
st.plotly_chart(fig, use_container_width=True)

st.set_page_config(layout='wide')
st.title('💰 Tips Dashboard')

df = px.data.tips()

# Sidebar
selected_day = st.sidebar.multiselect('Day', df['day'].unique(),
                            default=df['day'].unique(), key="day_multiselect")
selected_time = st.sidebar.selectbox('Time', ['All', 'Lunch', 'Dinner'],key="time_selectbox")

# Apply filters
filtered = df[df['day'].isin(selected_day)]
if selected_time != 'All':
    filtered = filtered[filtered['time'] == selected_time]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric('Total Bill', f'${filtered["total_bill"].sum():.0f}')
col2.metric('Avg Tip', f'${filtered["tip"].mean():.2f}')
col3.metric('Records', len(filtered))
# Charts
col1, col2 = st.columns(2)
with col1:
    fig = px.scatter(filtered, x='total_bill', y='tip', color='time')
    st.plotly_chart(fig, use_container_width=True,key="scatter_tip")
with col2:
    fig = px.box(filtered, x='day', y='total_bill', color='time')
    st.plotly_chart(fig, use_container_width=True, key="box_bill")

    df = px.data.tips()

# Multiple filters
days = st.sidebar.multiselect('Day', df['day'].unique(),
            default=df['day'].unique(),
    key='day_filter')
bill_range = st.sidebar.slider('Bill Range ($)',
            float(df['total_bill'].min()),
            float(df['total_bill'].max()))

# Apply all filters
filtered = df[(df['day'].isin(days)) &
                (df['total_bill'] <= bill_range)]

st.metric('Records', len(filtered))
fig = px.scatter(filtered, x='total_bill', y='tip', color='day')
st.plotly_chart(fig, use_container_width=True)

df = pd.read_csv('USA Housing Dataset.csv')
st.title('🏠 House Price Dashboard')

# Filters
price_range = st.sidebar.slider('Price Range ($)',
            int(df['price'].min()),
            int(df['price'].max()))
bedrooms = st.sidebar.slider('Min Bedrooms', 1, 10, 3)

# Apply
filtered = df[(df['price'] <= price_range) &
            (df['bedrooms'] >= bedrooms)]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric('Avg Price', f'${filtered["price"].mean():.0f}')
col2.metric('Count', len(filtered))
col3.metric('Avg Bedrooms', f'{filtered["bedrooms"].mean():.1f}')

# Charts
fig1 = px.scatter(filtered, x='sqft_living', y='price', color='bedrooms')
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.histogram(filtered, x='price', nbins=30)
st.plotly_chart(fig2, use_container_width=True)

@st.cache_data
def load_data():
    return pd.read_csv('USA Housing Dataset.csv')

data = load_data()

filter1 = st.sidebar.selectbox(
    'Pick price',
    data['price'].unique(),
    key='price_pick'
)

filtered = data[data['price'] == filter1]

col1, col2 = st.columns(2)

col1.metric(
    'Records',
    len(filtered)
)

col2.metric(
    'Avg Price',
    f"{filtered['price'].mean():,.0f}"
)
