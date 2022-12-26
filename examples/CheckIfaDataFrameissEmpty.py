dataset_validated_tsv = pd.read_csv('validated.tsv', sep='\t',low_memory=False)

dataset_validated_tsv.drop(dataset_validated_tsv[(dataset_validated_tsv['gender'] != 'female') | (dataset_validated_tsv['gender'].isna())| 
  (dataset_validated_tsv['accents'].isna())| (dataset_validated_tsv['accents']!='Alemannische Färbung,Schweizer Standart Deutsch')].index, inplace=True)
dataset_validated_tsv.count()
dataset_validated_tsv
if dataset_validated_tsv.empty:
  print('datafrme is empty')
else:
  print('datafrme is not empty')
  
  
  
  #### Or
  
  if not dataset_validated_tsv.empty:
  print('datafrme is not empty')
else:
  print('datafrme is empty')
