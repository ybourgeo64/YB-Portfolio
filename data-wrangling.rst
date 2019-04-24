
.. raw:: html

   <div class="alert alert-block alert-info" style="margin-top: 20px">

::

    <a href="https://cocl.us/corsera_da0101en_notebook_top">
         <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/Images/TopAd.png" width="750" align="center">
    </a>

.. raw:: html

   </div>

.. raw:: html

   <h1 align="center">

Data Analysis with Python

.. raw:: html

   </h1>

.. raw:: html

   <h1>

Data Wrangling

.. raw:: html

   </h1>

.. raw:: html

   <h3>

Welcome!

.. raw:: html

   </h3>

By the end of this notebook, you will have learned the basics of Data
Wrangling!

.. raw:: html

   <h2>

Table of content

.. raw:: html

   </h2>

.. raw:: html

   <div class="alert alert-block alert-info" style="margin-top: 20px">

.. raw:: html

   <ul>

::

    <li><a href="#identify_handle_missing_values">Identify and handle missing values</a>
        <ul>
            <li><a href="#identify_missing_values">Identify missing values</a></li>
            <li><a href="#deal_missing_values">Deal with missing values</a></li>
            <li><a href="#correct_data_format">Correct data format</a></li>
        </ul>
    </li>
    <li><a href="#data_standardization">Data standardization</a></li>
    <li><a href="#data_normalization">Data Normalization (centering/scaling)</a></li>
    <li><a href="#binning">Binning</a></li>
    <li><a href="#indicator">Indicator variable</a></li>

.. raw:: html

   </ul>

Estimated Time Needed: 30 min

.. raw:: html

   </div>

.. raw:: html

   <hr>

.. raw:: html

   <h2>

What is the purpose of Data Wrangling?

.. raw:: html

   </h2>

Data Wrangling is the process of converting data from the initial format
to a format that may be better for analysis.

.. raw:: html

   <h3>

What is the fuel consumption (L/100k) rate for the diesel car?

.. raw:: html

   </h3>

.. raw:: html

   <h3>

Import data

.. raw:: html

   </h3>

.. raw:: html

   <p>

You can find the "Automobile Data Set" from the following link:
https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data.
We will be using this data set throughout this course.

.. raw:: html

   </p>

.. raw:: html

   <h4>

Import pandas

.. raw:: html

   </h4>

.. code:: ipython3

    import pandas as pd
    import matplotlib.pylab as plt

.. raw:: html

   <h2>

Reading the data set from the URL and adding the related headers.

.. raw:: html

   </h2>

URL of the dataset

This dataset was hosted on IBM Cloud object click HERE for free storage

.. code:: ipython3

    filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"

Python list headers containing name of headers

.. code:: ipython3

    headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
             "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
             "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
             "peak-rpm","city-mpg","highway-mpg","price"]

Use the Pandas method read\_csv() to load the data from the web address.
Set the parameter "names" equal to the Python list "headers".

.. code:: ipython3

    df = pd.read_csv(filename, names = headers)

Use the method head() to display the first five rows of the dataframe.

