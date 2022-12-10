
! cp /content/drive/test_at.txt /content/test_at.txt
dataset_test_at = pd.read_csv('test_at.txt', sep='\t')
print('*******************************************')
print(dataset_test_at)
print('*******************************************')
dataset_test_at.info()
print('*******************************************')



dataset_test_at['numeric'] = pd.read_csv('test_at.txt', sep='\t')

# extract the numeric values of the durations from the third Column and store it in a new column called 
dataset_test_at['numeric'] = dataset_test_at[' "duration": 4.9}'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
dataset_test_at
