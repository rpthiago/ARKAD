#!/usr/bin/env python
# coding: utf-8

# In[46]:


import datetime
from datetime import date, timedelta
Date = date.today() + timedelta(0)
print("Data de Análise:",Date)


# # Código Fonte

# In[47]:


from futpythontrader import *
#from google.colab import data_table
#data_table.enable_dataframe_formatter()


# In[48]:


base = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Base_de_Dados/futpythontraderpunter.csv?raw=true")
base = base[base['Season'].isin(['2022', '2022/2023']) == True]

# Resultado
base.loc[base['FT_Goals_H'] > base['FT_Goals_A'], 'FT_Result'] = "H"
base.loc[base['FT_Goals_H'] == base['FT_Goals_A'], 'FT_Result'] = "D"
base.loc[base['FT_Goals_H'] < base['FT_Goals_A'], 'FT_Result'] = "A"

# # Probabilidades
base['p_H'] = 1 / base.FT_Odd_H
base['p_D'] = 1 / base.FT_Odd_D
base['p_A'] = 1 / base.FT_Odd_A

# Pontos
base.loc[base['FT_Goals_H'] > base['FT_Goals_A'], 'Ptos_H'] = 3
base.loc[base['FT_Goals_H'] == base['FT_Goals_A'], 'Ptos_H'] = 1
base.loc[base['FT_Goals_H'] < base['FT_Goals_A'], 'Ptos_H'] = 0
base.loc[base['FT_Goals_H'] < base['FT_Goals_A'], 'Ptos_A'] = 3
base.loc[base['FT_Goals_H'] == base['FT_Goals_A'], 'Ptos_A'] = 1
base.loc[base['FT_Goals_H'] > base['FT_Goals_A'], 'Ptos_A'] = 0
base["Ptos_H"] = base["Ptos_H"].astype('int64')
base["Ptos_A"] = base["Ptos_A"].astype('int64')
base['Media_Ptos_H'] = base.groupby('Home')['Ptos_H'].rolling(window=5, min_periods=2).mean().reset_index(0,drop=True)
base['Media_Ptos_A'] = base.groupby('Away')['Ptos_A'].rolling(window=5, min_periods=2).mean().reset_index(0,drop=True)
base['DesvPad_Ptos_H'] = base.groupby('Home')['Ptos_H'].rolling(window=5, min_periods=2).std().reset_index(0,drop=True)
base['DesvPad_Ptos_A'] = base.groupby('Away')['Ptos_A'].rolling(window=5, min_periods=2).std().reset_index(0,drop=True)                
base['CV_Ptos_H'] = base['DesvPad_Ptos_H'] / base['Media_Ptos_H']
base['CV_Ptos_A'] = base['DesvPad_Ptos_A'] / base['Media_Ptos_A']

# Valor do Gol
base['VG_H'] = base.FT_Goals_H * base.p_A
base['VG_A'] = base.FT_Goals_A * base.p_H
base['Media_VG_H'] = base.groupby('Home')['VG_H'].rolling(window=5, min_periods=2).mean().reset_index(0,drop=True)
base['Media_VG_A'] = base.groupby('Away')['VG_A'].rolling(window=5, min_periods=2).mean().reset_index(0,drop=True)
base['DesvPad_VG_H'] = base.groupby('Home')['VG_H'].rolling(window=5, min_periods=2).std().reset_index(0,drop=True)
base['DesvPad_VG_A'] = base.groupby('Away')['VG_A'].rolling(window=5, min_periods=2).std().reset_index(0,drop=True)
base['CV_VG_H'] = base['DesvPad_VG_H'] / base['Media_VG_H']
base['CV_VG_A'] = base['DesvPad_VG_A'] / base['Media_VG_A']

# Custo do Gol
base['CG_H'] = base.p_H / base.FT_Goals_H
base['CG_A'] = base.p_A / base.FT_Goals_A
base['Media_CG_H'] = base.groupby('Home')['CG_H'].rolling(window=5, min_periods=2).mean().reset_index(0,drop=True)
base['Media_CG_A'] = base.groupby('Away')['CG_A'].rolling(window=5, min_periods=2).mean().reset_index(0,drop=True)
base['DesvPad_CG_H'] = base.groupby('Home')['CG_H'].rolling(window=5, min_periods=2).std().reset_index(0,drop=True)
base['DesvPad_CG_A'] = base.groupby('Away')['CG_A'].rolling(window=5, min_periods=2).std().reset_index(0,drop=True)
base['CV_CG_H'] = base['DesvPad_CG_H'] / base['Media_CG_H']
base['CV_CG_A'] = base['DesvPad_CG_A'] / base['Media_CG_A']

