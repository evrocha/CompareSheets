# Importing Libraries
import pandas as pd
import numpy as np
 
# data's stored in dictionary
details = {
    'Column1': [7, 2, 30, 4],
    'Column2': [7, 4, 25, 9],
    
}
others = {
    'Column1': [2,2,3,1],
    'Column2': [2,2,3,1,0,0,0]
    
}
# creating a Dataframe object
df = pd.DataFrame(details)
df = df.reset_index()
df2 = pd.DataFrame(others)
df2 = df.reset_index()

df_diff = pd.merge(df, df2, how = 'outer', indicator='exist')
# Where method to compare the values
# The values were stored in the new column
# a = [1, 3, 4]
# b = [2, 3, 2]

df['new'] = np.where((df['Column1'] != df2['Column1']), df['Column1'], np.nan)
print(df)


# df['new2'] = np.where((df['Column1'] == df['Column2']), df['Column1'], np.nan)
# printing the dataframe
# print(df)