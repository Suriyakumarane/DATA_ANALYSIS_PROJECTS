
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#To ignore warnings
import warnings
warnings.filterwarnings("ignore")  


# In[20]:


file1=pd.read_excel('C:/Users/Gayathri/OneDrive/Desktop/da cf/bps_data/bps_2011_report_english.xlsx')
file2=pd.read_excel('C:/Users/Gayathri/OneDrive/Desktop/da cf/bps_data/bps_2012_report_english.xlsx')
file3=pd.read_excel('C:/Users/Gayathri/OneDrive/Desktop/da cf/bps_data/bps_2013_report_english.xlsx')
file4=pd.read_excel('C:/Users/Gayathri/OneDrive/Desktop/da cf/bps_data/bps_2014_report_english.xlsx')
file5=pd.read_excel('C:/Users/Gayathri/OneDrive/Desktop/da cf/bps_data/bps_2015_report_english.xlsx')
file6=pd.read_excel('C:/Users/Gayathri/OneDrive/Desktop/da cf/bps_data/bps_2016_report_english.xlsx')
file7=pd.read_excel('C:/Users/Gayathri/OneDrive/Desktop/da cf/bps_data/bps_2017_report_english.xlsx')
file8=pd.read_excel('C:/Users/Gayathri/OneDrive/Desktop/da cf/bps_data/bps_2018_report_english.xlsx')
file9=pd.read_excel('C:/Users/Gayathri/OneDrive/Desktop/da cf/bps_data/bps_2019_report_english.xlsx')
file10=pd.read_excel('C:/Users/Gayathri/OneDrive/Desktop/da cf/bps_data/bps_2020_report_english.xlsx')
file11=pd.read_excel('C:/Users/Gayathri/OneDrive/Desktop/da cf/bps_data/bps_2021_report_english.xlsx')


# MERGING DATASET

# In[21]:


file1.head(2)


# In[22]:


pd.set_option('display.max_columns',None)
file1.head(2)


# In[23]:


column_name_mapping = {
    'Sector Name': 'Sector',
    'SubSector Name': 'SubSector',
    'Organization Name' : 'Organization',
    'Operation Name':'Operation',
    'Average Hours Per Week':'Weekly Average Hours',
    'Total Floor Area':'Total Indoor Space_x',
    'Unit1':'Unit of Measure',
    'Annual Flow':'Annual Flow (M)',
    'Electricity':'Electricity_Quantity',
    'Unit2':'Electricity_Unit',
    'Natural Gas':'NaturalGas_Quantity',
    'Unit3':'NaturalGas_Unit',
    'Fuel Oil 1 & 2':'FuelOil12_Quantity',
    'Unit4':'FuelOil12_Unit',
    'Fuel Oil 4 & 6':'FuelOil46_Quantity',
    'Unit5':'FuelOil46_Unit',
    'Propane':'Propane_Quantity',
    'Unit6':'Propane_Unit',
    'Coal':'Coal_Quantity',
    'Unit7':'Coal_Unit',
    'Wood':'Wood_Quantity',
    'Unit8':'Wood_Unit',
    'District Heat':'DistrictHeating_Quantity',
    'Unit9':'DistrictHeating_Unit',
    'Renewable1':'DistrictHeating_IsRenewable',
    'Emission Factor1':'DistrictHeating_RenewableEmissionFactor',
    'District Cool':'DistrictCooling_Quantity',
    'Unit10':'DistrictCooling_Unit',
    'Renewable2':'DistrictCooling_IsRenewable',
    'Emission Factor2':'DistrictCooling_RenewableEmissionFactor',
    'GHG Emissions(Kg)':'GHG Emissions KG',
    
}


# In[24]:


file1 = file1.rename(columns=column_name_mapping)


# In[25]:


file1.columns


# In[26]:


