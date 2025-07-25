# %%
d1={'kedar':78, 'jeevan': 11, 'john': 56,'abc':2}

# %%
l1=sorted(d1.keys())

# %%
l1

# %%
sort_d1={}
for i in l1:
    sort_d1[i]=d1[i]

# %%
sort_d1

# %%
sort_val={}

# %%
l2=sorted(d1.values())

# %%
l2

# %%
for i in l2:
    for key, value in d1.items():
        if value==i:
            sort_val[key]=i            

# %%
sort_val

# %%
d1={1:11,2:22,3:33}

# %%
d1_sum=sum(d1.keys())+sum(d1.values())

# %%
d1_sum

# %%
l1=[1,2,3,4,5,6,8]

# %%
per=f'{round(((sum(l1)/(len(l1)*100))*100),2)} %'

# %%
per

# %%
l1=[('pen',13),('pencil',10),('book',43),('chock',1)]

# %%
sort_l1=sorted(l1, key=lambda x:x[1])

# %%
sort_l1

# %%
import pandas as pd

# %%
df=pd.read_csv('Iris.csv')

# %%
df.shape

# %%
df.index

# %%
df.axes

# %%
df.columns

# %%
df.shape[0]

# %%
for i in df.columns:
    print(i)

# %%
df.info()

# %%
df.describe()

# %%
df[['SepalLengthCm','SepalWidthCm']][:4]

# %%
df.loc[4:10]

# %%
df.loc[4:10,['PetalWidthCm','SepalLengthCm']]

# %%
df[4:7]

# %%
df.iloc[4:10:2,::-1]

# %%
df.iloc[1,2]=56

# %%
df.size

# %%
df.shape

# %%
df.isnull().sum().sum()

# %%
df.isna().sum()

# %%
df.SepalLengthCm.max()

# %%
df

# %%
df.sort_index()

# %%
df2=df.set_index('SepalLengthCm')

# %%
df2.sort_index(axis=0)

# %%
df.SepalWidthCm.sort_values()

# %%
df.sort_values('SepalWidthCm')

# %%



