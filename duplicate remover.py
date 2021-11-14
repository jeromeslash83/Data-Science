import pandas as pd

item = pd.read_csv('addfile here')

item.drop_duplicates(subset='')

item.to_csv('s')