column_name_mapping = {
    'Sector Name': 'Sector',
    'Sub Sector ': 'SubSector',
    'Organization Name' : 'Organization',
    'Operation Name':'Operation',
    'Average Hours per week':'Weekly Average Hours',
    'Total Floor Area ':'Total Indoor Space_x',
    'Unit':'Unit of Measure',
    'Annual Flow ':'Annual Flow (M)',
    'Electricity':'Electricity_Quantity',
    'Electricity Unit':'Electricity_Unit',
    'Natural Gas':'NaturalGas_Quantity',
    'Natural Gas2':'NaturalGas_Unit',
    'Fuel Oil 1 & 2':'FuelOil12_Quantity',
    'Fuel Oil 1 & 2 Unit':'FuelOil12_Unit',
    'Fuel Oil 4 &6':'FuelOil46_Quantity',
    'Fuel Oil 4 &6 Unit':'FuelOil46_Unit',
    'Propane':'Propane_Quantity',
    'Propane Unit':'Propane_Unit',
    'Coal Quantity':'Coal_Quantity',
    'Coal Unit':'Coal_Unit',
    'Wood':'Wood_Quantity',
    'Wood3':'Wood_Unit',
    'District Heating':'DistrictHeating_Quantity',
    'District Heating Unit':'DistrictHeating_Unit',
    'Renewable':'DistrictHeating_IsRenewable',
    'Renewable Emission Factor':'DistrictHeating_RenewableEmissionFactor',
    'District Cooling':'DistrictCooling_Quantity',
    'District Cooling Unit':'DistrictCooling_Unit',
    'District Cooling Renewable':'DistrictCooling_IsRenewable',
    'District Cooling Renewable Emission Factor':'DistrictCooling_RenewableEmissionFactor',
    'GHG Emissions(Kg)':'GHG Emissions KG',
    'Swimming Pools':'Swimming Pool'
}


# In[27]:


file2 = file2.rename(columns=column_name_mapping)


# In[28]:


file2.columns


# In[29]:


column_name_mapping = {'Annual Flow (M':'Annual Flow (M)','Sub Sector':'SubSector'}
file3 = file3.rename(columns=column_name_mapping)


# In[30]:


column_name_mapping = {'Annual Flow (M':'Annual Flow (M)','Sub Sector':'SubSector'}
file4 = file4.rename(columns=column_name_mapping)


# In[31]:


column_name_mapping = {'Annual Flow (M':'Annual Flow (M)','Sub Sector':'SubSector'}
file5 = file5.rename(columns=column_name_mapping)


# In[32]:


column_name_mapping = {'Annual Flow (M':'Annual Flow (M)','Sub Sector':'SubSector'}
file6 = file6.rename(columns=column_name_mapping)


# In[33]:


column_name_mapping = {'Annual Flow (M':'Annual Flow (M)','Sub Sector':'SubSector'}
file7 = file7.rename(columns=column_name_mapping)


# In[34]:


column_name_mapping = {'Annual Flow (M':'Annual Flow (M)','Sub Sector':'SubSector'}
file8 = file8.rename(columns=column_name_mapping)


# In[35]:


column_name_mapping = {'Annual Flow (M':'Annual Flow (M)','Sub Sector':'SubSector'}
file9 = file9.rename(columns=column_name_mapping)


# In[36]:


df = pd.concat([file1, file10,file9,file8,file7,file6,file5,file4,file3,file2], ignore_index=True)
pd.set_option('display.max_columns',None)
df


# DATA CLEANING

# In[37]:


df.isnull().sum()


# In[38]:


numeric_columns = df.select_dtypes(include=['float64']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

int_columns = df.select_dtypes(include=['int64']).columns
df[int_columns] = df[int_columns].fillna(df[int_columns].mean())

# categorical columns (using mode)
categorical_columns = df.select_dtypes(include=['object']).columns
df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])


# In[39]:


df.isnull().sum()


# Formating
# 

# In[40]:


df.dtypes


# In[41]:


df.head(2)


# In[42]:


df['Coal_Quantity'].value_counts()


# In[43]:


df['Swimming Pool'].describe()


# In[44]:


df['Coal_Quantity'] = pd.to_numeric(df['Coal_Quantity'], errors='coerce')


# In[45]:


df['Coal_Quantity'].dtypes


# In[46]:


df['DistrictHeating_IsRenewable'].value_counts()


# In[47]:


df['DistrictCooling_IsRenewable'].value_counts()


# In[48]:


df['DistrictHeating_IsRenewable'] = pd.to_numeric(df['DistrictHeating_IsRenewable'], errors='coerce')
df['DistrictCooling_IsRenewable'] = pd.to_numeric(df['DistrictCooling_IsRenewable'], errors='coerce')


# In[49]:


df['DistrictHeating_IsRenewable'].dtypes
df['DistrictCooling_IsRenewable'].dtypes


# TEXT ERRORS
# 

# In[50]:


object_data_cols = [var for var in df.columns if df[var].dtype == 'object']
object_data_cols


# In[51]:


df['Sector'].value_counts()


# In[52]:


df['Sector'] = df['Sector'].replace({
                                    'Post-secondary Educational Institution':'Post-Secondary Educational Institution',
                                    'Public Hospital':'Hospital',
                                    
                                            })


# In[53]:


df['SubSector'].value_counts()


# In[54]:


