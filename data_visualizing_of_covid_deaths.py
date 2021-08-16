#import the necessary libraries

import pandas as pd
import numpy as np
import chart_studio.plotly as py
import cufflinks as cf
import seaborn as sns
import plotly.express
%matplotlib inline

# Make Plotly work in your Jupyter Notebook
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
# Use Plotly locally
cf.go_offline()

#loading country wise dataset

country_wise = pd.read_csv('C:\kiran/country_wise_latest.csv')
print("Country Wise Data shape =",country_wise.shape)
country_wise.head()

country_wise.info()


#deaths in first 50 countries

import plotly.graph_objects as go


# Display death due to covid data for various countries 
fig = px.bar(country_wise.head(50), y='Deaths', x='Country/Region', text='Deaths', color='Country/Region')
# Put bar total value above bars with 2 values of precision
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
# Set fontsize and uniformtext_mode='hide' says to hide the text if it won't fit
fig.update_layout(uniformtext_minsize=8)
# Rotate labels 45 degrees
fig.update_layout(xaxis_tickangle=-45)
fig


#deaths in next 50 countries

# Display death due to covid data for various countries 
fig1 = px.bar(country_wise[50:101], y='Deaths', x='Country/Region', text='Deaths', color='Country/Region')
# Put bar total value above bars with 2 values of precision
fig1.update_traces(texttemplate='%{text:.2s}', textposition='outside')
# Set fontsize and uniformtext_mode='hide' says to hide the text if it won't fit
fig1.update_layout(uniformtext_minsize=8)
# Rotate labels 45 degrees
fig1.update_layout(xaxis_tickangle=-45)
fig1


#deaths in next 50 countries

# Display death due to covid data for various countries 
fig2 = px.bar(country_wise[101:151], y='Deaths', x='Country/Region',text='Deaths', color='Country/Region')
# Put bar total value above bars with 2 values of precision
fig2.update_traces(texttemplate='%{text:.2s}', textposition='outside')
# Set fontsize and uniformtext_mode='hide' says to hide the text if it won't fit
fig2.update_layout(uniformtext_minsize=8)
# Rotate labels 45 degrees
fig2.update_layout(xaxis_tickangle=-45)
fig2


#deaths in the rest of countries

fig3 = px.bar(country_wise[151:], y='Deaths', x='Country/Region', text='Deaths', color='Country/Region')
# Put bar total value above bars with 2 values of precision
fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside')
# Set fontsize and uniformtext_mode='hide' says to hide the text if it won't fit
fig3.update_layout(uniformtext_minsize=8)
# Rotate labels 45 degrees
fig3.update_layout(xaxis_tickangle=-45)
fig3

#pie chart of total deaths in all asian countries

worldometer = pd.read_csv('C:\kiran/worldometer_data.csv')
worldometer_asia = worldometer[worldometer['Continent'] == 'Asia']


px.pie(worldometer_asia, values='TotalCases', names='Country/Region', 
       title='Population of Asian continent', 
       color_discrete_sequence=px.colors.sequential.RdBu)

#the animated transition of confirmed cases from 22 Jan 2020 to July 2020

full_grouped = pd.read_csv('C:\kiran/full_grouped.csv')

india = full_grouped[full_grouped['Country/Region'] == 'India']
us = full_grouped[full_grouped['Country/Region'] == 'US']
russia = full_grouped[full_grouped['Country/Region'] == 'Russia']
china = full_grouped[full_grouped['Country/Region'] == 'China']
df = pd.concat([india,us,russia,china], axis=0)

# Watch as bars chart covid cases changes


fig = px.bar(df, x="Country/Region", y="Confirmed", color="Country/Region",
  animation_frame="Date", animation_group="Country/Region", range_y=[0,df['Confirmed'].max() + 100000])

fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1

fig

# bins represent the number of bars to make
# Can define x label, color, title
# marginal creates another plot (violin, box, rug)

fig = px.histogram(worldometer_asia,x = 'TotalDeaths', nbins=20, 
                   labels={'value':'Total Deaths'},title='Death Distribution of Asia Continent', 
                   marginal='violin',
                   color='Country/Region')

fig.update_layout(
    xaxis_title_text='Total Deaths', showlegend=True
)


#A box plot to represent total cases distribution across Asia and Europe

# A box plot allows you to compare different variables
# The box shows the quartiles of the data. The bar in the middle is the median 
# The whiskers extend to all the other data aside from the points that are considered
# to be outliers

# Complex Styling
fig = go.Figure()
# Show all points, spread them so they don't overlap and change whisker width
fig.add_trace(go.Box(y=worldometer_asia['TotalCases'], boxpoints='all', name='Asia',
                    fillcolor='blue', jitter=0.5, whiskerwidth=0.2))
fig.add_trace(go.Box(y=worldometer[worldometer['Continent'] == 'Europe']['TotalCases'], boxpoints='all', name='Europe',
                    fillcolor='red', jitter=0.5, whiskerwidth=0.2))
# Change background / grid colors
fig.update_layout(title='Asia vs Europe total cases distribution', 
                  yaxis=dict(gridcolor='rgb(255, 255, 255)',
                 gridwidth=3),
                 paper_bgcolor='rgb(243, 243, 243)',
                 plot_bgcolor='rgb(243, 243, 243)')


#creating a interactive globe map


import pycountry

worldometer['Country/Region'].replace('USA','United States', inplace=True)
worldometer['Country/Region'].replace('UAE','United Arab Emirates', inplace=True)
worldometer['Country/Region'].replace('Ivory Coast','Côte dIvoire', inplace=True)
worldometer['Country/Region'].replace('S. Korea','Korea', inplace=True)
worldometer['Country/Region'].replace('N. Korea','Korea', inplace=True)
worldometer['Country/Region'].replace('DRC','Republic of the Congo', inplace=True)
worldometer['Country/Region'].replace('Channel Islands','Jersey', inplace=True)

exceptions = []

def get_alpha_3_code(cou):
    try:
        return pycountry.countries.search_fuzzy(cou)[0].alpha_3
    except:
        exceptions.append(cou)


worldometer['iso_alpha'] = worldometer['Country/Region'].apply(lambda x : get_alpha_3_code(x))

# removeing exceptions
for exc in exceptions:
    worldometer = worldometer[worldometer['Country/Region']!=exc]
    
    
fig = px.scatter_geo(worldometer, locations="iso_alpha",
                     color="Continent", # which column to use to set the color of markers
                     hover_name="Country/Region", # column added to hover information
                     size="TotalCases", # size of markers
                     projection="orthographic")
fig