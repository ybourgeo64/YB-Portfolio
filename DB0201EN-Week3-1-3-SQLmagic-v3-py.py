#!/usr/bin/env python
# coding: utf-8

# <a href="https://www.bigdatauniversity.com"><img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 300, align = "center"></a>
# 
# <h1 align=center><font size = 5>Accessing Databases with SQL Magic</font></h1>

# #### After using this notebook, you will know how to perform simplified database access using SQL "magic". You will connect to a Db2 database, issue SQL commands to create tables, insert data, and run queries, as well as retrieve results in a Python dataframe. 

# ##### To communicate with SQL Databases from within a JupyterLab notebook, we can use the SQL "magic" provided by the [ipython-sql](https://github.com/catherinedevlin/ipython-sql) extension. "Magic" is JupyterLab's term for special commands that start with "%". Below, we'll use the _load_\__ext_ magic to load the ipython-sql extension. In the lab environemnt provided in the course the ipython-sql extension is already installed and so is the ibm_db_sa driver. 

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')


# ##### Now we have access to SQL magic. With our first SQL magic command, we'll connect to a Db2 database. However, in order to do that, you'll first need to retrieve or create your credentials to access your Db2 database.

# <a ><img src = "https://ibm.box.com/shared/static/uy78gy1uq3uj6fkvd4muzy5zcr62tb72.png" width = 1000, align = "center"></a>
#   <h5 align=center>  This image shows the location of your connection string if you're using Db2 on IBM Cloud. If you're using another host the format is: username:password@hostname:port/database-name
#   </h5>

# In[2]:


# Enter your Db2 credentials in the connection string below
# Recall you created Service Credentials in Part III of the first lab of the course in Week 1
# i.e. from the uri field in the Service Credentials copy everything after db2:// (but remove the double quote at the end)
# for example, if your credentials are as in the screenshot above, you would write:
# %sql ibm_db_sa://my-username:my-password@dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net:50000/BLUDB
# Note the ibm_db_sa:// prefix instead of db2://
# This is because JupyterLab's ipython-sql extension uses sqlalchemy (a python SQL toolkit)
# which in turn uses IBM's sqlalchemy dialect: ibm_db_sa
get_ipython().run_line_magic('sql', 'ibm_db_sa://lln32654:69d16lp9%5Ecw5lj4g@dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net:50000/BLUDB')


# ##### For convenience, we can use %%sql (two %'s instead of one) at the top of a cell to indicate we want the entire cell to be treated as SQL. Let's use this to create a table and fill it with some test data for experimenting.

# In[3]:


