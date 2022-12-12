# Duration distribution of audiofiles per speaker's accent AT,CA, CH, DE_AL, DE_ni, DE, FR, GB, IT, RU, US. both as a plot and in terms of mean and variance.
import re # import the library of research about special value in String 
################################## Accent AT ###########################################
print('################################## Accent AT ###########################################')
# add Columns Names to the Dataset: header=None, names=['audio_filepath','text','duration']
dataset_test_at = pd.read_csv('test_at.txt', header=None, names=['audio_filepath','text','duration'])


###########################################################################################
### How To Extract a SubString from a String In Column From the Left ==> .str[-12:-4]
dataset_test_at['audio_filepath(numeric)'] = dataset_test_at['audio_filepath'].str[-12:-4]

print(dataset_test_at)

 
