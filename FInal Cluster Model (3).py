#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


# RFM Code


# In[76]:


import pandas as pd

# Load your CSV file
data = pd.read_csv("RFM_Final_Pivot.csv")

# Display the first few rows of the DataFrame to check if the data is loaded correctly
data.head()




   










# In[78]:


# Calculate the recency percentiles
data['Recency_Score'] = pd.qcut(data['Recency'], q=5, labels=[5, 4, 3, 2, 1])

# Display the resulting DataFrame with Recency Score
print(data[['Recency', 'Recency_Score']].head())


# In[79]:


# Define a dictionary to map Frequency values to scores
frequency_score_mapping = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5
}

# Assign Frequency scores based on the mapping
data['Frequency_Score'] = data['Frequency'].map(frequency_score_mapping)

# Display the resulting DataFrame with Frequency Score
print(data[['Frequency', 'Frequency_Score']].head())



# In[80]:


# Define a dictionary to map Monetary percentiles to scores
monetary_percentile_mapping = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5
}

# Calculate the Monetary percentiles for each row
data['Monetary_Percentile'] = pd.qcut(data['Monetary'], q=5, labels=[1, 2, 3, 4, 5])

# Assign Monetary scores based on the mapping
data['Monetary_Score'] = data['Monetary_Percentile'].map(monetary_percentile_mapping)

# Display the resulting DataFrame with Monetary Score
print(data[['Monetary', 'Monetary_Score']].head())















# In[81]:


# Define a dictionary to map RFM scores to customer categories
rfm_mapping = {
    111: 'Lost Customers',
    112: 'Lost Customers',
    113: 'Lost Customers',
    114: 'Lost Customers',
    115: 'Lost Customers',
    121: 'Lost Customers',
    122: 'Lost Customers',
    123: 'Lost Customers',
    124: 'Lost Customers',
    125: 'Lost Customers',
    131: 'Lost Customers',
    132: 'Lost Customers',
    133: 'Hibernating',
    134: 'Hibernating',
    135: 'Hibernating',
    141: 'Hibernating',
    142: 'Hibernating',
    143: 'Hibernating',
    144: 'Hibernating',
    145: 'Hibernating',
    151: 'Hibernating',
    152: 'Hibernating',
    153: 'Hibernating',
    154: 'Hibernating',
    155: 'Cant Lose Them',
    211: 'About to Churn',
    212: 'About to Churn',
    213: 'About to Churn',
    214: 'About to Churn',
    215: 'About to Churn',
    221: 'About to Churn',
    222: 'About to Churn',
    223: 'About to Churn',
    224: 'About to Churn',
    225: 'About to Churn',
    231: 'About to Churn',
    232: 'About to Churn',
    233: 'Hibernating',
    234: 'Hibernating',
    235: 'Hibernating',
    241: 'Hibernating',
    242: 'Hibernating',
    243: 'Hibernating',
    244: 'Hibernating',
    245: 'Hibernating',
    251: 'Hibernating',
    252: 'Hibernating',
    253: 'Hibernating',
    254: 'Hibernating',
    255: 'Cant Lose Them',
    311: 'Price Sensitive',
    312: 'Price Sensitive',
    313: 'Price Sensitive',
    314: 'Price Sensitive',
    315: 'Price Sensitive',
    321: 'Price Sensitive',
    322: 'Price Sensitive',
    323: 'Price Sensitive',
    324: 'Price Sensitive',
    325: 'Price Sensitive',
    331: 'Price Sensitive',
    332: 'Price Sensitive',
    333: 'Price Sensitive',
    334: 'Price Sensitive',
    335: 'Price Sensitive',
    341: 'Price Sensitive',
    342: 'Price Sensitive',
    343: 'Price Sensitive',
    344: 'Attention',
    345: 'Attention',
    351: 'Attention',
    352: 'Attention',
    353: 'Attention',
    354: 'Attention',
    355: 'Attention',
    411: 'Promising',
    412: 'Promising',
    413: 'Promising',
    414: 'Promising',
    415: 'Promising',
    421: 'Promising',
    422: 'Promising',
    423: 'Promising',
    424: 'Promising',
    425: 'Promising',
    431: 'Promising',
    432: 'Promising',
    433: 'Potential Loyalist',
    434: 'Potential Loyalist',
    435: 'Potential Loyalist',
    441: 'Potential Loyalist',
    442: 'Potential Loyalist',
    443: 'Potential Loyalist',
    444: 'Potential Loyalist',
    445: 'Loyal Customers',
    451: 'Loyal Customers',
    452: 'Loyal Customers',
    453: 'Loyal Customers',
    454: 'Loyal Customers',
    455: 'Loyal Customers',
    511: 'Recent Users',
    512: 'Recent Users',
    513: 'Recent Users',
    514: 'Recent Users',
    515: 'Recent Users',
    521: 'Recent Users',
    522: 'Recent Users',
    523: 'Recent Users',
    524: 'Recent Users',
    525: 'Recent Users',
    531: 'Recent Users',
    532: 'Recent Users',
    533: 'Recent Users',
    534: 'Recent Users',
    535: 'Recent Users',
    541: 'Recent Users',
    542: 'Recent Users',
    543: 'Recent Users',
    544: 'Recent Users',
    545: 'Recent Users',
    551: 'Recent Users',
    552: 'Recent Users',
    553: 'Recent Users',
    554: 'Recent Users',
    555: 'Recent Users'
}