df['SubSector'] = df['SubSector'].replace({'Acute Hospital':'Acute/Chronic Hospital',
                                           'Chronic Hospital':'Acute/Chronic Hospital',
                                           'Acute/Chronic':'Acute/Chronic Hospital',
                                           'Acute':'Acute/Chronic Hospital',
                                           'Chronic':'Acute/Chronic Hospital',
                                           'University ':'University',
                                           'college':'College',
                                           'School Boards':'School Board',
                                           'Municipal':'Municipal Service Board',
                                           })


# In[55]:


df['Organization'].value_counts()


# In[58]:


df['Operation'].value_counts()


# In[59]:


df['Operation Type'].value_counts()


# In[60]:


df['Unit of Measure'].value_counts()


# In[61]:


df['Unit of Measure'] = df['Unit of Measure'].replace({'Sq Ft':'Square Feet',
                                                       'x':'Square Feet',
                                                       'Square feet':'Square Feet',
                                                       'square feet':'Square Feet',
                                                       'Square meters':'Square Meters',
                                                       'square meters':'Square Meters',
                                                       'mètres carrés':'Mètres carrés',
                                                       'Mètres carrés':'Metres Carres',
                                                       'pieds carrés':'Pieds carrés',
                                                       'Pieds carrés':'Pieds Carres'
                                           })


# In[62]:


df['Electricity_Unit'].value_counts()


# In[63]:


df['Electricity_Unit'] = df['Electricity_Unit'].replace({'kWh':'KWh',
                                                         'kwh':'KWh',
                                                         'x':'KWh'
                                                       
                                           })


# In[64]:


df['NaturalGas_Unit'].value_counts()


# In[65]:


df['NaturalGas_Unit'] = df['NaturalGas_Unit'].replace({'Cubic meter':'Cubic Meter',
                                                       'cubic meter':'Cubic Meter',
                                                       'mètre cube':'Cubic Meter',
                                                       'x':'ekWh',
                                                       'Litre':'ekWh',
                                                       'ekwh':'ekWh'
                                           })


# In[66]:


df['FuelOil12_Unit'].value_counts()


# In[67]:


df['FuelOil12_Unit'] = df['FuelOil12_Unit'].replace({'Litres':'Litre',
                                                         'litre':'Litre',})


# In[68]:


df['FuelOil46_Unit'].value_counts()


# In[69]:


df['Propane_Unit'].value_counts()


# In[70]:


df['Propane_Unit'] = df['Propane_Unit'].replace({
    125544.62: 'Litre',
    36052.69: 'Litre',
    123351.09: 'Litre',
    18181.02: 'Litre'})



# In[71]:


df['Coal_Unit'].value_counts()


# In[72]:


df['Coal_Unit'] = df['Coal_Unit'].replace({'Metric tonne':'Metric Tonne',
                                                         'Tonne métrique':'Metric Tonne',})


# In[73]:


df['Wood_Unit'].value_counts()


# In[74]:


df['Wood_Unit'] = df['Wood_Unit'].replace({'Metric tonne':'Metric Tonne',
                                                         'Tonne métrique':'Metric Tonne',})


# In[75]:


df['DistrictHeating_Unit'].value_counts()


# In[76]:


df['DistrictHeating_Unit'] = df['DistrictHeating_Unit'].replace({'Giga Joule - steam or hot water':'Giga Joule',
                                                       'Gigajoule - vapeur ou eau chaude':'Giga Joule',
                                                       'metric tonne - steam':'Metric Tonne',
                                                       'kilolitre - hot water':'kilolitre',
                                                       'KL Hot Water':'kilolitre', })


# In[77]:


df['DistrictCooling_Unit'].value_counts()


# In[78]:


df['DistrictCooling_Unit'] = df['DistrictCooling_Unit'].replace({'Giga Joule - chilled water':'Giga Joule',
                                                       'Gigajoule':'Giga Joule',
                                                       'kilolitre - chilled water':'kilolitre',
                                                       'KL Chilled Water':'kilolitre', })


# In[79]:


df['Swimming Pool'].value_counts()


# In[80]:


df['Swimming Pool'] = df['Swimming Pool'].replace({1.0:'Yes',
                                                       0.0:'non',
                                                       'S.O.':'Yes',
                                                        })


# In[81]:


df['Swimming Pool'].value_counts()


# CONVERT_CSV

# In[83]:


df.to_csv('C:/Users/Gayathri/OneDrive/Desktop/da cf/bps_data/final.csv')


# In[84]:


df=pd.read_csv('C:/Users/Gayathri/OneDrive/Desktop/da cf/bps_data/final.csv')
df


# In[ ]:




