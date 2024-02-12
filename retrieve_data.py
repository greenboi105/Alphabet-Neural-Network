import pandas as pd 

data = pd.read_csv('https://static.bc-edx.com/data/dl-1-2/m21/lms/starter/charity_data.csv')

data.to_csv('alphabet_data.csv', index=False)