.. code:: ipython3

    # To see what the data set looks like, we'll use the head() method.
    df.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>symboling</th>
          <th>normalized-losses</th>
          <th>make</th>
          <th>fuel-type</th>
          <th>aspiration</th>
          <th>num-of-doors</th>
          <th>body-style</th>
          <th>drive-wheels</th>
          <th>engine-location</th>
          <th>wheel-base</th>
          <th>...</th>
          <th>engine-size</th>
          <th>fuel-system</th>
          <th>bore</th>
          <th>stroke</th>
          <th>compression-ratio</th>
          <th>horsepower</th>
          <th>peak-rpm</th>
          <th>city-mpg</th>
          <th>highway-mpg</th>
          <th>price</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>3</td>
          <td>?</td>
          <td>alfa-romero</td>
          <td>gas</td>
          <td>std</td>
          <td>two</td>
          <td>convertible</td>
          <td>rwd</td>
          <td>front</td>
          <td>88.6</td>
          <td>...</td>
          <td>130</td>
          <td>mpfi</td>
          <td>3.47</td>
          <td>2.68</td>
          <td>9.0</td>
          <td>111</td>
          <td>5000</td>
          <td>21</td>
          <td>27</td>
          <td>13495</td>
        </tr>
        <tr>
          <th>1</th>
          <td>3</td>
          <td>?</td>
          <td>alfa-romero</td>
          <td>gas</td>
          <td>std</td>
          <td>two</td>
          <td>convertible</td>
          <td>rwd</td>
          <td>front</td>
          <td>88.6</td>
          <td>...</td>
          <td>130</td>
          <td>mpfi</td>
          <td>3.47</td>
          <td>2.68</td>
          <td>9.0</td>
          <td>111</td>
          <td>5000</td>
          <td>21</td>
          <td>27</td>
          <td>16500</td>
        </tr>
        <tr>
          <th>2</th>
          <td>1</td>
          <td>?</td>
          <td>alfa-romero</td>
          <td>gas</td>
          <td>std</td>
          <td>two</td>
          <td>hatchback</td>
          <td>rwd</td>
          <td>front</td>
          <td>94.5</td>
          <td>...</td>
          <td>152</td>
          <td>mpfi</td>
          <td>2.68</td>
          <td>3.47</td>
          <td>9.0</td>
          <td>154</td>
          <td>5000</td>
          <td>19</td>
          <td>26</td>
          <td>16500</td>
        </tr>
        <tr>
          <th>3</th>
          <td>2</td>
          <td>164</td>
          <td>audi</td>
          <td>gas</td>
          <td>std</td>
          <td>four</td>
          <td>sedan</td>
          <td>fwd</td>
          <td>front</td>
          <td>99.8</td>
          <td>...</td>
          <td>109</td>
          <td>mpfi</td>
          <td>3.19</td>
          <td>3.40</td>
          <td>10.0</td>
          <td>102</td>
          <td>5500</td>
          <td>24</td>
          <td>30</td>
          <td>13950</td>
        </tr>
        <tr>
          <th>4</th>
          <td>2</td>
          <td>164</td>
          <td>audi</td>
          <td>gas</td>
          <td>std</td>
          <td>four</td>
          <td>sedan</td>
          <td>4wd</td>
          <td>front</td>
          <td>99.4</td>
          <td>...</td>
          <td>136</td>
          <td>mpfi</td>
          <td>3.19</td>
          <td>3.40</td>
          <td>8.0</td>
          <td>115</td>
          <td>5500</td>
          <td>18</td>
          <td>22</td>
          <td>17450</td>
        </tr>
      </tbody>
    </table>
    <p>5 rows × 26 columns</p>
    </div>



As we can see, several question marks appeared in the dataframe; those
are missing values which may hinder our further analysis.

.. raw:: html

   <div>

So, how do we identify all those missing values and deal with them?

.. raw:: html

   </div>

How to work with missing data?

Steps for working with missing data:

.. raw:: html

   <ol>

::

    <li>dentify missing data</li>
    <li>deal with missing data</li>
    <li>correct data format</li>

.. raw:: html

   </ol>

.. raw:: html

   <h2 id="identify_handle_missing_values">

Identify and handle missing values

.. raw:: html

   </h2>

.. raw:: html

   <h3 id="identify_missing_values">

Identify missing values

.. raw:: html

   </h3>

.. raw:: html

   <h4>

Convert "?" to NaN

.. raw:: html

   </h4>

In the car dataset, missing data comes with the question mark "?". We
replace "?" with NaN (Not a Number), which is Python's default missing
value marker, for reasons of computational speed and convenience. Here
we use the function:

.. raw:: html

   <pre>.replace(A, B, inplace = True) </pre>

to replace A by B

