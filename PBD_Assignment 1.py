#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../input/nodules-in-chest-xrays-jsrt/jsrt_metadata.csv')
df.head()
gender_meta_data = {'female':1,'male':0}
df['gender'] = gender_labels
df.head()
labels_metadata = {'malignant':2,'non-nodule':0,'benign':1}
df['state'] = df['state'].map(labels_metadata)
df.head()
df['diagnosis'].unique()

df['diagnosis'].plot(kind='hist')


# In[2]:


#Question 2
diagnosis_data = df["diagnosis"]
state_data = df["state"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (0.1, 0, 0, 0, 0)  
plt.pie(state_data, labels=diagnosis_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Total number of patients of each disease with respect to the disease state malignant or benign")
plot in a pie chart.")
plt.show()
          


          


# In[ ]:


#Question 3

diagnosis_data = df["diagnosis"]
gender_data = df["gender"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (0.1, 0, 0, 0, 0)  
plt.pie(gender_data, labels=diagnosis_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title(" Total number of patients of each diagnosis with respect to the gender Female Male")
plot in a pie chart.")
plt.show()
 

