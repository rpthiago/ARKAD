#!/usr/bin/env python
# coding: utf-8

# In[1]:


from futpythontrader import *


# In[2]:


key = 'a535168594f7c33f403cbd0c07c3b61d37105c253cd887672147bee92709a3b3'


# In[3]:


url1 = f"https://api.football-data-api.com/todays-matches?key={key}&date={ontem()}"
data1 = requests.get(url1)
resp1 = data1.json()
resp1 = data1.json()['data']
df1 = pd.DataFrame.from_dict(resp1)

url2 = f"https://api.football-data-api.com/todays-matches?key={key}&date={hoje()}"
data2 = requests.get(url2)
resp2 = data2.json()
resp2 = data2.json()['data']
df2 = pd.DataFrame.from_dict(resp2)

url3 = f"https://api.football-data-api.com/todays-matches?key={key}&date={amanha()}"
data3 = requests.get(url3)
resp3 = data3.json()
resp3 = data3.json()['data']
df3 = pd.DataFrame.from_dict(resp3)

df_jogos = pd.concat([df1,df2,df3])

df_jogos = df_jogos[['competition_id','date_unix','game_week','home_name','away_name','odds_ft_1','odds_ft_x','odds_ft_2','odds_ft_over05','odds_ft_under05','odds_ft_over15','odds_ft_under15','odds_ft_over25','odds_ft_under25','odds_ft_over35','odds_ft_under35','odds_ft_over45','odds_ft_under45','odds_btts_yes','odds_btts_no']]
df_jogos.columns = ['League','Data','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over05','FT_Odd_Under05','FT_Odd_Over15','FT_Odd_Under15','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_Over35','FT_Odd_Under35','FT_Odd_Over45','FT_Odd_Under45','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No']

