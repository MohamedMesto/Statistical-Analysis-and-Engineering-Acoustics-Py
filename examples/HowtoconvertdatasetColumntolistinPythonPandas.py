

#,y="speaker's accent",x="Duration distribution"
import re # import the library of research about special value in String 
# add Columns Names to the Dataset: header=None, names=['audio_filepath','text','duration']
dataset_test_at = pd.read_csv('test_at.txt', header=None, names=['audio_filepath','text','duration'])
'''
df['Numbers Only'] = df['Numbers and Text'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
'''
# extract the numeric values of the durations from the third Column and store it in a new column called
dataset_test_at['duration(numeric)'] = dataset_test_at['duration'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
dataset_test_at['duration(numeric)'] =dataset_test_at['duration(numeric)'].div(10)
# extract the numeric values of the durations from the third Column and store it in a new column called 
#dataset_test_at['audio_filepath(numeric)'] = dataset_test_at['audio_filepath'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)

dataset_test_at['audio_filepath(numeric)'] = dataset_test_at['audio_filepath'].str[103:111]

###dataset_test_at['audio_filepath(numeric)']=re.search('AAA(.+?)ZZZ', text)
dataset_test_at



 

#############################
# convert the column duration(numeric) to a list
duriationdistribution_y = dataset_test_at['duration(numeric)'].tolist()
print(duriationdistribution_y)
