# How to Compare Values between two Pandas DataFrames
import pandas as pd

data_1 = {'product_1': ['computer','monitor','printer','desk'],
                   'price_1': [1200,800,200,350]
                   }
df1 = pd.DataFrame(data_1)
print(df1)

data_2 = {'product_2': ['computer','monitor','printer','desk'],
                    'price_2': [900,800,300,350]
                    }
df2 = pd.DataFrame(data_2)
print (df2)

# df1['new column that will contain the comparison results'] = np.where(condition,'value if true','value if false')
# df1['prices_match'] = np.where(df1['price_1'] == df2['price_2'], 'True', 'False')
########################################################
mport pandas as pd
import numpy as np

data_1 = {'product_1': ['computer','monitor','printer','desk'],
                   'price_1': [1200,800,200,350]
                   }
df1 = pd.DataFrame(data_1)


data_2 = {'product_2': ['computer','monitor','printer','desk'],
                    'price_2': [900,800,300,350]
                    }
df2 = pd.DataFrame(data_2)


df1['price_2'] = df2['price_2'] #add the price_2 column from df2 to df1
df1['prices_match'] = np.where(df1['price_1'] == df2['price_2'], 'True', 'False') #create a new column in df1 to check if prices match

print(df1)
