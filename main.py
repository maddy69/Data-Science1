import pandas as pd
import glob
import os

import pandas as pd

df1 = pd.read_csv('customer_data_one.csv')
df2 = pd.read_csv('customer_data_two.csv')
out = df1.append(df2)
print(out)

with open(r'C:\Users\madha\SocioGraph\customer_data_merged.csv', 'w', encoding='utf-8') as f:
    out.to_csv(f, index=False)


