import plotly.express as px
import pandas as pandas

country_df = pandas.read_csv('datasets/Country-data.csv')
fig = px.choropleth (country_df, locationmode = 'country names', locations = 'country', color = 'inflation',
                     title = "Distribution of 'GDPP' in different countries of the world"
                     , color_continuous_scale = "piyg")
fig.show()