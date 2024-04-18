import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
# df2 = pd.read_csv('data-2.csv')
# refs = pd.read_csv('references.csv')

# df = pd.read_csv('data.csv', index_col='Column') # To Start With Column
# print(df.head()) # First Five Rows
# print(df.tail()) # Last Five Rows

# for c in df.columns:
    # print(c) # Print Columns

# id
# date
# First_name
# email

# c = list(df.columns) # Make List of Columns

# data_cols = [
#     'date',
#     'first_name',
#     'last_name',
#     'email',
#     ...
# ]

# Rearranging Columns
# df = df.reindex(columns=data_cols)

# Get The First 10 Rows
# print(df.head(10))

# Add Files To Each Other
# con_df = pd.concat([df, df2])

# Print The Length Of The Data Fram
# print(len(df.index))

# pivot = pd.pivot_table(con_df, index=['country', 'size'], values=['qty', 'price], aggfunc=np.sum)
# print(
    # size    qty 
    # 2XL     890
    # 3XL     818
    # L       895
    # M       ...
    # S       ...
    # XL      ...
    # XS      ...
# )

# Merge
# merged = con_df.merge(refs, how='left', on='id')

# Save Data On New File
# merged.to_csv('merged.csv')