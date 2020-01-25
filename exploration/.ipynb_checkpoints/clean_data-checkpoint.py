#%%
import pandas as pd
import numpy as np

# Layout of the columns
layout_df = pd.read_csv('/Users/thomas.farrandibm.com/Documents/GitHub/vietnam_air_records/data/CACTA.TR.LAY.6570', delimiter='\t')
layout_df

#%%
layout_df.reset_index(inplace=True)
layout_df.drop(columns='level_1', inplace=True)
layout_df

#%%
rows_list = []
for index, row in layout_df.iterrows():
    no_na_row = row.dropna()
    no_na_row.index = ['COLUMN NAME', 'TITLE/DESCRIPTION', 'DATA TYPE', 'START', 'END', 'WIDTH']
    rows_list.append(no_na_row)

new_layout_df = pd.DataFrame([row for row in rows_list])
new_layout_df

#%%
# Data dataframe
df = pd.read_csv('/Users/thomas.farrandibm.com/Documents/GitHub/vietnam_air_records/data/CACTA.TR.6510')
df

#%%
series_list = []
for index, row in df.iterrows():
    print(index, len(df))
    split_row = []
    for ind, split in new_layout_df['END'].iteritems():
        
        if ind == 0:
            lower_split = 0
        else:
            lower_split = new_layout_df['END'][ind - 1]
        
        parsed_str = row[0][int(lower_split):int(split)]
        split_row.append(parsed_str)
    row_series = pd.Series(split_row, index=new_layout_df['TITLE/DESCRIPTION'])
    series_list.append(row_series)


#%%
series_list[0]


#%%
df_f = pd.concat([series for series in series_list], axis=1)

#%%
df_f = df_f.transpose()
df_f

#%%
df_f.to_csv('clean_data/initial_clean_data.csv')


#%%
# Checking that the split has been performed correctly



#%%
print(split)

#%%
data_row = df.iloc[0]

#%%
data_row[0][:10]

#%%
layout_df.reset_index(inplace=True)

#%%
new_layout_df = pd.DataFrame()
for index, row in layout_df.iterrows():
    row.dropna(inplace=True)
    new_layout_df.append(row)


layout_df

#%%
layout_df.dropna(axis=1)

#%%
# Removing white space from the columns
layout_df.columns = layout_df.columns.str.strip()

#%%
layout_df['END'][]

