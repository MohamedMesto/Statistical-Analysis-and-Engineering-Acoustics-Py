# Duration distribution of audiofiles per speaker's accent AT,CA, CH, DE_AL, DE_ni, DE, FR, GB, IT, RU, US. both as a plot and in terms of mean and variance.
import re # import the library of research about special value in String 
################################## Accent AT ###########################################
print('################################## Accent AT ###########################################')
# add Columns Names to the Dataset: header=None, names=['audio_filepath','text','duration']
dataset_test_at = pd.read_csv('test_at.txt', header=None, names=['audio_filepath','text','duration'])

'''
df['Numbers Only'] = df['Numbers and Text'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
'''

# extract the numeric values of the durations from the third Column and store it in a new column called duration(numeric)
dataset_test_at['duration(numeric)'] = dataset_test_at['duration'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
dataset_test_at['duration(numeric)'] =dataset_test_at['duration(numeric)'].div(10)
# extract the audio files ID values from the first Column and store it in a new column called audio_filepath(numeric)
#dataset_test_at['audio_filepath(numeric)'] = dataset_test_at['audio_filepath'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)

###########################################################################################
### How To Extract a SubString from a String In Column From the Left ==> .str[-12:-4]
dataset_test_at['audio_filepath(numeric)'] = dataset_test_at['audio_filepath'].str[-12:-4]

###dataset_test_at['audio_filepath(numeric)']=re.search('AAA(.+?)ZZZ', text)
print(dataset_test_at)

 
