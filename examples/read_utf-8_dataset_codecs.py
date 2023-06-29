import csv
import codecs
import pandas as pd
import os
import numpy as np
os.chdir('/home/mmm2050/QU_DFKI_Thesis/Experimentation/ASR_Accent_Analysis_De')
main_path=os.getcwd()

if not os.path.exists(main_path+'/Data_results'):
  os.makedirs(main_path+'/Data_results')

if not os.path.exists(main_path+'/Figures_results'):
  os.makedirs(main_path+'/Figures_results')

Data_path=main_path+'/Data/'



MCV_all=pd.DataFrame({})


df_at= pd.read_csv(Data_path+'test_at.txt',delimiter = ", ", header = None, names=['audio_filepath','transcript','duration'],engine='python' )
df_gb= pd.read_csv(Data_path+'test_gb.txt',delimiter = ", ", header = None, names=['audio_filepath','transcript','duration'],engine='python' )
df_it= pd.read_csv( Data_path+'test_it.txt',delimiter = ", ", header = None, names=['audio_filepath','transcript','duration'],engine='python' )
df_de_al= pd.read_csv(Data_path+'test_de_al.txt',delimiter = ", ", header = None, names=['audio_filepath','transcript','duration'],engine='python' )
df_fr= pd.read_csv(Data_path+'test_fr.txt',delimiter = ", ", header = None, names=['audio_filepath','transcript','duration'],engine='python' )
df_de_ni= pd.read_csv( Data_path+'test_de_ni.txt',delimiter = ", ", header = None, names=['audio_filepath','transcript','duration'],engine='python' )
df_ch= pd.read_csv(Data_path+'test_ch.txt',delimiter = ", ", header = None, names=['audio_filepath','transcript','duration'],engine='python' )
df_de= pd.read_csv(Data_path+'test_de.txt',delimiter = ", ", header = None, names=['audio_filepath','transcript','duration'],engine='python' )
df_us= pd.read_csv( Data_path+'test_us.txt',delimiter = ", ", header = None, names=['audio_filepath','transcript','duration'],engine='python' )
df_ca= pd.read_csv(Data_path+'test_ca.txt',delimiter = ", ", header = None, names=['audio_filepath','transcript','duration'],engine='python' )
df_ru= pd.read_csv(Data_path+'test_ru.txt',delimiter = ", ", header = None, names=['audio_filepath','transcript','duration'],engine='python' )
 
# combine the dataframes into a single one 
combined_df = pd.concat([df_at, df_gb, df_it, df_de_al, df_fr, df_de_ni, df_ch, df_de, df_us, df_ca, df_ru], ignore_index=True)

dataset_trans_test_all_duration=combined_df

dataset_trans_test_all_duration['audio_filepath'] = dataset_trans_test_all_duration['audio_filepath'].map(lambda x: x.split('.',6)[2])
dataset_trans_test_all_duration['audio_filepath'] = dataset_trans_test_all_duration['audio_filepath'].map(lambda x: x.split('/',6)[3])
dataset_trans_test_all_duration['transcript'] = dataset_trans_test_all_duration['transcript'].map(lambda x: x.split('": "',2)[1])
dataset_trans_test_all_duration['transcript'] = dataset_trans_test_all_duration['transcript'].map(lambda x: x.split('"',2)[0])
dataset_trans_test_all_duration['duration'] = dataset_trans_test_all_duration['duration'].map(lambda x: x.split('": ',2)[1])
dataset_trans_test_all_duration['duration'] = dataset_trans_test_all_duration['duration'].map(lambda x: x.split('}',2)[0])

 
 

# to read the UTF-8 Letters, Ä Ö Ü ß of the datasets via codecs library
for i, row in enumerate(dataset_trans_test_all_duration['transcript']):
  decoded_text = codecs.decode(row, 'unicode_escape') 
  dataset_trans_test_all_duration['transcript'][i] = np.where(dataset_trans_test_all_duration['transcript'][i] != np.NAN,decoded_text,'000' )

 
print('# ','*'*30,dataset_trans_test_all_duration )
# text = r"Was Du s\u00e4st, das wist Du ernten . \u00e4"

# decoded_text = codecs.decode(text, 'unicode_escape')
# print(decoded_text)

