import pandas as pd

data_list = [[1, 2, 3], [1, 5, 4], [3, 7, 9], [6, 8, 5]]
df = pd.DataFrame(data_list, columns=['C', 'B', 'D'])
df.index = ['X', 'Z', 'Y', 'V']
print(df)
df_sort_axis0 = df.sort_index()
print('data after sort_index:')
print(df_sort_axis0)
df_sort_axis1 = df.sort_index(axis=1)
print('data after sort_index(axis = 1):')
print(df_sort_axis1)
df_data_order0 = df.sort_values(by=['D'], ascending=[True])
print('data after sort_values sorted by D:')
print(df_data_order0)
