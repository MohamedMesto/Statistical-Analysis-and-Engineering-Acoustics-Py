############################## for loop#######################################
list_dataset_test_=['at','ca','ch','de_al','de_ni','de','fr','gb','it','ru','us']


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#from compare_df import * # import compare-df Function

############################# 1- reading the dataset ##########################################################
dataset_validated_tsv = pd.read_csv('validated.tsv', sep='\t')

#################################Extract and calculate the duration_numeric########################################
# add Columns Names to the Dataset: header=None, names=['audio_filepath','text','duration']
# dataset_test_ca = pd.read_csv('test_ca.txt', header=None, names=['audio_filepath','text','duration'])
'''
df['Numbers Only'] = df['Numbers and Text'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
'''

for i in list_dataset_test_:
  # accent=i
  # dataset_accent=f'dataset_test_{i}'
  # textfile_name=f'test_{i}.txt'
  dataset_test_ca = pd.read_csv(f'test_{i}.txt', header=None, names=['audio_filepath','text','duration'])
  
  # dataset_test_ca=f'dataset_test_{i}'
  # extract the numeric values of the durations from the third Column and store it in a new column called
  dataset_test_ca['duration_numeric'] = dataset_test_ca['duration'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
  dataset_test_ca['duration_numeric'] =dataset_test_ca['duration_numeric'].div(10)
  # extract the numeric values of the durations from the third Column and store it in a new column called 
  #dataset_test_ca['audio_filepath_numeric'] = dataset_test_ca['audio_filepath'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)

  dataset_test_ca['audio_filepath_numeric'] = dataset_test_ca['audio_filepath'].str[-13:-5]
  print(dataset_test_ca)
  print('################################## Gender ###########################################')
  
