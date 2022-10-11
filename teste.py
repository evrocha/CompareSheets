# Importing Libraries
import pandas as pd
import numpy as np
 
# data's stored in dictionary
details = {
    'Column1': [7, 2, 30, 4],
    'Column2': [7, 4, 25, 9],
    'Column3': [3, 8, 10, 30]
}
 
# creating a Dataframe object
df = pd.DataFrame(details)
 
# Where method to compare the values
# The values were stored in the new column
df['new'] = np.where((df['Column1'] <= df['Column2']) & (
    df['Column1'] <= df['Column3']), df['Column1'], np.nan)
 
# printing the dataframe
print(df)