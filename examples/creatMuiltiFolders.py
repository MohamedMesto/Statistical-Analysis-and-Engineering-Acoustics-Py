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
