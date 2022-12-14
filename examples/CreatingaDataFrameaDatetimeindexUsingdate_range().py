# Creating a DataFrame by passing a NumPy array, with a datetime index using date_range() and labeled columns:

dates = pd.date_range("20130101", periods=6)
dates
'''
Out[6]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
'''





# https://pandas.pydata.org/docs/user_guide/10min.html
