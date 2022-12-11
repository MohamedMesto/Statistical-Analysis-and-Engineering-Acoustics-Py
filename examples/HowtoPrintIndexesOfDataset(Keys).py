# How to Print the indexes of the dataset (Keys)
# Reading the dataset
dataset_test_at = pd.read_csv('test_at.txt', sep='\t')

# to avoid reading the NaN data of the column_name column
dataset_test_at.drop(dataset_test_at[(dataset_test_at['column_name'].isna())].index, inplace=True)


# to Print the indexes of the dataset (Keys)
dataset_test_at.keys()
