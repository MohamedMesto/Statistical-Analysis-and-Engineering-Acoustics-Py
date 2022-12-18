# How to write a .py file from an existing python script?
#!python3

fname = 'dataset.py'
data = 11

with open(fname, 'w') as f:
    f.write('data = [{}]'.format(data))

    
### then
import dataset
print(dataset.data)

# will print 11
