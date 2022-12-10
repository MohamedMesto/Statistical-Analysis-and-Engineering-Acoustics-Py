# copy the TSV file/Dataset test_at.txt
! cp /content/drive/MyDrivetest_at.txt /content/test_at.txt

# read the TSV file/Dataset test_at.txt
# Duration distribution of audiofiles per speaker's accent

#   dataset_test_at = pd.read_csv('test_at.txt', sep='\t')
#   print('*******************************************')
#   print(dataset_test_at)
#   print('*******************************************')
#   dataset_test_at.info()
#   print('*******************************************')
#   print('*********************indexes**********************')
 

print('*******************************************')
dataset_test_at = pd.read_csv('test_at.txt')
print('*******************************************')
print(dataset_test_at)
print('*******************************************')
dataset_test_at.info()
print('*******************************************')
print('*********************indexes**********************')

# columns --> Labels
# rows ==> Contents

for label, content in dataset_test_at.items():
    print(f'label: {label}')
    print(f'content: {content}', sep='\n')