.. code:: ipython3

    import numpy as np
    
    # replace "?" to NaN
    df.replace("?", np.nan, inplace = True)
    df.head(5)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>symboling</th>
          <th>normalized-losses</th>
          <th>make</th>
          <th>fuel-type</th>
          <th>aspiration</th>
          <th>num-of-doors</th>
          <th>body-style</th>
          <th>drive-wheels</th>
          <th>engine-location</th>
          <th>wheel-base</th>
          <th>...</th>
          <th>engine-size</th>
          <th>fuel-system</th>
          <th>bore</th>
          <th>stroke</th>
          <th>compression-ratio</th>
          <th>horsepower</th>
          <th>peak-rpm</th>
          <th>city-mpg</th>
          <th>highway-mpg</th>
          <th>price</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>3</td>
          <td>NaN</td>
          <td>alfa-romero</td>
          <td>gas</td>
          <td>std</td>
          <td>two</td>
          <td>convertible</td>
          <td>rwd</td>
          <td>front</td>
          <td>88.6</td>
          <td>...</td>
          <td>130</td>
          <td>mpfi</td>
          <td>3.47</td>
          <td>2.68</td>
          <td>9.0</td>
          <td>111</td>
          <td>5000</td>
          <td>21</td>
          <td>27</td>
          <td>13495</td>
        </tr>
        <tr>
          <th>1</th>
          <td>3</td>
          <td>NaN</td>
          <td>alfa-romero</td>
          <td>gas</td>
          <td>std</td>
          <td>two</td>
          <td>convertible</td>
          <td>rwd</td>
          <td>front</td>
          <td>88.6</td>
          <td>...</td>
          <td>130</td>
          <td>mpfi</td>
          <td>3.47</td>
          <td>2.68</td>
          <td>9.0</td>
          <td>111</td>
          <td>5000</td>
          <td>21</td>
          <td>27</td>
          <td>16500</td>
        </tr>
        <tr>
          <th>2</th>
          <td>1</td>
          <td>NaN</td>
          <td>alfa-romero</td>
          <td>gas</td>
          <td>std</td>
          <td>two</td>
          <td>hatchback</td>
          <td>rwd</td>
          <td>front</td>
          <td>94.5</td>
          <td>...</td>
          <td>152</td>
          <td>mpfi</td>
          <td>2.68</td>
          <td>3.47</td>
          <td>9.0</td>
          <td>154</td>
          <td>5000</td>
          <td>19</td>
          <td>26</td>
          <td>16500</td>
        </tr>
        <tr>
          <th>3</th>
          <td>2</td>
          <td>164</td>
          <td>audi</td>
          <td>gas</td>
          <td>std</td>
          <td>four</td>
          <td>sedan</td>
          <td>fwd</td>
          <td>front</td>
          <td>99.8</td>
          <td>...</td>
          <td>109</td>
          <td>mpfi</td>
          <td>3.19</td>
          <td>3.40</td>
          <td>10.0</td>
          <td>102</td>
          <td>5500</td>
          <td>24</td>
          <td>30</td>
          <td>13950</td>
        </tr>
        <tr>
          <th>4</th>
          <td>2</td>
          <td>164</td>
          <td>audi</td>
          <td>gas</td>
          <td>std</td>
          <td>four</td>
          <td>sedan</td>
          <td>4wd</td>
          <td>front</td>
          <td>99.4</td>
          <td>...</td>
          <td>136</td>
          <td>mpfi</td>
          <td>3.19</td>
          <td>3.40</td>
          <td>8.0</td>
          <td>115</td>
          <td>5500</td>
          <td>18</td>
          <td>22</td>
          <td>17450</td>
        </tr>
      </tbody>
    </table>
    <p>5 rows × 26 columns</p>
    </div>



dentify\_missing\_values

.. raw:: html

   <h4>

Evaluating for Missing Data

.. raw:: html

   </h4>

The missing values are converted to Python's default. We use Python's
built-in functions to identify these missing values. There are two
methods to detect missing data:

.. raw:: html

   <ol>

::

    <li><b>.isnull()</b></li>
    <li><b>.notnull()</b></li>

.. raw:: html

   </ol>

The output is a boolean value indicating whether the value that is
passed into the argument is in fact missing data.

.. code:: ipython3

    missing_data = df.isnull()
    missing_data.head(5)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>symboling</th>
          <th>normalized-losses</th>
          <th>make</th>
          <th>fuel-type</th>
          <th>aspiration</th>
          <th>num-of-doors</th>
          <th>body-style</th>
          <th>drive-wheels</th>
          <th>engine-location</th>
          <th>wheel-base</th>
          <th>...</th>
          <th>engine-size</th>
          <th>fuel-system</th>
          <th>bore</th>
          <th>stroke</th>
          <th>compression-ratio</th>
          <th>horsepower</th>
          <th>peak-rpm</th>
          <th>city-mpg</th>
          <th>highway-mpg</th>
          <th>price</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>False</td>
          <td>True</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>...</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
        </tr>
        <tr>
          <th>1</th>
          <td>False</td>
          <td>True</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>...</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
        </tr>
        <tr>
          <th>2</th>
          <td>False</td>
          <td>True</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>...</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
        </tr>
        <tr>
          <th>3</th>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>...</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
        </tr>
        <tr>
          <th>4</th>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>...</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
          <td>False</td>
        </tr>
      </tbody>
    </table>
    <p>5 rows × 26 columns</p>
    </div>



"True" stands for missing value, while "False" stands for not missing
value.

.. raw:: html

   <h4>

