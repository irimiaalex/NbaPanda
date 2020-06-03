import pandas as pd
import re
import numpy as np


df=pd.read_csv('all_seasons.csv')


df['draft_yr_num']=df['draft_year']+',' + df['draft_number']
df['eff']=df['pts']+df['ast']+df['reb']
df['overall']=np.where(df['eff']>=20, 'star', 'bust')


new_df=df[['player_name', 'draft_yr_num', 'eff', 'overall']]

print(new_df.sort_values('eff', ascending=False))


df2010=new_df[new_df['draft_yr_num'].str.contains('2010')]
df2011=new_df[new_df['draft_yr_num'].str.contains('2011')]
df2012=new_df[new_df['draft_yr_num'].str.contains('2012')]
df2013=new_df[new_df['draft_yr_num'].str.contains('2013')]
df2014=new_df[new_df['draft_yr_num'].str.contains('2014')]
df2015=new_df[new_df['draft_yr_num'].str.contains('2015')]
df2016=new_df[new_df['draft_yr_num'].str.contains('2016')]
df2017=new_df[new_df['draft_yr_num'].str.contains('2017')]
df2018=new_df[new_df['draft_yr_num'].str.contains('2018')]
df2019=new_df[new_df['draft_yr_num'].str.contains('2019')]

lst=[df2010,df2011,df2012,df2013,df2014,df2015,df2016,df2017,df2018,df2019]

season=2010
for filename in lst:
    filename.to_csv(str(season))
    season+=1


print(df2015.head(5))










#print([df[df['college'].str.contains(str(c), flags=re.I, regex=True)].sort_values('pts', ascending=False).head(10)])
