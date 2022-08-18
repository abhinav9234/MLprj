#!/usr/bin/env python
# coding: utf-8

# In[2]:


#read the data first


# In[3]:


import pandas as pd


# In[4]:


pip install pandas


# In[124]:


df1=pd.read_excel(r"C:\Users\rumad\OneDrive\Desktop\Wine Synthetic data .xlsx")


# In[125]:


df1.head()


# In[126]:


df1.describe()


# In[127]:


pip install plotly


# In[128]:


pip install plotly_express


# In[129]:


import plotly_express as px


# In[193]:


fig1=px.scatter(df1,x="Country",y="Sales")


# In[194]:


fig1.show()


# In[132]:


feature_cols=["Malvia","Felto"]


# In[133]:


x=df1[feature_cols]


# In[134]:


y=df1.Sales


# In[135]:


import sklearn as sk


# In[136]:


pip install sklearn


# In[171]:


#dummy encoding in the column nothing can be in strings so to change in numbers you need to give number
final_data=pd.get_dummies(df1,columns=["Country"])


# In[175]:


final_data.head(5)


# In[176]:


from sklearn.model_selection import train_test_split


# In[177]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=6)


# In[178]:


x_train.shape


# In[179]:


y_train.shape


# In[180]:


pip install algorithm


# In[183]:


import algorithm as algo


# In[184]:


pip install DecisionTree


# In[185]:


from sklearn.tree import DecisionTreeRegressor


# In[186]:


dtree=DecisionTreeRegressor()


# In[187]:


dtree.fit(x_train,y_train)


# In[188]:


prediction=dtree.predict(x_test)


# In[190]:


y_test


# In[191]:


x_test


# In[199]:


prediction


# In[163]:


#Validation Technique is different for regression and classifier- do that to understand the accuracy of the model

