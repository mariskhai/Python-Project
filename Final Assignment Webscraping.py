#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/Images/SN_logo.png" width="300" alt="cognitiveclass.ai logo">
# </center>
# 

# <h1>Extracting Stock Data Using a Web Scraping</h1>
# 

# Not all stock data is available via API in this assignment; you will use web-scraping to obtain financial data. You will be quizzed on your results.  
#  Using beautiful soup we will extract historical share data from a web-page.
# 

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     
# 1. Extracting data using Beautiful soup
#    
#     <ul> 
#     <li> Downloading the Webpage Using Requests Library </li>
#     <li> Parsing Webpage HTML Using BeautifulSoup </li>
#     <li> Extracting Data and Building DataFrame </li>
# 
#     </ul>
# 
# 2. Extracting data using pandas
# 3. Exercise
# <p>
#     Estimated Time Needed: <strong>30 min</strong></p>
# </div>
# 
# <hr>
# 

# In[1]:


#!pip install pandas==1.3.3
#!pip install requests==2.26.0
get_ipython().system('mamba install bs4==4.10.0 -y')
get_ipython().system('mamba install html5lib==1.1 -y')
get_ipython().system('pip install lxml==4.6.4')
#!pip install plotly==5.3.1


# In[2]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# ## Using Webscraping to Extract Stock Data Example
# 

# We will extract Netflix stock data [https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html).
# 

# <center> 
#     
# #### In this example, we are using yahoo finance website and looking to extract Netflix data.
# 
# </center>
#     <br>
# 
#   <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/Images/netflix.png"> </center> 
#   
# <center> Fig:- Table that we need to extract </center>
# 

# On the following webpage we have a table with columns name (Date, Open, High, Low, close, adj close volume) out of which we must extract following columns  
# 
# * Date 
# 
# * Open  
# 
# * High 
# 
# * Low 
# 
# * Close 
# 
# * Volume 
# 
# 

# # Steps to be followed for extracting data
# 1. Send an HTTP request to the webpage using the requests library.
# 2. Parse the HTML content of the webpage using BeautifulSoup.
# 3. Identify the HTML tags that contain the data you want to extract.
# 4. Use BeautifulSoup methods to extract the data from the HTML tags.
# 5. Print the extracted data
# 

# ### Step-1 Send an HTTP Request to the webpage
# 

# We are using Request library for sending an HTTP request to the webpage.<br>
# 

# In[3]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"


# The requests.get() method takes a URL as its first argument, which specifies the location of the resource to be retrieved. In this case, the value of the url variable is passed as the argument to the requests.get() method, as we've stored a webpage URL in a url variable.
# 
# we have used .text method for extracting the HTML content as a string in order to make it readable.
# 

# In[4]:


data  = requests.get(url).text
print(data)


# ### Step:-2 Parse the HTML content
# 

# <hr>
# <hr>
# <center>
# 
# # What is parsing?
# In simple words, parsing refers to the process of analyzing a string of text or a data structure, usually following a set of rules or grammar, to understand its structure and meaning.
# Parsing involves breaking down a piece of text or data into its individual components or elements, and then analyzing those components to extract the desired information or to understand their relationships and meanings.</center>
# <hr>
# <hr>
# 

# Next we will take the raw HTML content of a webpage or a string of HTML code which needs to be parsed and transformed into a structured, hierarchical format that can be more easily analyzed and manipulated in Python. This can be done using a Python library called <b>Beautiful Soup</b>.
# 

# ## How to parse the data using Beautiful soup library?
# * Create a new Beautiful soup object.
# <br>
# <br>
# <b>Note:- </b>To create a Beautiful Soup object in Python, you need to pass two arguments to its constructor:
# 
# 1. The HTML or XML content that you want to parse as a string.
# 2. The name of the parser that you want to use to parse the HTML or XML content. This argument is optional, and if you don't specify a parser, Beautiful Soup will use the default HTML parser included with the library.
# here in this lab we are using "html5lib" parser.
# 

# In[5]:


soup = BeautifulSoup(data, 'html5lib')


# ### Step-3 Identify the HTML tags
# 

# As stated above webpage consist of table so, we will be scrapping the content of the HTML webpage and convert the table into a dataframe.
# 

# We will creates an empty DataFrame using the <b> pd.DataFrame() </b> function with the following columns.
# * "Date"
# * "Open"
# * "High" 
# * "Low" 
# * "Close"
# * "Volume"
# 