base.replace(np.inf, 1, inplace=True)
base.dropna(inplace=True)
base.reset_index(inplace=True, drop=True)
base.index = base.index.set_names(['Nº'])
base = base.rename(index=lambda x: x + 1)

df_H = base[['Home','Media_Ptos_H','DesvPad_Ptos_H','CV_Ptos_H','Media_VG_H','DesvPad_VG_H','CV_VG_H',
'Media_CG_H','DesvPad_CG_H','CV_CG_H']]
df_A = base[['Away','Media_Ptos_A','DesvPad_Ptos_A','CV_Ptos_A','Media_VG_A','DesvPad_VG_A','CV_VG_A',
'Media_CG_A','DesvPad_CG_A','CV_CG_A']]


# In[49]:


jogos_do_dia = pd.read_csv('https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_FlashScore/'+str(Date)+'_Jogos_do_Dia_FlashScore.csv?raw=true')

jogos_do_dia = jogos_do_dia[jogos_do_dia['League'].isin(['ARGENTINA - LIGA PROFESIONAL','AUSTRIA - BUNDESLIGA','BELGIUM - JUPILER PRO LEAGUE','BRAZIL - SERIE A','BRAZIL - SERIE B',
                           'CROATIA - HNL','DENMARK - SUPERLIGA','ENGLAND - CHAMPIONSHIP','ENGLAND - PREMIER LEAGUE','FRANCE - LIGUE 1','FRANCE - LIGUE 2',
                           'GERMANY - 2. BUNDESLIGA','GERMANY - BUNDESLIGA','IRELAND - PREMIER DIVISION','ITALY - SERIE A', 'ITALY - SERIE B','MEXICO - LIGA MX',
                           'NETHERLANDS - EERSTE DIVISIE','NETHERLANDS - EREDIVISIE','NORWAY - ELITESERIEN','POLAND - EKSTRAKLASA','PORTUGAL - LIGA PORTUGAL',
                           'PORTUGAL - LIGA PORTUGAL 2','SCOTLAND - PREMIERSHIP','SERBIA - SUPER LIGA','SLOVAKIA - FORTUNA LIGA','SLOVENIA - PRVA LIGA',
                           'SPAIN - LALIGA','SPAIN - LALIGA2','SWEDEN - ALLSVENSKAN','SWITZERLAND - SUPER LEAGUE','TURKEY - SUPER LIG','USA - MLS'])]

jogos_do_dia.to_excel('tt.xlsx')


# In[50]:


lista=[]

for a,b,c,d,e,f,g,h,i in zip(jogos_do_dia.League,jogos_do_dia.Date,jogos_do_dia.Time,jogos_do_dia.Home,jogos_do_dia.Away,jogos_do_dia.FT_Odd_H,jogos_do_dia.FT_Odd_D,jogos_do_dia.FT_Odd_A,jogos_do_dia.FT_Odd_Over25):
    try:
        League = a
        Date = b
        Time = c
        home = d
        away = e
        FT_Odd_H = f
        FT_Odd_D = g
        FT_Odd_A = h
        FT_Odd_Over25 = i

        df1 = df_H[df_H.Home == home].tail(1)

        df2 = df_A[df_A.Away == away].tail(1)

        jogo = {}

        jogo["League"] = League 
        jogo["Date"] = Date
        jogo["Time"] = Time
        jogo["Home"] = home
        jogo["Away"] = away
        jogo["FT_Odd_H"] = FT_Odd_H
        jogo["FT_Odd_D"] = FT_Odd_D
        jogo["FT_Odd_A"] = FT_Odd_A
        jogo["FT_Odd_Over25"] = FT_Odd_Over25
        jogo["Media_Ptos_H"] = df1[df1.Home == home]['Media_Ptos_H'].iloc[0]
        jogo["DesvPad_Ptos_H"] = df1[df1.Home == home]['DesvPad_Ptos_H'].iloc[0]
        jogo["CV_Ptos_H"] = df1[df1.Home == home]['CV_Ptos_H'].iloc[0]
        jogo["Media_VG_H"] = df1[df1.Home == home]['Media_VG_H'].iloc[0]
        jogo["DesvPad_VG_H"] = df1[df1.Home == home]['DesvPad_VG_H'].iloc[0]
        jogo["CV_VG_H"] = df1[df1.Home == home]['CV_Ptos_H'].iloc[0]
        jogo["Media_CG_H"] = df1[df1.Home == home]['Media_CG_H'].iloc[0]
        jogo["DesvPad_CG_H"] = df1[df1.Home == home]['DesvPad_CG_H'].iloc[0]
        jogo["CV_CG_H"] = df1[df1.Home == home]['CV_CG_H'].iloc[0]
        jogo["Media_Ptos_A"] = df2[df2.Away == away]['Media_Ptos_A'].iloc[0]
        jogo["DesvPad_Ptos_A"] = df2[df2.Away == away]['DesvPad_Ptos_A'].iloc[0]
        jogo["CV_Ptos_A"] = df2[df2.Away == away]['CV_Ptos_A'].iloc[0]
        jogo["Media_VG_A"] = df2[df2.Away == away]['Media_VG_A'].iloc[0]
        jogo["DesvPad_VG_A"] = df2[df2.Away == away]['DesvPad_VG_A'].iloc[0]
        jogo["CV_VG_A"] = df2[df2.Away == away]['CV_Ptos_A'].iloc[0]
        jogo["Media_CG_A"] = df2[df2.Away == away]['Media_CG_A'].iloc[0]
        jogo["DesvPad_CG_A"] = df2[df2.Away == away]['DesvPad_CG_A'].iloc[0]
        jogo["CV_CG_A"] = df2[df2.Away == away]['CV_CG_A'].iloc[0]
        
        lista.append(jogo)

    except:
        pass