Count missing values in each column

.. raw:: html

   </h4>

.. raw:: html

   <p>

Using a for loop in Python, we can quickly figure out the number of
missing values in each column. As mentioned above, "True" represents a
missing value, "False" means the value is present in the dataset. In the
body of the for loop the method ".value\_counts()" counts the number of
"True" values.

.. raw:: html

   </p>

.. code:: ipython3

    for column in missing_data.columns.values.tolist():
        print(column)
        print (missing_data[column].value_counts())
        print("")    


.. parsed-literal::

    symboling
    False    205
    Name: symboling, dtype: int64
    
    normalized-losses
    False    164
    True      41
    Name: normalized-losses, dtype: int64
    
    make
    False    205
    Name: make, dtype: int64
    
    fuel-type
    False    205
    Name: fuel-type, dtype: int64
    
    aspiration
    False    205
    Name: aspiration, dtype: int64
    
    num-of-doors
    False    203
    True       2
    Name: num-of-doors, dtype: int64
    
    body-style
    False    205
    Name: body-style, dtype: int64
    
    drive-wheels
    False    205
    Name: drive-wheels, dtype: int64
    
    engine-location
    False    205
    Name: engine-location, dtype: int64
    
    wheel-base
    False    205
    Name: wheel-base, dtype: int64
    
    length
    False    205
    Name: length, dtype: int64
    
    width
    False    205
    Name: width, dtype: int64
    
    height
    False    205
    Name: height, dtype: int64
    
    curb-weight
    False    205
    Name: curb-weight, dtype: int64
    
    engine-type
    False    205
    Name: engine-type, dtype: int64
    
    num-of-cylinders
    False    205
    Name: num-of-cylinders, dtype: int64
    
    engine-size
    False    205
    Name: engine-size, dtype: int64
    
    fuel-system
    False    205
    Name: fuel-system, dtype: int64
    
    bore
    False    201
    True       4
    Name: bore, dtype: int64
    
    stroke
    False    201
    True       4
    Name: stroke, dtype: int64
    
    compression-ratio
    False    205
    Name: compression-ratio, dtype: int64
    
    horsepower
    False    203
    True       2
    Name: horsepower, dtype: int64
    
    peak-rpm
    False    203
    True       2
    Name: peak-rpm, dtype: int64
    
    city-mpg
    False    205
    Name: city-mpg, dtype: int64
    
    highway-mpg
    False    205
    Name: highway-mpg, dtype: int64
    
    price
    False    201
    True       4
    Name: price, dtype: int64
    


Based on the summary above, each column has 205 rows of data, seven
columns containing missing data:

.. raw:: html

   <ol>

::

    <li>"normalized-losses": 41 missing data</li>
    <li>"num-of-doors": 2 missing data</li>
    <li>"bore": 4 missing data</li>
    <li>"stroke" : 4 missing data</li>
    <li>"horsepower": 2 missing data</li>
    <li>"peak-rpm": 2 missing data</li>
    <li>"price": 4 missing data</li>

.. raw:: html

   </ol>

.. raw:: html

   <h3 id="deal_missing_values">

Deal with missing data

.. raw:: html

   </h3>

How to deal with missing data?

.. raw:: html

   <ol>

::

    <li>drop data<br>
        a. drop the whole row<br>
        b. drop the whole column
    </li>
    <li>replace data<br>
        a. replace it by mean<br>
        b. replace it by frequency<br>
        c. replace it based on other functions
    </li>

.. raw:: html

   </ol>

Whole columns should be dropped only if most entries in the column are
empty. In our dataset, none of the columns are empty enough to drop
entirely. We have some freedom in choosing which method to replace data;
however, some methods may seem more reasonable than others. We will
apply each method to many different columns:

Replace by mean:

.. raw:: html

   <ul>

::

    <li>"normalized-losses": 41 missing data, replace them with mean</li>
    <li>"stroke": 4 missing data, replace them with mean</li>
    <li>"bore": 4 missing data, replace them with mean</li>
    <li>"horsepower": 2 missing data, replace them with mean</li>
    <li>"peak-rpm": 2 missing data, replace them with mean</li>

.. raw:: html

   </ul>

Replace by frequency:

.. raw:: html

   <ul>

::

    <li>"num-of-doors": 2 missing data, replace them with "four". 
        <ul>
            <li>Reason: 84% sedans is four doors. Since four doors is most frequent, it is most likely to occur</li>
        </ul>
    </li>

