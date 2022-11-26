import os
import datetime
today = datetime.date.today()
print(today)
# to creat a n number of folders in the current work directory
n=int(input('the Numbers of the Folders/Files'))
pathname = 1
directory = "os.getcwd()" + str(pathname)

while pathname < n:
    if not os.path.exists(directory):
        os.makedirs(directory)
    pathname += 1  
    directory = "os.getcwd()" + str(pathname)
    
# or other exp
'''
for i in range(1000):
    dir = os.path.join('C:/Test', *f"{i:09d}")
    os.makedirs(dir)
'''
####################
'''
import os
for year in range(1922, 2011):
    os.mkdir("\\{}".format(year))
    '''
