Data Visualization of covid-19 deaths 
with plotly


Abstract :

Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data.
In the world of Big Data, data visualization tools and technologies are essential to analyze massive amounts of information and make data-driven decisions.
The advantages and benefits of good data visualization :

•	Quickens the Decision-making process
•	Easily identify hidden patterns
•	Getting business insights
•	Finding errors in beliefs
•	Storytelling about the data is more engaging
•	Helps non-technical background people understand the data better
•	Identify new trends
Human eyes are drawn to colors and patterns. We can quickly identify yellow from green, circle from a square.  the human culture is visual itself, starting from Arts and crafts, to advertisements, Tv, and movies.
Data visualization can be described as another form of art, that grabs our eyes and attention, and keeps us focused on the underlying message. While viewing a chart we can easily and quickly see upcoming or ongoing trends, outliers, etc. And this visual representation helps us digest the facts faster.
You know how much more effective data visualization can be if you’ve ever stared at a massive excel sheet, and couldn’t make out the head or tail of it.


Introduction:
Data visualization of covid-19 deaths 
A picture is worth a thousand words! Data Visualization proves this proverb correct in so many ways. It is always more impactful to see a beautiful and crisp visualization of a data set rather than reads pages and pages about that same data. And this is even more true for COVID-19. A red line steadily going upwards depicting the increasing cases of Coronavirus in a country is much more alarming and impactful rather than just reading about it. 
And so there are many universities and tech companies that are providing data visualization dashboards of COVID-19. These dashboards provide information on everything about the disease ranging from the number of confirmed cases in countries, the current death toll, the rate at which the cases are in reading, etc.

Currently, websites of the World Health Organisation, US Centers for Disease Control and Prevention, etc. provide the most accurate information about COVID-19 symptoms, prevention methods, common treatments, current statistics, etc. 
However, dynamic data visualization dashboards are much more impactful and detailed. So let’s check out some of the most accurate and impactful data visualization dashboards across the world.


 


Plotly:
    Plotly Library is an open-source library that can be used for data visualization and understanding data simply and easily. Plotly supports various types of plots like line charts, scatter plots, histograms, cox plots, etc. So you all must be wondering why Plotly over other visualization tools or libraries? Here’s the answer –
•	Plotly has hover tool capabilities that allow us to detect any outliers or anomalies in a large number of data points.
•	It is visually attractive that can be accepted by a wide range of audiences.
•	It allows us for the endless customization of our graphs that makes our plot more meaningful and understandable for others.


![image](https://user-images.githubusercontent.com/88198990/131072503-68e83e83-ea01-4919-b05a-37c2ff6a2688.png)


  
Install the important libraries
•	Pandas
•	Numpy
•	Chart_studio
•	Seaborn
•	Cufflinlks
•	Matplotlib

#import the necessary libraries

import pandas as pd
import numpy as np
import chart_studio.plotly as py
import cufflinks as cf
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
%matplotlib inline


# Make Plotly work in your Jupyter Notebook

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

# Use Plotly locally

cf.go_offline()

#loading country wise dataset

Now we will do Data Visualization of covid datasets across the world. This dataset can be found on Kaggle, 
Downloaded it.

country_wise = pd.read_csv('C:\kiran\country_wise_latest.csv')
print("Country Wise Data shape =",country_wise.shape)
country_wise.head()

 ![image](https://user-images.githubusercontent.com/88198990/131072771-f1b6049c-c5a1-4e54-b643-b14eb440a7c9.png)




country_wise.info()

![image](https://user-images.githubusercontent.com/88198990/131072679-0109a30a-ce0d-4b24-9211-82770c20fb6d.png)

 



Histogram Plot
Let us visualize total deaths from all the countries. Due to a large number of countries, I have divided them into different plots.

#deaths in first 50 countries
# Display death due to covid data for various countries 
fig = px.bar(country_wise.head(50), y='Deaths', x='Country/Region', text='Deaths', color='Country/Region')
# Put bar total value above bars with 2 values of precision
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
# Set fontsize and uniformtext_mode='hide' says to hide the text if it won't fit
fig.update_layout(uniformtext_minsize=8)
# Rotate labels 45 degrees
fig.update_layout(xaxis_tickangle=-45)
fig
 
 ![image](https://user-images.githubusercontent.com/88198990/131072806-6912313e-9e80-4790-9992-09c51fbaf080.png)


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

 ![image](https://user-images.githubusercontent.com/88198990/131073054-048bbdbc-36b8-45ae-a199-680c70c1857b.png)

 
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

 ![image](https://user-images.githubusercontent.com/88198990/131073118-818fe145-ba40-488d-807f-8e5e3f4324f0.png)

 
#deaths in the rest of countries

fig3 = px.bar(country_wise[151:], y='Deaths', x='Country/Region', text='Deaths', color='Country/Region')
# Put bar total value above bars with 2 values of precision
fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside')
# Set fontsize and uniformtext_mode='hide' says to hide the text if it won't fit
fig3.update_layout(uniformtext_minsize=8)
# Rotate labels 45 degrees
fig3.update_layout(xaxis_tickangle=-45)
fig3
  
  ![image](https://user-images.githubusercontent.com/88198990/131073152-ff1cd4b1-b83b-4ec2-a9a8-26a5519e7ca0.png)

  
#pie chart of total deaths in all asian countries
worldometer = pd.read_csv('C:\kiran\worldometer_data.csv')
worldometer_asia = worldometer[worldometer['Continent'] == 'Asia']
px.pie(worldometer_asia, values='TotalCases', names='Country/Region', 
       title='Population of Asian continent', 
       color_discrete_sequence=px.colors.sequential.RdBu)
       
   ![image](https://user-images.githubusercontent.com/88198990/131073214-bbc4ec26-6a86-45cc-b1e3-35c5ba22de95.png)


  
#the animated transition of confirmed cases from 22 Jan 2020 to July 2020

full_grouped = pd.read_csv('C:\kiran\full_grouped.csv')

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

Note: The animation could not be added to this article, but if you write the code and run it, it will play seamlessly.
 
 ![image](https://user-images.githubusercontent.com/88198990/131073393-f1de41e8-40f9-4d20-9e64-016f70b94289.png)


![image](https://user-images.githubusercontent.com/88198990/131073466-6e410cbe-1a6e-49f0-b1cf-34b3fce7b1ad.png)



The end result of the animation


Now we plot a histogram for deaths across all the Asian Countries.
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




![image](https://user-images.githubusercontent.com/88198990/131073530-9502e395-2cf0-4e86-8d01-1cea559b5bfb.png)







 
So as you can see,india had the most number of deaths, around 40-45k, which really sad.

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







 
![image](https://user-images.githubusercontent.com/88198990/131073578-2a4365ba-cace-4d84-a1f3-1b0c9f089ded.png)





	


Creating an interactive globe map
This is one of my favourite features from Plotly and another module called Pycountry. We can create an interactive Global Map, which displays all the deaths due to the Coronavirus, in different regions. I highly urge you to run this code and see how this map works.





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
 

 
![image](https://user-images.githubusercontent.com/88198990/131073706-a22ef0c9-f9ad-4b53-82c1-dbb3ec977d2c.png)



	You can rotate the globe using your cursor and view all the deaths in every country. A very tidy and neat visualization in my opinion.



End Notes
Plotly is one of my favorite goto libraries for visualization, apart from Matplotlib or Seaborn. I would like to write a blog about it someday as well.