.. raw:: html

   </ul>

Drop the whole row:

.. raw:: html

   <ul>

::

    <li>"price": 4 missing data, simply delete the whole row
        <ul>
            <li>Reason: price is what we want to predict. Any data entry without price data cannot be used for prediction; therefore any row now without price data is not useful to us</li>
        </ul>
    </li>

.. raw:: html

   </ul>

.. raw:: html

   <h4>

Calculate the average of the column

.. raw:: html

   </h4>

.. code:: ipython3

    avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
    print("Average of normalized-losses:", avg_norm_loss)


.. parsed-literal::

    Average of normalized-losses: 122.0


.. raw:: html

   <h4>

Replace "NaN" by mean value in "normalized-losses" column

.. raw:: html

   </h4>

.. code:: ipython3

    df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

.. raw:: html

   <h4>

Calculate the mean value for 'bore' column

.. raw:: html

   </h4>

.. code:: ipython3

    avg_bore=df['bore'].astype('float').mean(axis=0)
    print("Average of bore:", avg_bore)


.. parsed-literal::

    Average of bore: 3.3297512437810943


.. raw:: html

   <h4>

Replace NaN by mean value

.. raw:: html

   </h4>

.. code:: ipython3

    df["bore"].replace(np.nan, avg_bore, inplace=True)

.. raw:: html

   <div class="alert alert-danger alertdanger" style="margin-top: 20px">

.. raw:: html

   <h1>

Question #1:

.. raw:: html

   </h1>

According to the example above, replace NaN in "stroke" column by mean.

.. raw:: html

   </div>

.. code:: ipython3

    # Write your code below and press Shift+Enter to execute 


Double-click here for the solution.

.. raw:: html

   <!-- The answer is below:

   # calculate the mean vaule for "stroke" column
   avg_stroke = df["stroke"].astype("float").mean(axis = 0)
   print("Average of stroke:", avg_stroke)

   # replace NaN by mean value in "stroke" column
   df["stroke"].replace(np.nan, avg_stroke, inplace = True)

   -->

.. raw:: html

   <h4>

Calculate the mean value for the 'horsepower' column:

.. raw:: html

   </h4>

.. code:: ipython3

    avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
    print("Average horsepower:", avg_horsepower)

.. raw:: html

   <h4>

Replace "NaN" by mean value:

.. raw:: html

   </h4>

.. code:: ipython3

    df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

.. raw:: html

   <h4>

Calculate the mean value for 'peak-rpm' column:

.. raw:: html

   </h4>

.. code:: ipython3

    avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
    print("Average peak rpm:", avg_peakrpm)

.. raw:: html

   <h4>

Replace NaN by mean value:

.. raw:: html

   </h4>

.. code:: ipython3

    df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

To see which values are present in a particular column, we can use the
".value\_counts()" method:

.. code:: ipython3

    df['num-of-doors'].value_counts()

We can see that four doors are the most common type. We can also use the
".idxmax()" method to calculate for us the most common type
automatically:

.. code:: ipython3

    df['num-of-doors'].value_counts().idxmax()

The replacement procedure is very similar to what we have seen
previously

.. code:: ipython3

    #replace the missing 'num-of-doors' values by the most frequent 
    df["num-of-doors"].replace(np.nan, "four", inplace=True)

Finally, let's drop all rows that do not have price data:

.. code:: ipython3

    # simply drop whole row with NaN in "price" column
    df.dropna(subset=["price"], axis=0, inplace=True)
    
    # reset index, because we droped two rows
    df.reset_index(drop=True, inplace=True)

.. code:: ipython3

    df.head()

Good! Now, we obtain the dataset with no missing values.

.. raw:: html

   <h3 id="correct_data_format">

Correct data format

.. raw:: html

   </h3>

We are almost there!

.. raw:: html

   <p>

The last step in data cleaning is checking and making sure that all data
is in the correct format (int, float, text or other).

.. raw:: html

   </p>

In Pandas, we use

.. raw:: html

   <p>

.dtype() to check the data type

.. raw:: html

   </p>

.. raw:: html

   <p>

.astype() to change the data type

.. raw:: html

   </p>

.. raw:: html

   <h4>

Lets list the data types for each column

.. raw:: html

   </h4>

.. code:: ipython3

    df.dtypes

.. raw:: html

   <p>