# In[6]:


netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])


# <hr>
# <hr>
# <center>
# 
# ### Working on HTML table  </center>
# <br>
# 
# These are the following tags which are used while creating HTML tables.
# 
# * &lt;table&gt; tag: This tag is root tag used to define the start and end of the table. All the content of the table is enclosed within these tags. 
# 
# 
# * &lt;tr&gt; tag: This tag is used to define a table row. Each row of the table is defined within this tag.
# 
# * &lt;td&gt; tag: This tag is used to define a table cell. Each cell of the table is defined within this tag. You can specify the content of the cell between the opening and closing <td> tags.
# 
# * &lt;th&gt; tag: This tag is used to define a header cell in the table. The header cell is used to describe the contents of a column or row. By default, the text inside a <th> tag is bold and centered.
# 
# * &lt;tbody&gt; tag: This is the main content of the table, which is defined using the <tbody> tag. It contains one or more rows of <tr> elements.
# 
# <hr>
# <hr>
# 
# 

# ### Step-4 Use Beautiful soup method for extracting data
# 

# 
# We will use <b>find()</b> and <b>find_all()</b> methods of the BeautifulSoup object to locate the table body and table row respectively in the HTML. 
#    * The <i>find() method </i> will return particular tag content.
#    * The <i>find_all()</i> method returns a list of all matching tags in the HTML.
# 

# In[7]:


# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    


# ### Step-5 Print the Extracted Data
# 

# We can now print out the DataFrame using head() or tail() function
# 

# In[8]:


netflix_data.head()


# # Extracting data using `pandas` library
# 

# We can also use the pandas `read_html` function from pandas library and use the URL for extracting data.
# 

# <center>
# 
# ## What is read_html in pandas library?
# `pd.read_html(url)` is a function provided by the pandas library in Python that is used to extract tables from HTML web pages. It takes in a URL as input and returns a list of all the tables found on the webpage. 
# </center>
# 

# In[9]:


read_html_pandas_data = pd.read_html(url)


# Or we can convert the BeautifulSoup object to a string
# 

# In[10]:


read_html_pandas_data = pd.read_html(str(soup))


# Because there is only one table on the page, we just take the first table in the list returned
# 

# In[11]:


netflix_dataframe = read_html_pandas_data[0]

netflix_dataframe.head()


# ## Using Webscraping to Extract Stock Data Exercise
# 

# Use the `requests` library to download the webpage [https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html). Save the text of the response as a variable named `html_data`.
# 

# In[12]:


new_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
html_data = requests.get(new_url).text


# Parse the html data using `beautiful_soup`.
# 

# In[13]:


beautiful_soup=BeautifulSoup(html_data,'html5lib')


# <b>Question 1</b> What is the content of the title attribute?
# 

# In[14]:


soup_title=beautiful_soup.title
print("The title is:",soup_title)


# Using beautiful soup extract the table with historical share prices and store it into a dataframe named `amazon_data`. The dataframe should have columns Date, Open, High, Low, Close, Adj Close, and Volume. Fill in each variable with the correct data from the list `col`. 
# 

# In[16]:


amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)


# Print out the first five rows of the `amazon_data` dataframe you created.
# 

# In[17]:


amazon_data.head()


# <b>Question 2</b> What is the name of the columns of the dataframe?
# 

# In[22]:


print(amazon_data.columns)


# <b>Question 3</b> What is the `Open` of the last row of the amazon_data dataframe?
# 

# In[20]:


amazon_data.tail()


# <h2>About the Authors:</h2> 
# 
# <a href="https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork900-2023-01-01">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 
# Azim Hirjani<br>
# Akansha yadav
# 

# ## Change Log
# 
# | Date (YYYY-MM-DD) | Version | Changed By    |       Change Description              |
# | ----------------- | ------- | ------------- | ------------------------------------- |
# |  02-05-2023       |   1.3   | Akansha yadav | Updated Lab content under maintenance |
# |  2021-06-09       | 1.2     | Lakshmi Holla |   Added URL in question 3             |
# |  2020-11-10       | 1.1     | Malika Singla |   Deleted the Optional part           |
# |  2020-08-27       | 1.0     | Malika Singla |   Added lab to GitLab                 |
# 
# <hr>
# 
# ## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
# 
# <p>
# 
