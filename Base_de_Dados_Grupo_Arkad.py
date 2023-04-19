#!/usr/bin/env python
# coding: utf-8

# In[2]:


from futpythontrader import *


# In[3]:


key = 'a535168594f7c33f403cbd0c07c3b61d37105c253cd887672147bee92709a3b3'


# In[4]:


url = "https://api.football-data-api.com/league-list?key="+key+"&chosen_leagues_only=true"

data1 = requests.get(url)
resp = data1.json()
resp = data1.json()['data']
dados = pd.DataFrame.from_dict(resp)
dados = dados.sort_values(['name'])
dados = drop_reset_index(dados)


# In[5]:


dados.to_excel("ligas.xlsx", encoding='utf-8', index=False)
df = pd.read_excel('ligas.xlsx')
new_df = {'league':[],'id':[],'season':[]}
for row in df.itertuples():
    for i in eval(row.season):
        new_df['league'].append(row.name)
        new_df['id'].append(i['id'])
        new_df['season'].append(i['year'])
new = pd.DataFrame(new_df)
new.columns = ['League', 'ID', 'Season']
new = drop_reset_index(new)
new.to_excel('ligas_arkard.xlsx', index=False)


# In[6]:


flt = ((new.Season == 2022) | (new.Season == 2023) | (new.Season == 20212022) | (new.Season == 20222023))
new2 = new[flt]
new2 = drop_reset_index(new2)
new2["Season"] = new2["Season"].astype('str')
new2["ID"] = new2["ID"].astype('str')


# In[7]:


for i,j,k in zip(new2.League, new2.ID, new2.Season):
    
    liga = str(i)
    ID = str(j)
    year = str(k)
    
    url = f"https://api.football-data-api.com/league-matches?key={key}&season_id={ID}"
    data = requests.get(url)
    resp = data.json()
    resp = data.json()['data']
    df = pd.DataFrame.from_dict(resp)
    df['League'] = liga
    df = df[['id','League','season','status','date_unix','game_week','home_name','away_name','homeGoalCount','awayGoalCount','odds_ft_1','odds_ft_x','odds_ft_2','odds_ft_over05','odds_ft_under05','odds_ft_over15','odds_ft_under15','odds_ft_over25','odds_ft_under25','odds_ft_over35','odds_ft_under35','odds_ft_over45','odds_ft_under45','odds_btts_yes','odds_btts_no']]
    df.columns = ['Id_Jogo','League','Season','Status','Date','Rodada','Home','Away','FT_Goals_H','FT_Goals_A','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over05','FT_Odd_Under05','FT_Odd_Over15','FT_Odd_Under15','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_Over35','FT_Odd_Under35','FT_Odd_Over45','FT_Odd_Under45','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No']
    df.fillna(0, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'], unit='s') - pd.DateOffset(hours=3)
    df = df.sort_values(['Date'])
    flt = df.Status == 'complete'
    df = df[flt]
    
    df = df[['Id_Jogo','League','Season','Date','Rodada','Home','Away','FT_Goals_H','FT_Goals_A','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over05','FT_Odd_Under05','FT_Odd_Over15','FT_Odd_Under15','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_Over35','FT_Odd_Under35','FT_Odd_Over45','FT_Odd_Under45','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No']]
    
    df.to_csv(f'./Bases_de_Dados/{liga}_{year}.csv',index=False)
    print(liga,'-',year)


# In[8]:


# Executar quando aparecer ligas novas




# for a,b in zip(new2.ID,new2.League):
#     print("df_jogos.replace("+a+",'"+b+"', inplace=True)")


# In[9]:


# for i,j,k in zip(new2.League, new2.ID, new2.Season):
#     print('if liga == "'+i+'":')
#     print('    df1 = pd.read_csv("./Bases/'+i+'_'+k+'.csv?raw=true")')
#     print('    df = pd.concat([df1,df2])')