As we can see above, some columns are not of the correct data type.
Numerical variables should have type 'float' or 'int', and variables
with strings such as categories should have type 'object'. For example,
'bore' and 'stroke' variables are numerical values that describe the
engines, so we should expect them to be of the type 'float' or 'int';
however, they are shown as type 'object'. We have to convert data types
into a proper format for each column using the "astype()" method.

.. raw:: html

   </p>

.. raw:: html

   <h4>

Convert data types to proper format

.. raw:: html

   </h4>

.. code:: ipython3

    df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
    df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
    df[["price"]] = df[["price"]].astype("float")
    df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

.. raw:: html

   <h4>

Let us list the columns after the conversion

.. raw:: html

   </h4>

.. code:: ipython3

    df.dtypes

Wonderful!

Now, we finally obtain the cleaned dataset with no missing values and
all data in its proper format.

.. raw:: html

   <h2 id="data_standardization">

Data Standardization

.. raw:: html

   </h2>

.. raw:: html

   <p>

Data is usually collected from different agencies with different
formats. (Data Standardization is also a term for a particular type of
data normalization, where we subtract the mean and divide by the
standard deviation)

.. raw:: html

   </p>

What is Standardization?

.. raw:: html

   <p>

Standardization is the process of transforming data into a common format
which allows the researcher to make the meaningful comparison.

.. raw:: html

   </p>

Example

.. raw:: html

   <p>

Transform mpg to L/100km:

.. raw:: html

   </p>

.. raw:: html

   <p>

In our dataset, the fuel consumption columns "city-mpg" and
"highway-mpg" are represented by mpg (miles per gallon) unit. Assume we
are developing an application in a country that accept the fuel
consumption with L/100km standard

.. raw:: html

   </p>

.. raw:: html

   <p>

We will need to apply data transformation to transform mpg into L/100km?

.. raw:: html

   </p>

.. raw:: html

   <p>

The formula for unit conversion is

.. raw:: html

   <p>

L/100km = 235 / mpg

.. raw:: html

   <p>

We can do many mathematical operations directly in Pandas.

.. raw:: html

   </p>

.. code:: ipython3

    df.head()

.. code:: ipython3

    # Convert mpg to L/100km by mathematical operation (235 divided by mpg)
    df['city-L/100km'] = 235/df["city-mpg"]
    
    # check your transformed data 
    df.head()

.. raw:: html

   <div class="alert alert-danger alertdanger" style="margin-top: 20px">

.. raw:: html

   <h1>

Question #2:

.. raw:: html

   </h1>

According to the example above, transform mpg to L/100km in the column
of "highway-mpg", and change the name of column to "highway-L/100km".

.. raw:: html

   </div>

.. code:: ipython3

    # Write your code below and press Shift+Enter to execute 


Double-click here for the solution.

.. raw:: html

   <!-- The answer is below:

   # transform mpg to L/100km by mathematical operation (235 divided by mpg)
   df["highway-mpg"] = 235/df["highway-mpg"]

   # rename column name from "highway-mpg" to "highway-L/100km"
   df.rename(columns={'"highway-mpg"':'highway-L/100km'}, inplace=True)

   # check your transformed data 
   df.head()

   -->

.. raw:: html

   <h2 id="data_normalization">

Data Normalization

.. raw:: html

   </h2>

Why normalization?

.. raw:: html

   <p>

Normalization is the process of transforming values of several variables
into a similar range. Typical normalizations include scaling the
variable so the variable average is 0, scaling the variable so the
variance is 1, or scaling variable so the variable values range from 0
to 1

.. raw:: html

   </p>

Example

.. raw:: html

   <p>

To demonstrate normalization, let's say we want to scale the columns
"length", "width" and "height"

.. raw:: html

   </p>

.. raw:: html

   <p>

Target:would like to Normalize those variables so their value ranges
from 0 to 1.

.. raw:: html

   </p>

.. raw:: html

   <p>

Approach: replace original value by (original value)/(maximum value)

.. raw:: html

   </p>

.. code:: ipython3

    # replace (original value) by (original value)/(maximum value)
    df['length'] = df['length']/df['length'].max()
    df['width'] = df['width']/df['width'].max()

.. raw:: html

   <div class="alert alert-danger alertdanger" style="margin-top: 20px">

.. raw:: html

   <h1>

Questiont #3:

.. raw:: html

   </h1>

According to the example above, normalize the column "height".

.. raw:: html

   </div>

.. code:: ipython3

    # Write your code below and press Shift+Enter to execute 


Double-click here for the solution.

