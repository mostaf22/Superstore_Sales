#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[9]:


pip install pandas


# In[10]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import warnings ## used to ignore warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# # Load the Dataset
# 

# In[23]:


df= pd.read_csv('Superstore_Sales.csv', encoding='cp1256')


# In[24]:


df


# In[25]:


print("Shape:", df.shape)
display(df.head())


# # Explore the Data
# 

# In[26]:


display(df.info())


# In[85]:


display(df.describe())


# In[32]:


df = df.dropna()


# In[33]:


df 


# In[34]:


print("\nMissing values per column:")
display(df.isnull().sum())


# In[30]:


# Remove duplicates if any
df.drop_duplicates(inplace=True)
df 


# # Data Cleaning

# In[35]:


# Convert date columns
for col in ['Order Date', 'Ship Date']:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')


# In[36]:


df


# In[37]:


# Extract Year, Month, and Month Name
if 'Order Date' in df.columns:
    df['Order_Year'] = df['Order Date'].dt.year
    df['Order_Month'] = df['Order Date'].dt.month
    df['Order_MonthName'] = df['Order Date'].dt.month_name()


# In[38]:


df


# In[39]:


# Convert numeric columns (Sales, Discount)
for col in ['Sales', 'Discount']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')


# In[40]:


df


# # Basic Analysis
# 

# In[41]:


# Total Sales
total_sales = df['Sales'].sum()
print(f"💰 Total Sales: {total_sales:,.2f}")


# In[42]:


# Sales by Category
if 'Category' in df.columns:
    cat_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    display(cat_sales)


# In[43]:


# Sales by Region
if 'Region' in df.columns:
    reg_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    display(reg_sales)


# In[44]:


# Monthly Sales Trend
if 'Order_MonthName' in df.columns:
    monthly_sales = df.groupby('Order_MonthName')['Sales'].sum().reindex([
        'January','February','March','April','May','June','July','August','September','October','November','December'
    ])
    display(monthly_sales)


# In[45]:


#Total Unique Customers
total_customers = df['Customer ID'].nunique()
print(f"Total Customers: {total_customers}")


# In[66]:


# Total orders
total_orders = df['Order ID'].nunique()
print(f"Total Orders: {total_orders}")


# In[52]:


avg_order_value = total_sales / total_orders
print(f"Average Order Value: {avg_order_value}")


# In[53]:


sales_by_category = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(sales_by_category)


# # Visualizations

# In[57]:


# Sales by Region
if 'Region' in df.columns:
    plt.figure(figsize=(8,5))
    sns.barplot(x='Region', y='Sales', data=df, estimator='sum', ci=None)
    plt.title('Sales by Region')
    plt.show()


# In[60]:


# Sales by Category
if 'Category' in df.columns:
    plt.figure(figsize=(8,5))
    sns.barplot(x='Category', y='Sales', data=df, estimator='sum', ci=None)
    plt.title('Sales by Category')
    plt.show()


# In[58]:


# Monthly Sales Trend
if 'Order_MonthName' in df.columns:
    monthly_sales = df.groupby('Order_MonthName')['Sales'].sum().reindex([
        'January','February','March','April','May','June','July','August','September','October','November','December'
    ])
    plt.figure(figsize=(10,5))
    sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.show()


# In[59]:


# Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# In[72]:


# Category vs Region
if {'Category','Region','Sales'}.issubset(df.columns):
    plt.figure(figsize=(10,6))
    sns.barplot(x='Category', y='Sales', hue='Region', data=df, estimator='sum', ci=None)
    plt.title('Sales by Category and Region')
    plt.show()


# # Save Cleaned Dataset
# 

# In[87]:


df.to_csv("Superstore_Sales_cleaned.csv", index=False)
print("✅ Cleaned data saved as 'Superstore_Sales_cleaned.csv'")