df = pd.DataFrame(lista)
df.reset_index(inplace=True, drop=True)
df.index = df.index.set_names(['Nº'])
df = df.rename(index=lambda x: x + 1)


# In[51]:


# Probabilidades
df['p_H'] = 1 / df.FT_Odd_H
df['p_D'] = 1 / df.FT_Odd_D
df['p_A'] = 1 / df.FT_Odd_A
df['p_Over'] = 1 / df.FT_Odd_Over25

# CV das Odds do Match Odds
df['CV_HDA'] = df[['p_H','p_D','p_A']].std(ddof=0, axis=1) / df[['p_H','p_D','p_A']].mean(axis=1)


# In[52]:


filtro = (   
  ((df.p_H>0.5649717514124294) & (df.p_H<0.9259259259259258))
& ((df.p_D>0.08333333333333333) & (df.p_D<0.3076923076923077))
& ((df.p_A>0.03333333333333333) & (df.p_A<0.2777777777777778))
& ((df.p_Over>0.3472222222222222) & (df.p_Over<0.7751937984496123))
& ((df.CV_HDA>0.36234682380465133) & (df.CV_HDA<1.159609030595692))
& ((df.Media_Ptos_H>0.2) & (df.Media_Ptos_H<3.0))
& ((df.Media_Ptos_A>0.0) & (df.Media_Ptos_A<1.75))
& ((df.CV_Ptos_H>0.0) & (df.CV_Ptos_H<2.2360679774997907))
& ((df.CV_Ptos_A>0.0) & (df.CV_Ptos_A<2.236067977499792))
& ((df.Media_VG_H>0.059340659340659074) & (df.Media_VG_H<1.0757265992756089))
& ((df.Media_VG_A>0.1934731934731934) & (df.Media_VG_A<1.7645676691729317))
& ((df.CV_VG_H>0.06332299533013878) & (df.CV_VG_H<1.8339629103004964))
& ((df.CV_VG_A>0.06869644114659167) & (df.CV_VG_A<1.5770968944078807))
& ((df.Media_CG_H>0.10727190605239376) & (df.Media_CG_H<0.675248419150858))
& ((df.Media_CG_A>0.10557290573168168) & (df.Media_CG_A<0.298245614035088))
& ((df.CV_CG_H>0.0) & (df.CV_CG_H<1.096295307426663))
& ((df.CV_CG_A>0.0) & (df.CV_CG_A<1.2784658672552298))
)


# In[53]:


# df_Lay_1x0 = df[filtro]
# df_Lay_1x0 = df_Lay_1x0[['League','Date','Time','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A']] 
# df_Lay_1x0.reset_index(inplace=True, drop=True)
# df_Lay_1x0.index = df_Lay_1x0.index.set_names(['Nº'])
# df_Lay_1x0 = df_Lay_1x0.rename(index=lambda x: x + 1)
# df_Lay_1x0 = df_Lay_1x0.sort_values(['Time'])
# df_Lay_1x0.reset_index(inplace=True, drop=True)
# df_Lay_1x0.index = df_Lay_1x0.index.set_names(['Nº'])
# df_Lay_1x0 = df_Lay_1x0.rename(index=lambda x: x + 1)


# In[54]:


# Dataframe Filtrado
def retorna_df(dicionario,data):
    data = data.copy()
    list_columns = dicionario.keys()
    for i in data.columns.to_list():
        for x in list_columns:
            if i.lower() in x:
                try:
                    x_min = dicionario[f'{i.lower()}_min']
                    x_max = dicionario[f'{i.lower()}_max']
                    data = data[data[i].between(x_min,x_max)]
                except:
                    pass
    return data


# In[55]:


result = {'p_h_min': 0.14285714285714285,
 'p_h_max': 0.31746031746031744,
 'p_d_min': 0.2,
 'p_d_max': 0.3333333333333333,
 'p_a_min': 0.5,
 'p_a_max': 0.6535947712418301,
 'p_over_min': 0.38167938931297707,
 'p_over_max': 0.6711409395973155,
 'cv_hda_min': 0.23750435276082887,
 'cv_hda_max': 0.6142425378260569,
 'media_ptos_h_min': 0.0,
 'media_ptos_h_max': 2.6,
 'media_ptos_a_min': 0.2,
 'media_ptos_a_max': 3.0,
 'cv_ptos_h_min': 0.0,
 'cv_ptos_h_max': 2.23606797749979,
 'cv_ptos_a_min': 0.0,
 'cv_ptos_a_max': 2.23606797749979,
 'media_vg_h_min': 0.09753694581280767,
 'media_vg_h_max': 0.9479747305834264,
 'media_vg_a_min': 0.1706766917293232,
 'media_vg_a_max': 0.7879256965944271,
 'cv_vg_h_min': 0.12487264529334759,
 'cv_vg_h_max': 1.8308606668040055,
 'cv_vg_a_min': 0.13251514240141918,
 'cv_vg_a_max': 1.7934349826132214,
 'media_cg_h_min': 0.10220797720797693,
 'media_cg_h_max': 0.5793650793650793,
 'media_cg_a_min': 0.11045270125987595,
 'media_cg_a_max': 0.5484167837555098,
 'cv_cg_h_min': 0.015890040026663988,
 'cv_cg_h_max': 1.0965284591499063,
 'cv_cg_a_min': 0.02119806196276601,
 'cv_cg_a_max': 0.9397910869035022}


# In[56]:


df_Lay_1x0 = retorna_df(result,df)
df_Lay_1x0 = df_Lay_1x0[['League','Date','Time','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A']] 
df_Lay_1x0.reset_index(inplace=True, drop=True)
df_Lay_1x0.index = df_Lay_1x0.index.set_names(['Nº'])
df_Lay_1x0 = df_Lay_1x0.rename(index=lambda x: x + 1)
df_Lay_1x0 = df_Lay_1x0.sort_values(['Time'])
df_Lay_1x0.reset_index(inplace=True, drop=True)
df_Lay_1x0.index = df_Lay_1x0.index.set_names(['Nº'])
df_Lay_1x0 = df_Lay_1x0.rename(index=lambda x: x + 1)


# In[57]:


def entradas_de_hoje():
     print('######################')
     print('Entradas - FutPythonPunter') 
     print('######################')
     print('Dia:',Date)
     print('######################')
     print('Método: Lay 1 x 0')
     print('######################')

     for a,b,c,d in zip(df_Lay_1x0.League,df_Lay_1x0.Time,df_Lay_1x0.Home,df_Lay_1x0.Away):

         liga = a
         horario = b
         home = c
         away = d
    
        
         print('');print("Liga:",liga)
         print("Horário:",horario)
         print("Jogo:",home,'x',away)
         print("Odd Lay 1 x 0 Pré-Live: ")
         print("Odd Lay 1 x 0 Entrada: ")
        
     print('')


# # Entradas

# In[58]:


data = hoje()
hoje = data.strftime('%Y-%m-%d')
nome = 'LAY_1X0.csv'
df_Lay_1x0.to_csv(f'./Teoria_dos_Retornos/{hoje}_{nome}', index = False)
df_Lay_1x0


# In[59]:


entradas_de_hoje()

