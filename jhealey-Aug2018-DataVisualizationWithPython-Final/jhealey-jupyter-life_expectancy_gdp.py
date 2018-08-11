
# coding: utf-8

# # Introduction
# 
# For this project, you will act as a data researcher for the World Health Organization. You will investigate if there is a strong correlation between the economic output of a country and the life expectancy of its citizens.  
# 
# During this project, you will analyze, prepare, and plot data, and seek to answer questions in a meaningful way.
# 
# After you perform analysis, you'll be creating an article with your visualizations to be featured in the fictional "Time Magazine".
# 
# **Focusing Questions**: 
# + Has life expectancy increased over time in the six nations?
# + Has GDP increased over time in the six nations?
# + Is there a correlation between GDP and life expectancy of a country?
# + What is the average life expactancy in these nations?
# + What is the distribution of that life expectancy?
# 
# GDP Source:[World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)national accounts data, and OECD National Accounts data files.
# 
# Life expectancy Data Source: [World Health Organization](http://apps.who.int/gho/data/node.main.688)
# 

# ## Step 1. Import Python Modules

# Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# ## Step 2 Prep The Data

# To look for connections between GDP and life expectancy you will need to load the datasets into DataFrames so that they can be visualized.
# 
# Load **all_data.csv** into a DataFrame called `df`. Then, quickly inspect the DataFrame using `.head()`.
# 
# Hint: Use `pd.read_csv()`
# 

# In[2]:


df = pd.read_csv("all_data.csv")
df.head()


# ## Step 3 Examine The Data

# The datasets are large and it may be easier to view the entire dataset locally on your computer. You can open the CSV files directly from the folder you downloaded for this project.
# 
# Let's learn more about our data:
# - GDP stands for **G**ross **D**omestic **P**roduct. GDP is a monetary measure of the market value of all final goods and services produced in a time period. 
# - The GDP values are in current US dollars.

# What six countries are represented in the data?

# In[3]:


# countries: 6, Chile, China, Germany, Mexico, United States of America, Zimbabwe
data_countries=["Chile","China","Germany","Mexico","United States of America","Zimbabwe"]


# What years are represented in the data?

# In[4]:


# years: 16, 2000-2015
data_years=["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]


# ## Step 4 Tweak The DataFrame
# 
# Look at the column names of the DataFrame `df` using `.head()`. 

# In[5]:


df.head()


# What do you notice? The first two column names are one word each, and the third is five words long! `Life expectancy at birth (years)` is descriptive, which will be good for labeling the axis, but a little difficult to wrangle for coding the plot itself. 
# 
# **Revise The DataFrame Part A:** 
# 
# Use Pandas to change the name of the last column to `LEABY`.
# 
# Hint: Use `.rename()`. [You can read the documentation here.](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)). </font>

# In[6]:


df=df.rename(index=str,columns={"Life expectancy at birth (years)": "LEABY"})


# Run `df.head()` again to check your new column name worked.

# In[7]:


df.head()


# ---

# ## Step 5 Bar Charts To Compare Average

# To take a first high level look at both datasets, create a bar chart for each DataFrame:
# 
# A) Create a bar chart from the data in `df` using `Country` on the x-axis and `GDP` on the y-axis. 
# Remember to `plt.show()` your chart!

# In[8]:


#sns.barplot(data=df, x='Country', y='GDP')
# no, bar chart, not bar plot.
plt.bar(df.Country,df.GDP)
plt.show()


 


# B) Create a bar chart using the data in `df` with `Country` on the x-axis and `LEABY` on the y-axis.
# Remember to `plt.show()` your chart!

# In[9]:


plt.bar(df.Country,df.LEABY)
plt.show()


# What do you notice about the two bar charts? Do they look similar?

# In[10]:


# These charts do not look similar.  
# The Life Expectancy at Birth (in Years) 
# does not seem to directly correlate with GDP, within country.
# Zimbabwe is the lowest in both values, though.


# ## Step 6. Violin Plots To Compare Life Expectancy Distributions 

# Another way to compare two datasets is to visualize the distributions of each and to look for patterns in the shapes.
# 
# We have added the code to instantiate a figure with the correct dimmensions to observe detail. 
# 1. Create an `sns.violinplot()` for the dataframe `df` and map `Country` and `LEABY` as its respective `x` and `y` axes. 
# 2. Be sure to show your plot

# In[11]:


fig = plt.subplots(figsize=(15, 10)) 

sns.set_style("darkgrid")
sns.set_palette("pastel")
sns.violinplot(data=df, x="Country", y="LEABY")
plt.title("Life Expectancy by Country - Violin Plot")
plt.savefig("violinLEABY.png")
plt.show()


# What do you notice about this distribution? Which country's life expactancy has changed the most?

#  

# ## Step 7. Bar Plots Of GDP and Life Expectancy over time
# 
# We want to compare the GDPs of the countries over time, in order to get a sense of the relationship between GDP and life expectancy. 
# 
# First, can plot the progession of GDP's over the years by country in a barplot using Seaborn.
# We have set up a figure with the correct dimensions for your plot. Under that declaration:
# 1. Save `sns.barplot()` to a variable named `ax`
# 2. Chart `Country` on the x axis, and `GDP` on the `Y` axis on the barplot. Hint: `ax = sns.barplot(x="Country", y="GDP")`
# 3. Use the `Year` as a `hue` to differentiate the 15 years in our data. Hint: `ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)`
# 4. Since the names of the countries are long, let's rotate their label by 90 degrees so that they are legible. Use `plt.xticks("rotation=90")`
# 5. Since our GDP is in trillions of US dollars, make sure your Y label reflects that by changing it to `"GDP in Trillions of U.S. Dollars"`. Hint: `plt.ylabel("GDP in Trillions of U.S. Dollars")`
# 6. Be sure to show your plot.
# 

# In[12]:


f, ax = plt.subplots(figsize=(10, 15)) 
ax = sns.barplot(data=df, x='Country', y='GDP',hue="Year")
# change the following from the -hint- above as its incorrectly quoted.
plt.xticks(rotation="90")
plt.ylabel("GDP in Trillions of U.S. Dollars")
plt.show()


# Now that we have plotted a barplot that clusters GDP over time by Country, let's do the same for Life Expectancy.
# 
# The code will essentially be the same as above! The beauty of Seaborn relies in its flexibility and extensibility. Paste the code from above in the cell bellow, and: 
# 1. Change your `y` value to `LEABY` in order to plot life expectancy instead of GDP. Hint: `ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)`
# 2. Tweak the name of your `ylabel` to reflect this change, by making the label `"Life expectancy at birth in years"` Hint: `ax.set(ylabel="Life expectancy at birth in years")`
# 

# In[13]:


f, ax = plt.subplots(figsize=(10, 15)) 
ax = sns.barplot(data=df, x='Country', y='LEABY',hue="Year")
# change the following from the -hint- above as its incorrectly quoted.
plt.xticks(rotation="90")
plt.ylabel("Life expectancy at birth in years")
# didnt use hint as we'd just done this in the last graph
# for completeness, hint was: ax.set(ylabel="Life expectancy at birth in years")
plt.show()


# What are your first impressions looking at the visualized data?
# 
# - Which countries' bars changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in GDP over time? 
# - How do countries compare to one another?
# - Now that you can see the both bar charts, what do you think about the relationship between GDP and life expectancy?
# - Can you think of any reasons that the data looks like this for particular countries?

# In[14]:


##Which countries' bars changes the most?
# Zimbabwe
##What years are there the biggest changes in the data?
# For Zimbabwe, 2008, 2009 and 2010.
##Which country has had the least change in GDP over time?
# Zimbabwe
##How do countries compare to one another?
# The Life Expectancy by the Countries included within this comparison is not very different.  The GDP is dramatically different.  All countries’ life expectancies have improved over this 16 year period.
##Now that you can see the both bar charts, what do you think about the relationship between GDP and life expectancy?
# GDP and Life Expectancy do not seem to be correlated at all, never mind strongly, except at very low levels of GDP.  This may be tied more strongly to other factors not included in this measurement, like health care.      
##Can you think of any reasons that the data looks like this for particular countries?
# GDP is self explanatory:  the products produced and services offered by the countries add up to a lot of wealth for some and not so much for others.  The Life Expectancy chart at the high end does not follow along with GDP, but at the low end, Zimbabwe in particular, has a much lower life expectancy than the other countries, including Chile, whose GDP is also poor, though nowhere near as poor as Zimbabwe’s.  Other factors, like health care, war, or social challenges, may play a larger factor here than GDP.


# Note: You've mapped two bar plots showcasing a variable over time by country, however, bar charts are not traditionally used for this purpose. In fact, a great way to visualize a variable over time is by using a line plot. While the bar charts tell us some information, the data would be better illustrated on a line plot.  We will complete this in steps 9 and 10, for now let's switch gears and create another type of chart.

# ## Step 8. Scatter Plots of GDP and Life Expectancy Data

# To create a visualization that will make it easier to see the possible correlation between GDP and life expectancy, you can plot each set of data on its own subplot, on a shared figure.
# 
# To create multiple plots for comparison, Seaborn has a special (function)[https://seaborn.pydata.org/generated/seaborn.FacetGrid.html] called `FacetGrid`. A FacetGrid takes in a function and creates an individual graph for which you specify the arguments!
#     
# Since this may be the first time you've learned about FacetGrid, we have prepped a fill in the blank code snippet below. 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want GDP on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up for every Year in the data
# 3. We want the data points to be differentiated (hue) by Country.
# 4. We want to use a Matplotlib scatter plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 

# In[15]:


# WORDBANK:
# "Year"
# "Country" 
# "GDP" 
# "LEABY" 
# plt.scatter


# Uncomment the code below and fill in the blanks
# note that like FacetGrid, matplotlib scatter plots were not part of the lessons prior to this point
g = sns.FacetGrid(df, col="Year", hue="Country", col_wrap=4, size=2)
g = (g.map(plt.scatter, "GDP", "LEABY", edgecolor="w").add_legend())
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("GDP vs LEABY by Country per Year - Scatter Plot", x=0.4, fontsize=14)
plt.savefig("FacetGDPLeabyScatter.png")


# + Which country moves the most along the X axis over the years?
# + Which country moves the most along the Y axis over the years?
# + Is this surprising?
# + Do you think these scatter plots are easy to read? Maybe there's a way to plot that! 

# In[16]:


##Which country moves the most along the X axis over the years?  
# China, with the largest GDP growth.
##Which country moves the most along the Y axis over the years?
# Zimbabwe, with the most improved life expectancy.
##Is this surprising?
# Not based on the prior graphs, nor with the knowledge that China has become a major world player in the last twenty years after a long period of isolationism.  
# I didn’t know much about Zimbabwe’s Life Expectancy plight prior to this data, and I’m happy to see that it’s far closer to the rest of the countries than it was.
##Do you think these scatter plots are easy to read? Maybe there's a way to plot that!
# I can read the plots, but I don’t think they show growth over time well with the data split. 


# ## Step 9. Line Plots for Life Expectancy

# In the scatter plot grid above, it was hard to isolate the change for GDP and Life expectancy over time. 
# It would be better illustrated with a line graph for each GDP and Life Expectancy by country. 
# 
# FacetGrid also allows you to do that! Instead of passing in `plt.scatter` as your Matplotlib function, you would have to pass in `plt.plot` to see a line graph. A few other things have to change as well. So we have created a different codesnippets with fill in the blanks.  that makes use of a line chart, and we will make two seperate FacetGrids for both GDP and Life Expectancy separately.
# 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want Years on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up by Country
# 3. We want to use a Matplotlib line plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 
# 

# In[17]:


# WORDBANK:
# plt.plot
# "LEABY"
# "Year"
# "Country"


# Uncomment the code below and fill in the blanks
g3 = sns.FacetGrid(df, col="Country", col_wrap=3, size=4)
g3 = (g3.map(plt.plot, "Year", "LEABY").add_legend())
g3.fig.subplots_adjust(top=0.9)
g3.fig.suptitle("LEABY by Year per Country - Line Plot", x=0.5, fontsize=14)
plt.savefig("FacetLEABYline.png")


# What are your first impressions looking at the visualized data?
# 
# - Which countries' line changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in life expectancy over time? 
# - Can you think of any reasons that the data looks like this for particular countries?

#  

# ## Step 10. Line Plots for GDP

# Let's recreate the same FacetGrid for GDP now. Instead of Life Expectancy on the Y axis, we now we want GDP.
# 
# Once you complete and successfully run the code above, copy and paste it into the cell below. Change the variable for the X axis. Change the color on your own! Be sure to show your plot.
# 

# In[18]:


# WORDBANK:
# plt.plot
# "LEABY"
# "Year"
# "Country"


# Uncomment the code below and fill in the blanks
g3 = sns.FacetGrid(df, col="Country", col_wrap=3, size=4)
g3 = (g3.map(plt.plot, "Year", "GDP").add_legend())
g3.fig.subplots_adjust(top=0.9)
g3.fig.suptitle("GDP by Year per Country - Line Plot", x=0.5, fontsize=14)
plt.savefig("FacetGDPline.png")


# Which countries have the highest and lowest GDP?

# In[19]:


# The US has the highest.  Zimbabwe has the lowest.


# Which countries have the highest and lowest life expectancy?

# In[20]:


# Germany is the highest life expectancy.  Zimbabwe is the lowest.


# ## Step 11 Researching Data Context 

# Based on the visualization, choose one part the data to research a little further so you can add some real world context to the visualization. You can choose anything you like, or use the example question below.
# 
# What happened in China between in the past 10 years that increased the GDP so drastically?

# In[21]:


# The average Chinese person is more than twice as well off now as they were in 2006.
# That’s according to the World Bank’s measure of national income per person, adjusted for purchasing power parity – a metric that seeks to allow meaningful comparisons across countries and time periods by looking at what dollar amounts can actually buy.
# In 2006, industry’s contribution to GDP was about 13% higher than that of services. In the latest breakdown, from two years ago, services contributed about 13% more than industry.
# Likewise, a decade ago many analysts expected China to become gradually less reliant on its export-led model of growth – and that path has been taken. In 2006, China’s exports amounted to 35% of its GDP; by 2014, that had fallen to 23%.
# Imports, meanwhile, dropped from 29% of GDP to 19% in the same period, indicating that China has become significantly more self-sufficient.
# The percentage of children dying before their fifth birthday halved from 2.19 in 2006 to 1.07 in 2015. In the same period, the percentage of Chinese who still lack access to improved sanitation dropped from 34% to 24%.
# In 2006, only 68% of secondary-aged children enrolled in secondary school. Within seven years, that had leapt to 96%. The percentage enrolling in tertiary education jumped from 20% to 30% in the same period.
#ref: https://www.weforum.org/agenda/2016/06/how-has-china-s-economy-changed-in-the-last-10-years/
#ref: https://en.wikipedia.org/wiki/Economic_history_of_China_(1949%E2%80%93present)


# ## Step 12 Create Blog Post

# Use the content you have created in this Jupyter notebook to create a blog post reflecting on this data.
# Include the following visuals in your blogpost:
# 
# 1. The violin plot of the life expectancy distribution by country
# 2. The facet grid of scatter graphs mapping GDP as a function Life Expectancy by country
# 3. The facet grid of line graphs mapping GDP by country
# 4. The facet grid of line graphs mapping Life Expectancy by country
# 
# 
# We encourage you to spend some time customizing the color and style of your plots! Remember to use `plt.savefig("filename.png")` to save your figures as a `.png` file.
# 
# When authoring your blog post, here are a few guiding questions to guide your research and writing:
# + How do you think the histories and the cultural values of each country relate to its GDP and life expectancy?
# + What would have helped make the project data more reliable? What were the limitations of the dataset?
# + Which graphs better illustrate different relationships??