.. raw:: html

   <!-- The answer is below:

   df['height'] = df['height']/df['height'].max() 
   # show the scaled columns
   df[["length","width","height"]].head()

   -->

Here we can see, we've normalized "length", "width" and "height" in the
range of [0,1].

.. raw:: html

   <h2 id="binning">

Binning

.. raw:: html

   </h2>

Why binning?

.. raw:: html

   <p>

::

    Binning is a process of transforming continuous numerical variables into discrete categorical 'bins', for grouped analysis.

.. raw:: html

   </p>

Example:

.. raw:: html

   <p>

In our dataset, "horsepower" is a real valued variable ranging from 48
to 288, it has 57 unique values. What if we only care about the price
difference between cars with high horsepower, medium horsepower, and
little horsepower (3 types)? Can we rearrange them into three ‘bins' to
simplify analysis?

.. raw:: html

   </p>

.. raw:: html

   <p>

We will use the Pandas method 'cut' to segment the 'horsepower' column
into 3 bins

.. raw:: html

   </p>

.. raw:: html

   <h3>

Example of Binning Data In Pandas

.. raw:: html

   </h3>

Convert data to correct format

.. code:: ipython3

    df["horsepower"]=df["horsepower"].astype(int, copy=True)

Lets plot the histogram of horspower, to see what the distribution of
horsepower looks like.

.. code:: ipython3

    %matplotlib inline
    import matplotlib as plt
    from matplotlib import pyplot
    plt.pyplot.hist(df["horsepower"])
    
    # set x/y labels and plot title
    plt.pyplot.xlabel("horsepower")
    plt.pyplot.ylabel("count")
    plt.pyplot.title("horsepower bins")

.. raw:: html

   <p>

