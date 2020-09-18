import pandas as pd
from datetime import datetime

df = pd.read_excel(r'C:\Users\ct\Downloads\test.xlsx')
# ddd = df['第二时间']
# print(ddd.head(5))
pre = [str(i) for i in df['第一时间']]
aft = [str(aa) for aa in df['第二时间']]
Date_Diff = []
for ppp, aaa in zip(pre, aft):
    # print(ppp, aaa)
    ppp = datetime.strptime(ppp, '%Y%m%d')
    aaa = datetime.strptime(aaa, '%Y%m%d')
    diff = aaa - ppp
    Date_Diff.append(diff.days)
print(Date_Diff)
df['日期差值'] = Date_Diff
df['日期差值'].to_excel(r'C:\Users\ct\Downloads\t.xlsx'
                    , header=None
                    , index=None)
