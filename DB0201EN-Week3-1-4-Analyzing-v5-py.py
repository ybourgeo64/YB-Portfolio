#!/usr/bin/env python
# coding: utf-8

# <a href="https://cognitiveclass.ai"><img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 300, align = "center"></a>
# 
# <h1 align=center><font size = 5>Lab: Analyzing a real world data-set with SQL and Python</font></h1>

# # Introduction
# 
# This notebook shows how to store a dataset into a database using and analyze data using SQL and Python. In this lab you will:
# 1. Understand a dataset of selected socioeconomic indicators in Chicago
# 1. Learn how to store data in an Db2 database on IBM Cloud instance
# 1. Solve example problems to practice your SQL skills 

# ## Selected Socioeconomic Indicators in Chicago
# 
# The city of Chicago released a dataset of socioeconomic data to the Chicago City Portal.
# This dataset contains a selection of six socioeconomic indicators of public health significance and a “hardship index,” for each Chicago community area, for the years 2008 – 2012.
# 
# Scores on the hardship index can range from 1 to 100, with a higher index number representing a greater level of hardship.
# 
# A detailed description of the dataset can be found on [the city of Chicago's website](
# https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2), but to summarize, the dataset has the following variables:
# 
# * **Community Area Number** (`ca`): Used to uniquely identify each row of the dataset
# 
# * **Community Area Name** (`community_area_name`): The name of the region in the city of Chicago 
# 
# * **Percent of Housing Crowded** (`percent_of_housing_crowded`): Percent of occupied housing units with more than one person per room
# 
# * **Percent Households Below Poverty** (`percent_households_below_poverty`): Percent of households living below the federal poverty line
# 
# * **Percent Aged 16+ Unemployed** (`percent_aged_16_unemployed`): Percent of persons over the age of 16 years that are unemployed
# 
# * **Percent Aged 25+ without High School Diploma** (`percent_aged_25_without_high_school_diploma`): Percent of persons over the age of 25 years without a high school education
# 
# * **Percent Aged Under** 18 or Over 64:Percent of population under 18 or over 64 years of age (`percent_aged_under_18_or_over_64`): (ie. dependents)
# 
# * **Per Capita Income** (`per_capita_income_`): Community Area per capita income is estimated as the sum of tract-level aggragate incomes divided by the total population
# 
# * **Hardship Index** (`hardship_index`): Score that incorporates each of the six selected socioeconomic indicators
# 
# In this Lab, we'll take a look at the variables in the socioeconomic indicators dataset and do some basic analysis with Python.
# 

# ### Connect to the database
# Let us first load the SQL extension and establish a connection with the database

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[3]:


# Remember the connection string is of the format:
# %sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name
# Enter the connection string for your Db2 on Cloud database instance below
# i.e. copy after db2:// from the URI string in Service Credentials of your Db2 instance. Remove the double quotes at the end.
get_ipython().run_line_magic('sql', 'ibm_db_sa://lln32654:69d16lp9%5Ecw5lj4g@dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net:50000/BLUDB')


# ### Store the dataset in a Table
# ##### In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. To analyze the data using SQL, it first needs to be stored in the database.
# 
# ##### We will first read the dataset source .CSV from the internet into pandas dataframe
# 
# ##### Then we need to create a table in our Db2 database to store the dataset. The PERSIST command in SQL "magic" simplifies the process of table creation and writing the data from a `pandas` dataframe into the table

# In[4]:


import pandas
chicago_socioeconomic_data = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
get_ipython().run_line_magic('sql', 'PERSIST chicago_socioeconomic_data')


# ##### You can verify that the table creation was successful by making a basic query like:

# In[5]:


get_ipython().run_line_magic('sql', 'SELECT * FROM chicago_socioeconomic_data limit 5;')


# ## Problems
# 
# ### Problem 1
# 
# ##### How many rows are in the dataset?

# In[6]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM chicago_socioeconomic_data;')


# Double-click __here__ for the solution.
# 
# <!-- Hint:
# 
# %sql SELECT COUNT(*) FROM chicago_socioeconomic_data;
# 
# Correct answer: 78
# 
# -->

# ### Problem 2
# 
# ##### How many community areas in Chicago have a hardship index greater than 50.0?

# In[7]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM chicago_socioeconomic_data where hardship_index>50;')


# Double-click __here__ for the solution.
# 
# <!-- Hint:
# 
# %sql SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;
# Correct answer: 38
# -->
# 

# ### Problem 3
# 
# ##### What is the maximum value of hardship index in this dataset?

# In[8]:


get_ipython().run_line_magic('sql', 'SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;')


# Double-click __here__ for the solution.
# 
# <!-- Hint:
# 
# %sql SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;
# 
# Correct answer: 98.0
# -->
# 

# ### Problem 4
# 
# ##### Which community area which has the highest hardship index?
# 

# 

# In[10]:


get_ipython().run_line_magic('sql', 'SELECT community_area_name FROM chicago_socioeconomic_data where hardship_index = 98;')


# Double-click __here__ for the solution.
# 
# <!-- Hint:
# 
# ## We can use the result of the last query to as an input to this query:
# %sql SELECT community_area_name FROM chicago_socioeconomic_data where hardship_index=98.0
# 
# ## or another option:
# %sql SELECT community_area_name FROM chicago_socioeconomic_data ORDER BY hardship_index DESC NULLS LAST FETCH FIRST ROW ONLY;
# 
# ## or you can use a sub-query to determine the max hardship index:
# %sql select community_area_name from chicago_socioeconomic_data where hardship_index = ( select max(hardship_index) from chicago_socioeconomic_data ) 
# 
# Correct answer: 'Riverdale'
# -->

# ### Problem 5
# 
# ##### Which Chicago community areas have per-capita incomes greater than $60,000?

# In[11]:


get_ipython().run_line_magic('sql', 'SELECT community_area_name FROM chicago_socioeconomic_data where per_capita_income_ >60000;')


# Double-click __here__ for the solution.
# 
# <!-- Hint:
# 
# %sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;
# 
# Correct answer:Lake View,Lincoln Park, Near North Side, Loop
# -->
# 

# ### Problem 6
# 
# ##### Create a scatter plot using the variables `per_capita_income_` and `hardship_index`. Explain the correlation between the two variables.

# In[19]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
income_vs_hardship = get_ipython().run_line_magic('sql', 'SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;')
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())


# Double-click __here__ for the solution.
# 
# <!-- Hint:
# # if the import command gives ModuleNotFoundError: No module named 'seaborn'
# # then uncomment the following line i.e. delete the # to install the seaborn package 
# # !pip install seaborn
# import matplotlib.pyplot as plt
# %matplotlib inline
# import seaborn as sns
# 
# income_vs_hardship = %sql SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;
# plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())
# 
# Correct answer:You can see that as Per Capita Income rises as the Hardship Index decreases. We see that the points on the scatter plot are somewhat closer to a straight line in the negative direction, so we have a negative correlation between the two variables. 
# -->
# 

# ### Conclusion
# 
# ##### Now that you know how to do basic exploratory data analysis using SQL and python visualization tools, you can further explore this dataset to see how the variable `per_capita_income_` is related to `percent_households_below_poverty` and `percent_aged_16_unemployed`. Try to create interesting visualizations!

# ## Summary
# 
# ##### In this lab you learned how to store a real world data set from the internet in a database (Db2 on IBM Cloud), gain insights into data using SQL queries. You also visualized a portion of the data in the database to see what story it tells.

# Copyright &copy; 2018 [cognitiveclass.ai](cognitiveclass.ai?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).
# 