# Define a function to map RFM scores to customer categories
def map_rfm_to_category(row):
    recency_score = int(row['Recency_Score'])
    frequency_score = int(row['Frequency_Score']) if not pd.isna(row['Frequency_Score']) else 0
    monetary_score = int(row['Monetary_Score']) if not pd.isna(row['Monetary_Score']) else 0
    
    rfm_score = recency_score * 100 + frequency_score * 10 + monetary_score
    
    return rfm_mapping.get(rfm_score, 'Unknown')

# Apply the function to map RFM scores to customer categories
data['Customer_Category'] = data.apply(map_rfm_to_category, axis=1)

# Display the DataFrame with the Customer Category
print(data[['Cust_Id', 'Customer_Category']].head())

 



# In[83]:


# Count the occurrences of each customer category
category_counts = data['Customer_Category'].value_counts()

# Display the count for each category
print(category_counts)

  


# In[82]:


import matplotlib.pyplot as plt
import seaborn as sns

# Create a pivot table for the 2D matrix plot
pivot_table = data.pivot_table(index='Monetary_Score', columns='Recency_Score', values='Frequency_Score', aggfunc='mean')

# Create a heatmap using seaborn for the frequency plot
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="YlGnBu", cbar=False)

# Set axis labels and title for the frequency plot
plt.xlabel('Recency')
plt.ylabel('Monetary')
plt.title('2D Matrix Box Plot of Frequency with RFM Segments')

# Create a secondary Y-axis for the frequency plot
ax2 = plt.gca().twinx()
pivot_table_freq = data.pivot_table(index='Monetary_Score', columns='Recency_Score', values='Frequency_Score', aggfunc='count')
sns.heatmap(pivot_table_freq, annot=True, fmt=".0f", cmap="Blues", cbar=False, ax=ax2)
ax2.set_ylabel('Frequency Count')

# Display the plot
plt.show()




# In[84]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a pivot table for the 2D matrix plot
pivot_table = data.pivot_table(index='Monetary_Score', columns='Recency_Score', values='Customer_Category', aggfunc='count')

# Create a formatted annotation DataFrame for counts
# Create a formatted annotation DataFrame for counts and category names
pivot_table_annotations_count = pivot_table.applymap(lambda x: f"{x}\n{rfm_mapping.get(int(x), 'Unknown')}")


