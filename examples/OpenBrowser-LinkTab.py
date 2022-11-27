#open a Browser - Link and a Tab multiple times 


import os
import datetime
today = datetime.date.today()
print(today)

n=int(input('insert hte number of the iteration: '))
T=0
'''
we need to install selenium # by using  
pip install selenium
or 
C:\Python39\Scripts\pip.exe install selenium

'''
from selenium import webdriver
# Define the URL's we will open and a few other variables 
main_url = 'https://github.com/MohamedMesto' # URL A
tab_url = 'https://github.com/MohamedMesto/AWT-PJ-ss22-Video-Streaming-Mixer-Library-1' # URL B
chromedriver = 'DESCTINATION_TO_YOUR_CHROME_DRIVER'

# Open main window with URL A
browser= webdriver.Chrome(chromedriver)



for i in range(n):
    T=T+1
    if T>30 :
        # Open main window with URL A
        browser= webdriver.Chrome(chromedriver)
        T=0


    browser.get(main_url)
    print("Current Page Title is : %s" %browser.title)
    # Open a new window
    browser.execute_script("window.open('');")
    #Open a new window
    browser.execute_script("window.open('');")
    # Switch to the new window and open URL B
    browser.switch_to.window(browser.window_handles[1])
    browser.get(tab_url)