We would like 3 bins of equal size bandwidth so we use numpy's
linspace(start\_value, end\_value, numbers\_generated function.

.. raw:: html

   </p>

.. raw:: html

   <p>

Since we want to include the minimum value of horsepower we want to set
start\_value=min(df["horsepower"]).

.. raw:: html

   </p>

.. raw:: html

   <p>

Since we want to include the maximum value of horsepower we want to set
end\_value=max(df["horsepower"]).

.. raw:: html

   </p>

.. raw:: html

   <p>

Since we are building 3 bins of equal length, there should be 4
dividers, so numbers\_generated=4.

.. raw:: html

   </p>

We build a bin array, with a minimum value to a maximum value, with
bandwidth calculated above. The bins will be values used to determine
when one bin ends and another begins.

.. code:: ipython3

    bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
    bins

We set group names:

.. code:: ipython3

    group_names = ['Low', 'Medium', 'High']

We apply the function "cut" the determine what each value of
"df['horsepower']" belongs to.

.. code:: ipython3

    df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
    df[['horsepower','horsepower-binned']].head(20)

Lets see the number of vehicles in each bin.

.. code:: ipython3

    df["horsepower-binned"].value_counts()

Lets plot the distribution of each bin.

.. code:: ipython3

    %matplotlib inline
    import matplotlib as plt
    from matplotlib import pyplot
    pyplot.bar(group_names, df["horsepower-binned"].value_counts())
    
    # set x/y labels and plot title
    plt.pyplot.xlabel("horsepower")
    plt.pyplot.ylabel("count")
    plt.pyplot.title("horsepower bins")

.. raw:: html

   <p>

::

    Check the dataframe above carefully, you will find the last column provides the bins for "horsepower" with 3 categories ("Low","Medium" and "High"). 

.. raw:: html

   </p>

.. raw:: html

   <p>

::

    We successfully narrow the intervals from 57 to 3!

.. raw:: html

   </p>

.. raw:: html

   <h3>

Bins visualization

.. raw:: html

   </h3>

Normally, a histogram is used to visualize the distribution of bins we
created above.

.. code:: ipython3

    %matplotlib inline
    import matplotlib as plt
    from matplotlib import pyplot
    
    a = (0,1,2)
    
    # draw historgram of attribute "horsepower" with bins = 3
    plt.pyplot.hist(df["horsepower"], bins = 3)
    
    # set x/y labels and plot title
    plt.pyplot.xlabel("horsepower")
    plt.pyplot.ylabel("count")
    plt.pyplot.title("horsepower bins")

The plot above shows the binning result for attribute "horsepower".

.. raw:: html

   <h2 id="indicator">

Indicator variable (or dummy variable)

.. raw:: html

   </h2>

What is an indicator variable?

.. raw:: html

   <p>

::

    An indicator variable (or dummy variable) is a numerical variable used to label categories. They are called 'dummies' because the numbers themselves don't have inherent meaning. 

.. raw:: html

   </p>

Why we use indicator variables?

.. raw:: html

   <p>

::

    So we can use categorical variables for regression analysis in the later modules.

.. raw:: html

   </p>

Example

.. raw:: html

   <p>

::

    We see the column "fuel-type" has two unique values, "gas" or "diesel". Regression doesn't understand words, only numbers. To use this attribute in regression analysis, we convert "fuel-type" into indicator variables.

.. raw:: html

   </p>

.. raw:: html

   <p>

::

    We will use the panda's method 'get_dummies' to assign numerical values to different categories of fuel type. 

.. raw:: html

   </p>

.. code:: ipython3

    df.columns

get indicator variables and assign it to data frame "dummy\_variable\_1"

.. code:: ipython3

    dummy_variable_1 = pd.get_dummies(df["fuel-type"])
    dummy_variable_1.head()

change column names for clarity

.. code:: ipython3

    dummy_variable_1.rename(columns={'fuel-type-diesel':'gas', 'fuel-type-diesel':'diesel'}, inplace=True)
    dummy_variable_1.head()

We now have the value 0 to represent "gas" and 1 to represent "diesel"
in the column "fuel-type". We will now insert this column back into our
original dataset.

.. code:: ipython3

    # merge data frame "df" and "dummy_variable_1" 
    df = pd.concat([df, dummy_variable_1], axis=1)
    
    # drop original column "fuel-type" from "df"
    df.drop("fuel-type", axis = 1, inplace=True)

.. code:: ipython3

    df.head()

The last two columns are now the indicator variable representation of
the fuel-type variable. It's all 0s and 1s now.

.. raw:: html

   <div class="alert alert-danger alertdanger" style="margin-top: 20px">

.. raw:: html

   <h1>

Question #4:

.. raw:: html

   </h1>

As above, create indicator variable to the column of "aspiration": "std"
to 0, while "turbo" to 1.

.. raw:: html

   </div>

.. code:: ipython3

    # Write your code below and press Shift+Enter to execute 


Double-click here for the solution.

.. raw:: html

   <!-- The answer is below:

   # get indicator variables of aspiration and assign it to data frame "dummy_variable_2"
   dummy_variable_2 = pd.get_dummies(df['aspiration'])

   # change column names for clarity
   dummy_variable_2.rename(columns={'std':'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)

   # show first 5 instances of data frame "dummy_variable_1"
   dummy_variable_2.head()

   -->

.. raw:: html

   <div class="alert alert-danger alertdanger" style="margin-top: 20px">

.. raw:: html

   <h1>

Question #5:

.. raw:: html

   </h1>

Merge the new dataframe to the original dataframe then drop the column
'aspiration'

.. raw:: html

   </div>

.. code:: ipython3

    # Write your code below and press Shift+Enter to execute 


Double-click here for the solution.

.. raw:: html

   <!-- The answer is below:

   #merge the new dataframe to the original datafram
   df = pd.concat([df, dummy_variable_2], axis=1)

   # drop original column "aspiration" from "df"
   df.drop('aspiration', axis = 1, inplace=True)

   -->

save the new csv

.. code:: ipython3

    df.to_csv('clean_df.csv')

.. raw:: html

   <h1>

Thank you for completing this notebook

.. raw:: html

   </h1>

.. raw:: html

   <div class="alert alert-block alert-info" style="margin-top: 20px">

::

    <p><a href="https://cocl.us/corsera_da0101en_notebook_bottom"><img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/Images/BottomAd.png" width="750" align="center"></a></p>

.. raw:: html

   </div>

.. raw:: html

   <h3>

About the Authors:

.. raw:: html

   </h3>

This notebook was written by Mahdi Noorian PhD, Joseph Santarcangelo,
Bahare Talayian, Eric Xiao, Steven Dong, Parizad, Hima Vsudevan and
Fiorella Wenver and Yi Yao.

.. raw:: html

   <p>

Joseph Santarcangelo is a Data Scientist at IBM, and holds a PhD in
Electrical Engineering. His research focused on using Machine Learning,
Signal Processing, and Computer Vision to determine how videos impact
human cognition. Joseph has been working for IBM since he completed his
PhD.

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <p>

Copyright © 2018 IBM Developer Skills Network. This notebook and its
source code are released under the terms of the MIT License.

.. raw:: html

   </p>
