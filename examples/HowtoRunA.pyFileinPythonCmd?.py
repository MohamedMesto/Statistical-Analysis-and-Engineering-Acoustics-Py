How to run a.py file in python cmd?
3 methods

# after imporitng the file
import file 
# First method
execfile('file.py')
# Second method
exec(open("dataset_accent.py").read())
# Third method
import subprocess
import sys

subprocess.check_call([sys.executable, 'file.py'])
