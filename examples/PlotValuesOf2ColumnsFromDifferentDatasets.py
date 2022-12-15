# How to Compare Values between two Pandas DataFrames
#####################################################

# Plot Values Of 2 Columns From Different Datasets 
##########################################################################
import pandas as pd
import numpy as np
data_1 = {'product_1': ['computer','monitor','printer','desk'],
                   'audio_filepath_numeric': [1200,800,200,350],'duration_numeric':[4.9,10.1,9.0,3.7]
                   }
df1 = pd.DataFrame(data_1)

print('*********************print Contents of (df1)**********************')
print(df1)

data_2 = {'product_2': ['computer','monitor','printer','desk'],
                    'path_numeric': [1200,800,300,150],'gender': ['male','female','female','male']
                    }
df2 = pd.DataFrame(data_2)


print('*********************print Contents of (df2)**********************')
print(df2)
# df1['new column that will contain the comparison results'] = np.where(condition,'value if true','value if false')
# df1['path_match'] = np.where(df1['audio_filepath_numeric'] == df2['path_numeric'], 'True', 'False')
########################################################

df1['path_numeric'] = df2['path_numeric'] #add the path_numeric column from df2 to df1
df1['path_match'] = np.where(df1['audio_filepath_numeric'] == df2['path_numeric'], 'True', 'False') #create a new column in df1 to check if prices match
print('*********************print Contents of df1.info()**********************')

print(df1.info())
print('*********************print Contents of path_match**********************')

print(df1)


#df1['path_match']=df1.drop(df1[(df1['path_match'].isna())].index, inplace=True)

print('*********************print Contents of gender_from_df2**********************')

 
df1['gender_from_df2'] = np.where(df1['audio_filepath_numeric'] == df2['path_numeric'], df2['gender'],'No_path_match') #create a new column in df1 for path diff

print(df1)
print('*********************print Contents of search**********************')

#print(df1[df1["path_match_ID"].map(lambda path_match: "True" in path_match)])
# Plot Values Of 2 Columns From Different Datasets 
plt.xlabel("gender_from_df2")
plt.ylabel("duration_numeric")
plt.plot(df1['gender_from_df2'],df1['duration_numeric'], lw=1, ms=20)

# #kurvenname = ['blau', 'orange', 'grün', 'rot', 'lila']
# #plt.grid(True)
plt.show()
