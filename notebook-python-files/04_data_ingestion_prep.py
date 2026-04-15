#!/usr/bin/env python
# coding: utf-8

# ## Data Ingestion Notebook Prep
# 
# New notebook

# In[1]:


# API url for source data (range from 01/01/2014 to 02/01/2014)
url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02"


# In[3]:


# import requests module to retrive data from source url
import requests


# In[8]:


# status code 200 means the request is successfull
requests.get(url).status_code
# assign request to a variable "response"

response = requests.get(url)


# In[9]:


# return response in json format

response.json()


# In[11]:


# accessing data from the features key

response.json()['features']