# Create a mapping of RFM codes to category names
rfm_mapping = {
    111: 'Lost Customers',
    112: 'Lost Customers',
    113: 'Lost Customers',
    114: 'Lost Customers',
    115: 'Lost Customers',
    121: 'Lost Customers',
    122: 'Lost Customers',
    123: 'Lost Customers',
    124: 'Lost Customers',
    125: 'Lost Customers',
    131: 'Lost Customers',
    132: 'Lost Customers',
    133: 'Hibernating',
    134: 'Hibernating',
    135: 'Hibernating',
    141: 'Hibernating',
    142: 'Hibernating',
    143: 'Hibernating',
    144: 'Hibernating',
    145: 'Hibernating',
    151: 'Hibernating',
    152: 'Hibernating',
    153: 'Hibernating',
    154: 'Hibernating',
    155: 'Cant Lose Them',
    211: 'About to Churn',
    212: 'About to Churn',
    213: 'About to Churn',
    214: 'About to Churn',
    215: 'About to Churn',
    221: 'About to Churn',
    222: 'About to Churn',
    223: 'About to Churn',
    224: 'About to Churn',
    225: 'About to Churn',
    231: 'About to Churn',
    232: 'About to Churn',
    233: 'Hibernating',
    234: 'Hibernating',
    235: 'Hibernating',
    241: 'Hibernating',
    242: 'Hibernating',
    243: 'Hibernating',
    244: 'Hibernating',
    245: 'Hibernating',
    251: 'Hibernating',
    252: 'Hibernating',
    253: 'Hibernating',
    254: 'Hibernating',
    255: 'Cant Lose Them',
    311: 'Price Sensitive',
    312: 'Price Sensitive',
    313: 'Price Sensitive',
    314: 'Price Sensitive',
    315: 'Price Sensitive',
    321: 'Price Sensitive',
    322: 'Price Sensitive',
    323: 'Price Sensitive',
    324: 'Price Sensitive',
    325: 'Price Sensitive',
    331: 'Price Sensitive',
    332: 'Price Sensitive',
    333: 'Price Sensitive',
    334: 'Price Sensitive',
    335: 'Price Sensitive',
    341: 'Price Sensitive',
    342: 'Price Sensitive',
    343: 'Price Sensitive',
    344: 'Attention',
    345: 'Attention',
    351: 'Attention',
    352: 'Attention',
    353: 'Attention',
    354: 'Attention',
    355: 'Attention',
    411: 'Promising',
    412: 'Promising',
    413: 'Promising',
    414: 'Promising',
    415: 'Promising',
    421: 'Promising',
    422: 'Promising',
    423: 'Promising',
    424: 'Promising',
    425: 'Promising',
    431: 'Promising',
    432: 'Promising',
    433: 'Potential Loyalist',
    434: 'Potential Loyalist',
    435: 'Potential Loyalist',
    441: 'Potential Loyalist',
    442: 'Potential Loyalist',
    443: 'Potential Loyalist',
    444: 'Potential Loyalist',
    445: 'Loyal Customers',
    451: 'Loyal Customers',
    452: 'Loyal Customers',
    453: 'Loyal Customers',
    454: 'Loyal Customers',
    455: 'Loyal Customers',
    511: 'Recent Users',
    512: 'Recent Users',
    513: 'Recent Users',
    514: 'Recent Users',
    515: 'Recent Users',
    521: 'Recent Users',
    522: 'Recent Users',
    523: 'Recent Users',
    524: 'Recent Users',
    525: 'Recent Users',
    531: 'Recent Users',
    532: 'Recent Users',
    533: 'Recent Users',
    534: 'Recent Users',
    535: 'Recent Users',
    541: 'Recent Users',
    542: 'Recent Users',
    543: 'Recent Users',
    544: 'Recent Users',
    545: 'Recent Users',
    551: 'Recent Users',
    552: 'Recent Users',
    553: 'Recent Users',
    554: 'Recent Users',
    555: 'Recent Users'

}

# Map the RFM codes to category names in the pivot_table_annotations_count DataFrame
for idx, row in pivot_table.iterrows():
    for col in pivot_table.columns:
        rfm_code = int(str(idx) + str(col))
        category_name = rfm_mapping.get(rfm_code, 'Unknown')
        pivot_table_annotations_count.loc[idx, col] = f"{row[col]} ({category_name})"


# Create a heatmap using seaborn for the customer category plot
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=pivot_table_annotations_count, fmt="", cmap="YlGnBu", cbar=False, annot_kws={"ha": "center", "va": "center"})

# Set axis labels and title for the customer category plot
plt.xlabel('Recency')
plt.ylabel('Monetary')
plt.title('2D Matrix Box Plot of Customer Categories with RFM Segments')

# Display the plot
plt.show()




# In[ ]:





# In[ ]:




