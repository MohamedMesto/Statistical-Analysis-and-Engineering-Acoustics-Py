####################################Insert Accent Loop##################################################
# def MeanCal(DatasetName):
#   return np.mean(DatasetName)
 

print('################################## Accent Mean ###########################################')
list_dataset_test_=['at','ca','ch','de_al','de_ni','de','fr','gb','it','ru','us']
dataset_dataset_test_=pd.DataFrame(list_dataset_test_, columns=['all_accent']) 

dataset_name="dataset_test_"
dataset_column="['duration_numeric']"

dataset_all_accent=[] # create a dataset called "dataset_all_accent" required column of mean calculations of all Accents
list_all_accent_cal=[] # list of the results of mean calculations of all accents
list_all_accent=[]
list_all_accent_mean=[] # create a dataset called "list_all_accent_mean" contains the mean calculations of all Accents
for i in range(len(list_dataset_test_)):
  
  Accent_Values=dataset_test_[i]
  Accent_type=dataset_name+Accent_Values+dataset_column
  ###list_all_accent_cal.insert(i,5+i)
  #list_all_accent_cal[i]=np.mean(dataset_test_at['duration_numeric'])
  ###print(f' \'np.mean({Accent_type}\'),')
  temp_list=f' {Accent_type}'
  temp_mean_list=f' np.mean({Accent_type})'

  

  #list_all_accent_cal.insert(i,np.mean(temp_list))

  print(f'np.mean({Accent_type})')
  # create a dataset called "list_all_accent_mean" contains the mean calculations for all Accents
  ###dataset_all_accent.insert(i,Accent_type)
  list_all_accent.insert(i,temp_list)
  list_all_accent_mean.insert(i,temp_mean_list)
  
# print('#'*60,'dataset_all_accent')
# print(dataset_all_accent,'\n')

print('#'*30,'list_all_accent=','#'*30)
#print(f'{list_all_accent}',sep=os.linesep)
print(f'  {list_all_accent}','\n')


print('#'*30,'list_all_accent_mean=','#'*30)
#print(f'{list_all_accent_mean}',sep=os.linesep)
print(f'  {list_all_accent_mean}','\n')

print('#'*30,'list_all_accent_cal=','#'*30)
print(f'  {list_all_accent_cal}','\n')


 
########################################################################

dataset_all_accent= pd.DataFrame (list_all_accent, columns = ['all_accent'])
dataset_all_accent_mean = pd.DataFrame (list_all_accent_mean, columns = ['mean_of_all_accent'])
# dataset_all_accent_mean['Column'] = df['Column'].apply(ast.literal_eval)
dataset_all_accent_mean
# dataset_all_accent_mean.mean_of_all_accent[0]


list_dataset_test_=['at','ca','ch','de_al','de_ni','de','fr','gb','it','ru','us','stop']
list1=['']
Accent_=0
print('#'*60,'Insert Accent Loop','#'*60)
for j in list_dataset_test_:
  # print(j)
  onetime=0
  
  for i in range(0,11):
    #print(i)
    # print(onetime)
    if j!='stop':
      print(f'Accent_{j}={dataset_all_accent_mean.mean_of_all_accent[i]}')
      stopcal=i+1
      j=list_dataset_test_[stopcal]
  if j=='stop':
    break   #######           <<<<<<<<====================
  print('#'*60,{j},{i},'#'*60)