get_ipython().run_cell_magic('sql', '', "\nCREATE TABLE INTERNATIONAL_STUDENT_TEST_SCORES (\n\tcountry VARCHAR(50),\n\tfirst_name VARCHAR(50),\n\tlast_name VARCHAR(50),\n\ttest_score INT\n);\nINSERT INTO INTERNATIONAL_STUDENT_TEST_SCORES (country, first_name, last_name, test_score)\nVALUES\n('United States', 'Marshall', 'Bernadot', 54),\n('Ghana', 'Celinda', 'Malkin', 51),\n('Ukraine', 'Guillermo', 'Furze', 53),\n('Greece', 'Aharon', 'Tunnow', 48),\n('Russia', 'Bail', 'Goodwin', 46),\n('Poland', 'Cole', 'Winteringham', 49),\n('Sweden', 'Emlyn', 'Erricker', 55),\n('Russia', 'Cathee', 'Sivewright', 49),\n('China', 'Barny', 'Ingerson', 57),\n('Uganda', 'Sharla', 'Papaccio', 55),\n('China', 'Stella', 'Youens', 51),\n('Poland', 'Julio', 'Buesden', 48),\n('United States', 'Tiffie', 'Cosely', 58),\n('Poland', 'Auroora', 'Stiffell', 45),\n('China', 'Clarita', 'Huet', 52),\n('Poland', 'Shannon', 'Goulden', 45),\n('Philippines', 'Emylee', 'Privost', 50),\n('France', 'Madelina', 'Burk', 49),\n('China', 'Saunderson', 'Root', 58),\n('Indonesia', 'Bo', 'Waring', 55),\n('China', 'Hollis', 'Domotor', 45),\n('Russia', 'Robbie', 'Collip', 46),\n('Philippines', 'Davon', 'Donisi', 46),\n('China', 'Cristabel', 'Radeliffe', 48),\n('China', 'Wallis', 'Bartleet', 58),\n('Moldova', 'Arleen', 'Stailey', 38),\n('Ireland', 'Mendel', 'Grumble', 58),\n('China', 'Sallyann', 'Exley', 51),\n('Mexico', 'Kain', 'Swaite', 46),\n('Indonesia', 'Alonso', 'Bulteel', 45),\n('Armenia', 'Anatol', 'Tankus', 51),\n('Indonesia', 'Coralyn', 'Dawkins', 48),\n('China', 'Deanne', 'Edwinson', 45),\n('China', 'Georgiana', 'Epple', 51),\n('Portugal', 'Bartlet', 'Breese', 56),\n('Azerbaijan', 'Idalina', 'Lukash', 50),\n('France', 'Livvie', 'Flory', 54),\n('Malaysia', 'Nonie', 'Borit', 48),\n('Indonesia', 'Clio', 'Mugg', 47),\n('Brazil', 'Westley', 'Measor', 48),\n('Philippines', 'Katrinka', 'Sibbert', 51),\n('Poland', 'Valentia', 'Mounch', 50),\n('Norway', 'Sheilah', 'Hedditch', 53),\n('Papua New Guinea', 'Itch', 'Jubb', 50),\n('Latvia', 'Stesha', 'Garnson', 53),\n('Canada', 'Cristionna', 'Wadmore', 46),\n('China', 'Lianna', 'Gatward', 43),\n('Guatemala', 'Tanney', 'Vials', 48),\n('France', 'Alma', 'Zavittieri', 44),\n('China', 'Alvira', 'Tamas', 50),\n('United States', 'Shanon', 'Peres', 45),\n('Sweden', 'Maisey', 'Lynas', 53),\n('Indonesia', 'Kip', 'Hothersall', 46),\n('China', 'Cash', 'Landis', 48),\n('Panama', 'Kennith', 'Digance', 45),\n('China', 'Ulberto', 'Riggeard', 48),\n('Switzerland', 'Judy', 'Gilligan', 49),\n('Philippines', 'Tod', 'Trevaskus', 52),\n('Brazil', 'Herold', 'Heggs', 44),\n('Latvia', 'Verney', 'Note', 50),\n('Poland', 'Temp', 'Ribey', 50),\n('China', 'Conroy', 'Egdal', 48),\n('Japan', 'Gabie', 'Alessandone', 47),\n('Ukraine', 'Devlen', 'Chaperlin', 54),\n('France', 'Babbette', 'Turner', 51),\n('Czech Republic', 'Virgil', 'Scotney', 52),\n('Tajikistan', 'Zorina', 'Bedow', 49),\n('China', 'Aidan', 'Rudeyeard', 50),\n('Ireland', 'Saunder', 'MacLice', 48),\n('France', 'Waly', 'Brunstan', 53),\n('China', 'Gisele', 'Enns', 52),\n('Peru', 'Mina', 'Winchester', 48),\n('Japan', 'Torie', 'MacShirrie', 50),\n('Russia', 'Benjamen', 'Kenford', 51),\n('China', 'Etan', 'Burn', 53),\n('Russia', 'Merralee', 'Chaperlin', 38),\n('Indonesia', 'Lanny', 'Malam', 49),\n('Canada', 'Wilhelm', 'Deeprose', 54),\n('Czech Republic', 'Lari', 'Hillhouse', 48),\n('China', 'Ossie', 'Woodley', 52),\n('Macedonia', 'April', 'Tyer', 50),\n('Vietnam', 'Madelon', 'Dansey', 53),\n('Ukraine', 'Korella', 'McNamee', 52),\n('Jamaica', 'Linnea', 'Cannam', 43),\n('China', 'Mart', 'Coling', 52),\n('Indonesia', 'Marna', 'Causbey', 47),\n('China', 'Berni', 'Daintier', 55),\n('Poland', 'Cynthia', 'Hassell', 49),\n('Canada', 'Carma', 'Schule', 49),\n('Indonesia', 'Malia', 'Blight', 48),\n('China', 'Paulo', 'Seivertsen', 47),\n('Niger', 'Kaylee', 'Hearley', 54),\n('Japan', 'Maure', 'Jandak', 46),\n('Argentina', 'Foss', 'Feavers', 45),\n('Venezuela', 'Ron', 'Leggitt', 60),\n('Russia', 'Flint', 'Gokes', 40),\n('China', 'Linet', 'Conelly', 52),\n('Philippines', 'Nikolas', 'Birtwell', 57),\n('Australia', 'Eduard', 'Leipelt', 53)")


# #### Using Python Variables in your SQL Statements
# ##### You can use python variables in your SQL statements by adding a ":" prefix to your python variable names.
# ##### For example, if I have a python variable `country` with a value of `"Canada"`, I can use this variable in a SQL query to find all the rows of students from Canada.

# In[4]:


country = "Canada"
get_ipython().run_line_magic('sql', 'select * from INTERNATIONAL_STUDENT_TEST_SCORES where country = :country')


# #### Assigning the Results of Queries to Python Variables

# ##### You can use the normal python assignment syntax to assign the results of your queries to python variables.
# ##### For example, I have a SQL query to retrieve the distribution of test scores (i.e. how many students got each score). I can assign the result of this query to the variable `test_score_distribution` using the `=` operator.

# In[5]:


test_score_distribution = get_ipython().run_line_magic('sql', 'SELECT test_score as "Test Score", count(*) as "Frequency" from INTERNATIONAL_STUDENT_TEST_SCORES GROUP BY test_score;')
test_score_distribution


# #### Converting Query Results to DataFrames

# ##### You can easily convert a SQL query result to a pandas dataframe using the `DataFrame()` method. Dataframe objects are much more versatile than SQL query result objects. For example, we can easily graph our test score distribution after converting to a dataframe.

# In[6]:


dataframe = test_score_distribution.DataFrame()

get_ipython().run_line_magic('matplotlib', 'inline')
# uncomment the following line if you get an module error saying seaborn not found
# !pip install seaborn
import seaborn

plot = seaborn.barplot(x='Test Score',y='Frequency', data=dataframe)


# Now you know how to work with Db2 from within JupyterLab notebooks using SQL "magic"!

# In[22]:


get_ipython().run_cell_magic('sql', '', '\n-- Feel free to experiment with the data set provided in this notebook for practice:\nSELECT country, first_name, last_name, test_score FROM INTERNATIONAL_STUDENT_TEST_SCORES WHERE test_score>=54 ORDER BY COUNTRY ASC;    ')


# Copyright &copy; 2018 [cognitiveclass.ai](cognitiveclass.ai?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).
# 