df_jogos.replace(7032,'Argentina Prim B Nacional', inplace=True)
df_jogos.replace(8836,'Argentina Prim B Nacional', inplace=True)
df_jogos.replace(7892,'Argentina Primera División', inplace=True)
df_jogos.replace(8595,'Argentina Primera División', inplace=True)
df_jogos.replace(6639,'Australia A-League', inplace=True)
df_jogos.replace(8008,'Australia A-League', inplace=True)
df_jogos.replace(6008,'Austria Bundesliga', inplace=True)
df_jogos.replace(7890,'Austria Bundesliga', inplace=True)
df_jogos.replace(6079,'Belgium Pro League', inplace=True)
df_jogos.replace(7544,'Belgium Pro League', inplace=True)
df_jogos.replace(7033,'Bolivia LFPB', inplace=True)
df_jogos.replace(8926,'Bolivia LFPB', inplace=True)
df_jogos.replace(7097,'Brazil Serie A', inplace=True)
df_jogos.replace(9035,'Brazil Serie A', inplace=True)
df_jogos.replace(7107,'Brazil Serie B', inplace=True)
df_jogos.replace(9042,'Brazil Serie B', inplace=True)
df_jogos.replace(7109,'Brazil Serie C', inplace=True)
df_jogos.replace(9087,'Brazil Serie C', inplace=True)
df_jogos.replace(7093,'Brazil Serie D', inplace=True)
df_jogos.replace(9086,'Brazil Serie D', inplace=True)
df_jogos.replace(6012,'Bulgaria First League', inplace=True)
df_jogos.replace(7483,'Bulgaria First League', inplace=True)
df_jogos.replace(7112,'Canada Canadian Premier League', inplace=True)
df_jogos.replace(8946,'Canada Canadian Premier League', inplace=True)
df_jogos.replace(7114,'Chile Primera B', inplace=True)
df_jogos.replace(8875,'Chile Primera B', inplace=True)
df_jogos.replace(7036,'Chile Primera División', inplace=True)
df_jogos.replace(8833,'Chile Primera División', inplace=True)
df_jogos.replace(7257,'Chile Segunda División', inplace=True)
df_jogos.replace(9040,'Chile Segunda División', inplace=True)
df_jogos.replace(7356,'China Chinese Super League', inplace=True)
df_jogos.replace(6905,'Colombia Categoria Primera A', inplace=True)
df_jogos.replace(8936,'Colombia Categoria Primera A', inplace=True)
df_jogos.replace(6908,'Colombia Categoria Primera B', inplace=True)
df_jogos.replace(8897,'Colombia Categoria Primera B', inplace=True)
df_jogos.replace(5956,'Croatia Prva HNL', inplace=True)
df_jogos.replace(7457,'Croatia Prva HNL', inplace=True)
df_jogos.replace(5938,'Czech Republic First League', inplace=True)
df_jogos.replace(7586,'Czech Republic First League', inplace=True)
df_jogos.replace(5959,'Denmark 1st Division', inplace=True)
df_jogos.replace(7450,'Denmark 1st Division', inplace=True)
df_jogos.replace(5961,'Denmark Superliga', inplace=True)
df_jogos.replace(7426,'Denmark Superliga', inplace=True)
df_jogos.replace(7038,'Ecuador Primera Categoría Serie A', inplace=True)
df_jogos.replace(8934,'Ecuador Primera Categoría Serie A', inplace=True)
df_jogos.replace(6752,'Egypt Egyptian Premier League', inplace=True)
df_jogos.replace(8520,'Egypt Egyptian Premier League', inplace=True)
df_jogos.replace(6089,'England Championship', inplace=True)
df_jogos.replace(7593,'England Championship', inplace=True)
df_jogos.replace(6017,'England EFL League One', inplace=True)
df_jogos.replace(7570,'England EFL League One', inplace=True)
df_jogos.replace(6015,'England EFL League Two', inplace=True)
df_jogos.replace(7574,'England EFL League Two', inplace=True)
df_jogos.replace(6088,'England National League', inplace=True)
df_jogos.replace(7729,'England National League', inplace=True)
df_jogos.replace(6135,'England Premier League', inplace=True)
df_jogos.replace(7704,'England Premier League', inplace=True)
df_jogos.replace(7120,'Finland Veikkausliiga', inplace=True)
df_jogos.replace(8935,'Finland Veikkausliiga', inplace=True)
df_jogos.replace(6019,'France Ligue 1', inplace=True)
df_jogos.replace(7500,'France Ligue 1', inplace=True)
df_jogos.replace(6018,'France Ligue 2', inplace=True)
df_jogos.replace(7501,'France Ligue 2', inplace=True)
df_jogos.replace(6020,'Germany 2. Bundesliga', inplace=True)
df_jogos.replace(7499,'Germany 2. Bundesliga', inplace=True)
df_jogos.replace(6192,'Germany Bundesliga', inplace=True)
df_jogos.replace(7664,'Germany Bundesliga', inplace=True)
df_jogos.replace(6282,'Greece Super League', inplace=True)
df_jogos.replace(7954,'Greece Super League', inplace=True)
df_jogos.replace(5936,'Hungary NB I', inplace=True)
df_jogos.replace(7967,'Hungary NB I', inplace=True)
df_jogos.replace(6198,'Italy Serie A', inplace=True)
df_jogos.replace(7608,'Italy Serie A', inplace=True)
df_jogos.replace(6205,'Italy Serie B', inplace=True)
df_jogos.replace(7864,'Italy Serie B', inplace=True)
df_jogos.replace(6935,'Japan J1 League', inplace=True)
df_jogos.replace(8810,'Japan J1 League', inplace=True)
df_jogos.replace(6936,'Japan J2 League', inplace=True)
df_jogos.replace(8811,'Japan J2 League', inplace=True)
df_jogos.replace(6104,'Mexico Ascenso MX', inplace=True)
df_jogos.replace(7489,'Mexico Ascenso MX', inplace=True)
df_jogos.replace(6038,'Mexico Liga MX', inplace=True)
df_jogos.replace(7425,'Mexico Liga MX', inplace=True)
df_jogos.replace(5950,'Netherlands Eerste Divisie', inplace=True)
df_jogos.replace(7484,'Netherlands Eerste Divisie', inplace=True)
df_jogos.replace(5951,'Netherlands Eredivisie', inplace=True)
df_jogos.replace(7482,'Netherlands Eredivisie', inplace=True)
df_jogos.replace(6098,'Netherlands Tweede Divisie', inplace=True)
df_jogos.replace(7702,'Netherlands Tweede Divisie', inplace=True)
df_jogos.replace(7048,'Norway Eliteserien', inplace=True)
df_jogos.replace(8739,'Norway Eliteserien', inplace=True)
df_jogos.replace(6960,'Paraguay Division Profesional', inplace=True)
df_jogos.replace(8783,'Paraguay Division Profesional', inplace=True)
df_jogos.replace(6966,'Peru Primera División', inplace=True)
df_jogos.replace(8837,'Peru Primera División', inplace=True)
df_jogos.replace(5948,'Poland Ekstraklasa', inplace=True)
df_jogos.replace(7428,'Poland Ekstraklasa', inplace=True)
df_jogos.replace(6117,'Portugal Liga NOS', inplace=True)
df_jogos.replace(7731,'Portugal Liga NOS', inplace=True)
df_jogos.replace(6116,'Portugal LigaPro', inplace=True)
df_jogos.replace(7732,'Portugal LigaPro', inplace=True)
df_jogos.replace(6967,'Republic of Ireland Premier Division', inplace=True)
df_jogos.replace(8741,'Republic of Ireland Premier Division', inplace=True)
df_jogos.replace(6037,'Romania Liga I', inplace=True)
df_jogos.replace(7663,'Romania Liga I', inplace=True)
df_jogos.replace(5992,'Scotland Premiership', inplace=True)
df_jogos.replace(7494,'Scotland Premiership', inplace=True)
df_jogos.replace(6046,'Serbia SuperLiga', inplace=True)
df_jogos.replace(7492,'Serbia SuperLiga', inplace=True)
df_jogos.replace(5944,'Slovakia Super Liga', inplace=True)
df_jogos.replace(7958,'Slovakia Super Liga', inplace=True)
df_jogos.replace(6048,'Slovenia PrvaLiga', inplace=True)
df_jogos.replace(7526,'Slovenia PrvaLiga', inplace=True)
df_jogos.replace(7061,'South Korea K League 1', inplace=True)
df_jogos.replace(8899,'South Korea K League 1', inplace=True)
df_jogos.replace(7062,'South Korea K League 2', inplace=True)
df_jogos.replace(8938,'South Korea K League 2', inplace=True)
df_jogos.replace(6211,'Spain La Liga', inplace=True)
df_jogos.replace(7665,'Spain La Liga', inplace=True)
df_jogos.replace(6120,'Spain Segunda División', inplace=True)
df_jogos.replace(7592,'Spain Segunda División', inplace=True)
df_jogos.replace(7064,'Sweden Allsvenskan', inplace=True)
df_jogos.replace(8737,'Sweden Allsvenskan', inplace=True)
df_jogos.replace(6044,'Switzerland Super League', inplace=True)
df_jogos.replace(7504,'Switzerland Super League', inplace=True)
df_jogos.replace(6726,'Tunisia Ligue 1', inplace=True)
df_jogos.replace(8428,'Tunisia Ligue 1', inplace=True)
df_jogos.replace(6125,'Turkey Süper Lig', inplace=True)
df_jogos.replace(7768,'Turkey Süper Lig', inplace=True)
df_jogos.replace(6969,'USA MLS', inplace=True)
df_jogos.replace(8777,'USA MLS', inplace=True)
df_jogos.replace(6970,'USA USL Championship', inplace=True)
df_jogos.replace(8845,'USA USL Championship', inplace=True)
df_jogos.replace(5943,'Ukraine Ukrainian Premier League', inplace=True)
df_jogos.replace(8222,'Ukraine Ukrainian Premier League', inplace=True)
df_jogos.replace(7067,'Uruguay Primera División', inplace=True)
df_jogos.replace(8937,'Uruguay Primera División', inplace=True)
df_jogos.replace(7173,'Uruguay Segunda División', inplace=True)
df_jogos.replace(9034,'Uruguay Segunda División', inplace=True)
df_jogos.replace(7166,'Venezuela Primera División', inplace=True)
df_jogos.replace(8952,'Venezuela Primera División', inplace=True)

df_jogos['Data'] = pd.to_datetime(df_jogos['Data'], unit='s') - pd.DateOffset(hours=3)
df_jogos['Date'] = df_jogos['Data'].dt.date
df_jogos['Time'] = df_jogos['Data'].dt.time

df_jogos = df_jogos[['League','Date','Time','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over05','FT_Odd_Under05','FT_Odd_Over15','FT_Odd_Under15','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_Over35','FT_Odd_Under35','FT_Odd_Over45','FT_Odd_Under45','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No']]

from datetime import date
flt = df_jogos.Date == date.today()
df = df_jogos[flt]
df = drop_reset_index(df)


# In[4]:


data = hoje()
hoje = data.strftime('%Y-%m-%d')
nome = 'Jogos_do_Dia.csv'
df.to_csv(f'./Teoria_dos_Retornos/{hoje}_{nome}', index = False)


# In[5]:
print("FEITO")

df


