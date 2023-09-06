#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import date, datetime, timedelta
data = date.today() + timedelta(1)
print("Data de Análise:")

from futpythontrader import *


# In[2]:


#base = pd.read_csv("https://github.com/rpthiago/ARKAD/blob/main/BASE_DE_DAD0S_FLASHSCORE/Base_FlahScore.csv?raw=true")
base = pd.read_csv("C:/Users/thiag/OneDrive/curso python/MODELOS LEANDRO/WEBCRAPING_JOGOS_FLASHSCORE/Base_FlahScore_odds.csv")
base["Date"] = pd.to_datetime(base["Date"])


# In[3]:


#jogos_do_dia = pd.read_csv('https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_FlashScore/'+str(data)+'_Jogos_do_Dia_FlashScore.csv?raw=true')
jogos_do_dia = pd.read_csv('C:/Users/thiag/OneDrive/curso python/MODELOS LEANDRO/WEBCRAPING_JOGOS_FLASHSCORE/Jogos_do_Dia/'+str(data)+'_Jogos_do_Dia.csv') 
#jogos_do_dia = pd.read_csv('C:/Users/thiag/OneDrive/curso python/modelo_leandro_2/flashscore/Jogos_do_Dia/'+str(data)+'_Jogos_do_Dia.csv')


#jogos_do_dia.dropna(inplace=True)
jogos_do_dia.reset_index(inplace=True, drop=True)
jogos_do_dia.index = jogos_do_dia.index.set_names(['Nº'])
jogos_do_dia = jogos_do_dia.rename(index=lambda x: x + 1)

jogos_do_dia


# In[4]:


ligas = jogos_do_dia.sort_values(['League'])
ligas = ligas['League'].unique()
ligas


# In[5]:


def TR():
    for i in ligas:
        liga = i
        
        if liga == "ARMENIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ALBANIA - SUPERLIGA":
            df = base[base.League == liga]    
        if liga == "ANDORRA - PRIMERA DIVISIÓ":
            df = base[base.League == liga]
        if liga == "ANGOLA - GIRABOLA":
            df = base[base.League == liga]
        if liga == "ARGENTINA - COPA DE LA LIGA PROFESIONAL":
            df = base[base.League == liga]
        if liga == "ARGENTINA - LIGA PROFESIONAL":
            df = base[base.League == liga]
        if liga == "ARGENTINA - PRIMERA NACIONAL":
            df = base[base.League == liga]
        if liga == "AUSTRALIA - A-LEAGUE":
            df = base[base.League == liga]
        if liga == "AUSTRIA - 2. LIGA":
            df = base[base.League == liga]
        if liga == "AUSTRIA - BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "AZERBAIJAN - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "BANGLADESH - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "BELARUS - VYSSHAYA LIGA":
            df = base[base.League == liga]
        if liga == "BELGIUM - CHALLENGER PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "BELGIUM - JUPILER PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "BOLIVIA - DIVISION PROFESIONAL":
            df = base[base.League == liga]
        if liga == "BOLIVIA - NACIONAL B":
            df = base[base.League == liga]
        if liga == "BOSNIA AND HERZEGOVINA - PREMIJER LIGA BIH":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO U20":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO U23":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO WOMEN":
            df = base[base.League == liga]
        if liga == "BRAZIL - COPA DO BRASIL":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE A":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE B":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE C":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE D":
            df = base[base.League == liga]
        if liga == "BULGARIA - PARVA LIGA":
            df = base[base.League == liga]
        if liga == "CAMEROON - ELITE ONE":
            df = base[base.League == liga]
        if liga == "CANADA - CANADIAN PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "CHILE - PRIMERA B":
            df = base[base.League == liga]
        if liga == "CHILE - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "CHINA - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "COLOMBIA - PRIMERA A":
            df = base[base.League == liga]
        if liga == "COLOMBIA - PRIMERA B":
            df = base[base.League == liga]
        if liga == "COSTA RICA - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "CROATIA - HNL":
            df = base[base.League == liga]
        if liga == "CROATIA - PRVA NL":
            df = base[base.League == liga]
        if liga == "CYPRUS - CYTA CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "CZECH REPUBLIC - FORTUNA:LIGA":
            df = base[base.League == liga]
        if liga == "DENMARK - 1ST DIVISION":
            df = base[base.League == liga]
        if liga == "DENMARK - SUPERLIGA":
            df = base[base.League == liga]
        if liga == "DOMINICAN REPUBLIC - LDF":
            df = base[base.League == liga]
        if liga == "ECUADOR - LIGA PRO":
            df = base[base.League == liga]
        if liga == "ECUADOR - SERIE B":
            df = base[base.League == liga]
        if liga == "EGYPT - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "ENGLAND - EFL CUP":
            df = base[base.League == liga]
        if liga == "ENGLAND - FA CUP":
            df = base[base.League == liga]
        if liga == "ENGLAND - LEAGUE ONE":
            df = base[base.League == liga]
        if liga == "ENGLAND - LEAGUE TWO":
            df = base[base.League == liga]
        if liga == "ENGLAND - NATIONAL LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - PREMIER LEAGUE 2":
            df = base[base.League == liga]
        if liga == "ESTONIA - ESILIIGA":
            df = base[base.League == liga]
        if liga == "ESTONIA - MEISTRILIIGA":
            df = base[base.League == liga]
        if liga == "EUROPE - CHAMPIONS LEAGUE":
            df = base[base.League == liga]
        if liga == "EUROPE - EUROPA CONFERENCE LEAGUE":
            df = base[base.League == liga]
        if liga == "EUROPE - EUROPA LEAGUE":
            df = base[base.League == liga]
        if liga == "FIJI - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "FINLAND - VEIKKAUSLIIGA":
            df = base[base.League == liga]
        if liga == "FINLAND - YKKONEN":
            df = base[base.League == liga]
        if liga == "FRANCE - LIGUE 1":
            df = base[base.League == liga]
        if liga == "FRANCE - LIGUE 2":
            df = base[base.League == liga]
        if liga == "FRANCE - NATIONAL":
            df = base[base.League == liga]
        if liga == "GEORGIA - CRYSTALBET EROVNULI LIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - 2. BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - 3. LIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - DFB POKAL":
            df = base[base.League == liga]
        if liga == "GHANA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "GREECE - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "GUATEMALA - LIGA NACIONAL":
            df = base[base.League == liga]
        if liga == "HONDURAS - LIGA NACIONAL":
            df = base[base.League == liga]
        if liga == "HONG KONG - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "HUNGARY - OTP BANK LIGA":
            df = base[base.League == liga]
        if liga == "ICELAND - BESTA DEILD KARLA":
            df = base[base.League == liga]
        if liga == "INDIA - I-LEAGUE":
            df = base[base.League == liga]
        if liga == "INDIA - ISL":
            df = base[base.League == liga]
        if liga == "INDONESIA - LIGA 1":
            df = base[base.League == liga]
        if liga == "IRAN - PERSIAN GULF PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "IRAQ - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "IRELAND - DIVISION 1":
            df = base[base.League == liga]
        if liga == "IRELAND - PREMIER DIVISION":
            df = base[base.League == liga]
        if liga == "ISRAEL - LIGAT HA'AL":
            df = base[base.League == liga]
        if liga == "ITALY - COPPA ITALIA":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE A":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE B":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE C":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE D":
            df = base[base.League == liga]
        if liga == "IVORY COAST - LIGUE 1":
            df = base[base.League == liga]
        if liga == "JAMAICA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "JAPAN - J1 LEAGUE":
            df = base[base.League == liga]
        if liga == "JAPAN - J2 LEAGUE":
            df = base[base.League == liga]
        if liga == "LITHUANIA - A LYGA":
            df = base[base.League == liga]
        if liga == "LUXEMBOURG - NATIONAL DIVISION":
            df = base[base.League == liga]
        if liga == "MALTA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "MEXICO - LIGA DE EXPANSION MX":
            df = base[base.League == liga]
        if liga == "MEXICO - LIGA MX":
            df = base[base.League == liga]
        if liga == "MOLDOVA - SUPER LIGA":
            df = base[base.League == liga]
        if liga == "MONGOLIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "MONTENEGRO - PRVA CRNOGORSKA LIGA":
            df = base[base.League == liga]
        if liga == "MOROCCO - BOTOLA PRO":
            df = base[base.League == liga]
        if liga == "MOZAMBIQUE - MOCAMBOLA":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - DERDE DIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - EERSTE DIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - EREDIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - TWEEDE DIVISIE":
            df = base[base.League == liga]
        if liga == "NICARAGUA - LIGA PRIMERA":
            df = base[base.League == liga]
        if liga == "NIGERIA - NPFL":
            df = base[base.League == liga]
        if liga == "NORTH MACEDONIA - 1. MFL":
            df = base[base.League == liga]
        if liga == "NORTHERN IRELAND - NIFL CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "NORTHERN IRELAND - NIFL PREMIERSHIP":
            df = base[base.League == liga]
        if liga == "NORWAY - ELITESERIEN":
            df = base[base.League == liga]
        if liga == "NORWAY - OBOS-LIGAEN":
            df = base[base.League == liga]
        if liga == "PANAMA - LPF":
            df = base[base.League == liga]
        if liga == "PARAGUAY - DIVISION INTERMEDIA":
            df = base[base.League == liga]
        if liga == "PARAGUAY - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "PERU - LIGA 1":
            df = base[base.League == liga]
        if liga == "PERU - LIGA 2":
            df = base[base.League == liga]
        if liga == "PHILIPPINES - PFL":
            df = base[base.League == liga]
        if liga == "POLAND - DIVISION 1":
            df = base[base.League == liga]
        if liga == "POLAND - EKSTRAKLASA":
            df = base[base.League == liga]
        if liga == "PORTUGAL - LIGA PORTUGAL":
            df = base[base.League == liga]
        if liga == "PORTUGAL - LIGA PORTUGAL 2":
            df = base[base.League == liga]
        if liga == "PORTUGAL - TAÇA DE PORTUGAL":
            df = base[base.League == liga]
        if liga == "QATAR - QSL":    
            df = base[base.League == liga]
        if liga == "ROMANIA - LIGA 1":
            df = base[base.League == liga]
        if liga == "ROMANIA - LIGA 2":   
            df = base[base.League == liga]
        if liga == "RUSSIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "SAN MARINO - CAMPIONATO SAMMARINESE":
            df = base[base.League == liga]
        if liga == "SAUDI ARABIA - SAUDI PROFESSIONAL LEAGUE":
            df = base[base.League == liga]
        if liga == "SCOTLAND - CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "SCOTLAND - LEAGUE ONE":
            df = base[base.League == liga]
        if liga == "SCOTLAND - LEAGUE TWO":
            df = base[base.League == liga]
        if liga == "SCOTLAND - PREMIERSHIP":
            df = base[base.League == liga]
        if liga == "SENEGAL - LIGUE 1":   
            df = base[base.League == liga]
        if liga == "SERBIA - PRVA LIGA":  
            df = base[base.League == liga]
        if liga == "SERBIA - SUPER LIGA": 
            df = base[base.League == liga]
        if liga == "SINGAPORE - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "SLOVAKIA - NIKE LIGA":
            df = base[base.League == liga]
        if liga == "SLOVENIA - PRVA LIGA":
            df = base[base.League == liga]
        if liga == "SOUTH AMERICA - COPA LIBERTADORES":
            df = base[base.League == liga]
        if liga == "SOUTH AMERICA - COPA SUDAMERICANA":
            df = base[base.League == liga]
        if liga == "SOUTH KOREA - K LEAGUE 1":
            df = base[base.League == liga]
        if liga == "SOUTH KOREA - K LEAGUE 2":
            df = base[base.League == liga]
        if liga == "SPAIN - COPA DEL REY":
            df = base[base.League == liga]
        if liga == "SPAIN - LALIGA":
            df = base[base.League == liga]
        if liga == "SPAIN - LALIGA2":   
            df = base[base.League == liga]
        if liga == "SPAIN - PRIMERA RFEF":
            df = base[base.League == liga]
        if liga == "SPAIN - SEGUNDA RFEF":
            df = base[base.League == liga]
        if liga == "SWEDEN - ALLSVENSKAN":
            df = base[base.League == liga]
        if liga == "SWEDEN - SUPERETTAN": 
            df = base[base.League == liga]
        if liga == "SWITZERLAND - CHALLENGE LEAGUE":
            df = base[base.League == liga]
        if liga == "SWITZERLAND - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "THAILAND - THAI LEAGUE 1":
            df = base[base.League == liga]
        if liga == "THAILAND - THAI LEAGUE 2":
            df = base[base.League == liga]
        if liga == "TUNISIA - LIGUE PROFESSIONNELLE 1":
            df = base[base.League == liga]
        if liga == "TURKEY - 1. LIG":    
            df = base[base.League == liga]
        if liga == "TURKEY - SUPER LIG":
            df = base[base.League == liga]
        if liga == "UGANDA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "UKRAINE - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "UNITED ARAB EMIRATES - UAE LEAGUE": 
            df = base[base.League == liga]
        if liga == "URUGUAY - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "URUGUAY - SEGUNDA DIVISION":
            df = base[base.League == liga]
        if liga == "USA - MLS":    
            df = base[base.League == liga]
        if liga == "USA - USL CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "UZBEKISTAN - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "VENEZUELA - LIGA FUTVE":
            df = base[base.League == liga]
        if liga == "VENEZUELA - LIGA FUTVE 2":
            df = base[base.League == liga]
        if liga == "VIETNAM - V.LEAGUE 1":
            df = base[base.League == liga]
        if liga == "WALES - CYMRU PREMIER":
            df = base[base.League == liga]
        
        
        df["FT_Goals_H"] = df["FT_Goals_H"].astype('int64')
        df["FT_Goals_A"] = df["FT_Goals_A"].astype('int64')
        df['FT_Odd_H'] = pd.to_numeric(df['FT_Odd_H'],errors = 'coerce')
        df['FT_Odd_D'] = pd.to_numeric(df['FT_Odd_D'],errors = 'coerce')
        df['FT_Odd_A'] = pd.to_numeric(df['FT_Odd_A'],errors = 'coerce')
        df['FT_Odd_Over25'] = pd.to_numeric(df['FT_Odd_Over25'],errors = 'coerce')
        
        total_count = len(df.index)
        df["Date"] = pd.to_datetime(df["Date"])
        df['Date'] = df['Date'].dt.date

        winHPLValues = 100 * df.FT_Odd_H - 100
        winDPLValues = 100 * df.FT_Odd_D - 100
        winAPLValues = 100 * df.FT_Odd_A - 100
        losePLValues = -100

        df.loc[((df['FT_Goals_H']) > (df['FT_Goals_A'])), 'Result_FT'] = 'H'
        df.loc[((df['FT_Goals_H']) == (df['FT_Goals_A'])), 'Result_FT'] = 'D'
        df.loc[((df['FT_Goals_H']) < (df['FT_Goals_A'])), 'Result_FT'] = 'A'

        df['H'] = winHPLValues.where(df.Result_FT == 'H', other=losePLValues)
        df['D'] = winDPLValues.where(df.Result_FT == 'D', other=losePLValues)
        df['A'] = winAPLValues.where(df.Result_FT == 'A', other=losePLValues)

        no_of_days = 0

        matchDates = df.Date.unique()

        if no_of_days > 0:
            matchDates = (matchDates[-no_of_days:])
                
        df2 = pd.DataFrame()

        rowsIndex = []
        rowsDate = []
        rowsH = []
        rowsD = []
        rowsA = []

        count = 0
        for mDate in matchDates:
            count += 1
            rowsDate.append(mDate)
            rowsH.append(df.loc[df['Date'] == mDate]['H'].sum())
            rowsD.append(df.loc[df['Date'] == mDate]['D'].sum())
            rowsA.append(df.loc[df['Date'] == mDate]['A'].sum())

        df2['Date'] = rowsDate
        df2['H'] = rowsH
        df2['D'] = rowsD
        df2['A'] = rowsA

        df2 = df2.tail(101)
        df2 = df2.reset_index(drop=True)
        df2['Id'] = df2.reset_index()['index'].rename('index_copy')
        df2['Id'] = df2['Id'] + 1
        df2 = df2[['Id','Date','H','D','A']]

        df2['Hacu'] = df2.H.cumsum()
        df2['Dacu'] = df2.D.cumsum()
        df2['Aacu'] = df2.A.cumsum()

        df2['Hacu'].loc[0] = np.nan
        df2['Dacu'].loc[0] = np.nan
        df2['Aacu'].loc[0] = np.nan

        def weighted_mean_H(s):
            d = df2.loc[s.index, 'Hacu']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_H_C(s):
            d = df2.loc[s.index, 'waHC']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_D(s):
            d = df2.loc[s.index, 'Dacu']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_D_C(s):
            d = df2.loc[s.index, 'waDC']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_A(s):
            d = df2.loc[s.index, 'Aacu']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_A_C(s):
            d = df2.loc[s.index, 'waAC']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        df2['waH16'] = df2.rolling(16)['Hacu'].apply(weighted_mean_H, raw=False)
        df2['waH8'] = df2.rolling(8)['Hacu'].apply(weighted_mean_H, raw=False)
        df2['waHC'] = 2*df2.waH8-df2.waH16
        df2['waH4'] = df2.rolling(4)['waHC'].apply(weighted_mean_H_C, raw=False)

        df2['waD16'] = df2.rolling(16)['Dacu'].apply(weighted_mean_D, raw=False)
        df2['waD8'] = df2.rolling(8)['Dacu'].apply(weighted_mean_D, raw=False)
        df2['waDC'] = 2*df2.waD8-df2.waD16
        df2['waD4'] = df2.rolling(4)['waDC'].apply(weighted_mean_D_C, raw=False)

        df2['waA16'] = df2.rolling(16)['Aacu'].apply(weighted_mean_A, raw=False)
        df2['waA8'] = df2.rolling(8)['Aacu'].apply(weighted_mean_A, raw=False)
        df2['waAC'] = 2*df2.waA8-df2.waA16
        df2['waA4'] = df2.rolling(4)['waAC'].apply(weighted_mean_A_C, raw=False)

        df2['Hhull'] = df2['waH4']
        df2['Dhull'] = df2['waD4']
        df2['Ahull'] = df2['waA4']

        df2['Hdist'] = (df2.Hacu / df2.Hhull)
        df2['Ddist'] = (df2.Dacu / df2.Dhull)
        df2['Adist'] = (df2.Aacu / df2.Ahull)

        def r_function(s):
            f = s.loc[s.index.values[0]]
            l = s.loc[s.index.values[1]]
            return (l -f)/abs(f)

        df2['Hr'] = df2['Hhull'].rolling(2).apply(r_function, raw=False)
        df2['Dr'] = df2['Dhull'].rolling(2).apply(r_function, raw=False)
        df2['Ar'] = df2['Ahull'].rolling(2).apply(r_function, raw=False)

        def inc_H(s):
            x = df2.loc[s.index, 'Id']
            y = df2.loc[s.index, 'Hhull']
            slope, intercept = np.polyfit(x, y , 1)
            return slope

        def inc_D(s):
            x = df2.loc[s.index, 'Id']
            y = df2.loc[s.index, 'Dhull']
            slope, intercept = np.polyfit(x, y, 1)
            return slope

        def inc_A(s):
            x = df2.loc[s.index, 'Id']
            y = df2.loc[s.index, 'Ahull']
            slope, intercept = np.polyfit(x, y, 1)
            return slope
        
        df2['Hinc'] = df2['Hhull'].rolling(5).apply(inc_H, raw=False)
        df2['Dinc'] = df2['Dhull'].rolling(5).apply(inc_D, raw=False)
        df2['Ainc'] = df2['Ahull'].rolling(5).apply(inc_A, raw=False)

        df2['Hdp'] = df2['Hacu'].rolling(10).std()
        df2['Ddp'] = df2['Dacu'].rolling(10).std()
        df2['Adp'] = df2['Aacu'].rolling(10).std()

        df2['Hamp'] = df2['Hacu'].rolling(10).max() / df2['Hacu'].rolling(10).min()
        df2['Damp'] = df2['Dacu'].rolling(10).max() / df2['Dacu'].rolling(10).min()
        df2['Aamp'] = df2['Aacu'].rolling(10).max() / df2['Aacu'].rolling(10).min()
        
        df3 = pd.DataFrame()

        def normaliz(dfS):
            actual_value = (dfS.loc[dfS.index.values[4]])
            try:
                n = (actual_value - dfS.min()) / (dfS.max() - dfS.min())
                if math.isnan(n):
                    return 0
            except ZeroDivisionError:
                return 0
            return n

        
        df3['Id'] = df2['Id'].iloc[23:]

        df3['Hhull'] = df2['Hhull'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Dhull'] = df2['Dhull'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Ahull'] = df2['Ahull'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hdist'] = df2['Hdist'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Ddist'] = df2['Ddist'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Adist'] = df2['Adist'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hr'] = df2['Hr'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Dr'] = df2['Dr'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Ar'] = df2['Ar'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hinc'] = df2['Hinc'].rolling(5).apply(normaliz, raw=False)
        df3['Dinc'] = df2['Dinc'].rolling(5).apply(normaliz, raw=False)
        df3['Ainc'] = df2['Ainc'].rolling(5).apply(normaliz, raw=False)

        df3['Hdp'] = df2['Hdp'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Ddp'] = df2['Ddp'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Adp'] = df2['Adp'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hamp'] = df2['Hamp'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Damp'] = df2['Damp'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Aamp'] = df2['Aamp'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['R'] = ''

        for index, row in df2.iterrows():
            if index > 26:
                try:
                    h = df2.iloc[(index+1)].H
                    d = df2.iloc[(index+1)].D
                    a = df2.iloc[(index+1)].A
                    if h > d and h > a:
                        df3.loc[index, 'R'] = 'H'
                    elif d > h and d > a:
                        df3.loc[index, 'R'] = 'D'
                    else:
                        df3.loc[index, 'R'] = 'A'
                except LookupError:
                    pass

        selected_date = df3.iloc[-1]

        distance_columns = ['Hhull', 'Dhull', 'Ahull', 'Hdist', 'Ddist', 'Adist', 'Hr', 'Dr', 'Ar', 'Hinc', 'Dinc', 'Ainc', 'Hdp',
                            'Ddp', 'Adp', 'Hamp', 'Damp', 'Aamp']

        def euclidean_distance(row):
            """
            A simple euclidean distance function
            """
            inner_value = 0
            for k in distance_columns:
                inner_value += (row[k] - selected_date[k]) ** 2
            return math.sqrt(inner_value)

        def euclidean_distance_tr(row):
            inner_value = 0
            for k in distance_columns:
                inner_value += abs(row[k] - selected_date[k])
            return inner_value
        

        df3['eucli'] = df3.apply(euclidean_distance_tr, axis=1)
        
        
        df4 = pd.DataFrame()
        df4['R'] = df3['R']
        df4['eucli'] = df3['eucli']
        df4.sort_values(by=['eucli'], inplace=True)


        teoria_dos_retornos = {}
      
        try:
            #teoria_dos_retornos["Date"] = datetime.today().strftime('%Y-%m-%d')
            teoria_dos_retornos["League"] = liga
            teoria_dos_retornos["N1"] = df4[df4.eucli != 0]['R'].iloc[0]
        except:
            teoria_dos_retornos["N1"] = 0
        try:
            teoria_dos_retornos["N2"] = df4[df4.eucli != 0]['R'].iloc[1]
        except:
            teoria_dos_retornos["N2"] = 0
        try:
            teoria_dos_retornos["N3"] = df4[df4.eucli != 0]['R'].iloc[2]
        except:
            teoria_dos_retornos["N3"] = 0

        lista.append(teoria_dos_retornos)

lista = [ ]
TR() 
df00 = pd.DataFrame(lista)
Jogos_do_Dia = jogos_do_dia.merge(df00, on=['League'])
Jogos_do_Dia.reset_index(inplace=True, drop=True)
Jogos_do_Dia.index = Jogos_do_Dia.index.set_names(['Nº'])
Jogos_do_Dia = Jogos_do_Dia.rename(index=lambda x: x + 1)

# Gerando os dados para excel
# data = date.today()  + timedelta(1)
hoje = data.strftime('%Y-%m-%d')
nome = 'Teoria_dos_Retornos_Match_Odds_arkad.csv'
df00.to_csv(f'./Teoria_dos_Retornos/{data}_{nome}', index = False)
df00


# In[6]:


def TR():
    for i in ligas:
        liga = i
        
        if liga == "ARMENIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ALBANIA - SUPERLIGA":
            df = base[base.League == liga]
        if liga == "ANDORRA - PRIMERA DIVISIÓ":
            df = base[base.League == liga]
        if liga == "ANGOLA - GIRABOLA":
            df = base[base.League == liga]
        if liga == "ARGENTINA - COPA DE LA LIGA PROFESIONAL":
            df = base[base.League == liga]
        if liga == "ARGENTINA - LIGA PROFESIONAL":
            df = base[base.League == liga]
        if liga == "ARGENTINA - PRIMERA NACIONAL":
            df = base[base.League == liga]
        if liga == "AUSTRALIA - A-LEAGUE":
            df = base[base.League == liga]
        if liga == "AUSTRIA - 2. LIGA":
            df = base[base.League == liga]
        if liga == "AUSTRIA - BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "AZERBAIJAN - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "BANGLADESH - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "BELARUS - VYSSHAYA LIGA":
            df = base[base.League == liga]
        if liga == "BELGIUM - CHALLENGER PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "BELGIUM - JUPILER PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "BOLIVIA - DIVISION PROFESIONAL":
            df = base[base.League == liga]
        if liga == "BOLIVIA - NACIONAL B":
            df = base[base.League == liga]
        if liga == "BOSNIA AND HERZEGOVINA - PREMIJER LIGA BIH":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO U20":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO U23":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO WOMEN":
            df = base[base.League == liga]
        if liga == "BRAZIL - COPA DO BRASIL":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE A":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE B":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE C":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE D":
            df = base[base.League == liga]
        if liga == "BULGARIA - PARVA LIGA":
            df = base[base.League == liga]
        if liga == "CAMEROON - ELITE ONE":
            df = base[base.League == liga]
        if liga == "CANADA - CANADIAN PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "CHILE - PRIMERA B":
            df = base[base.League == liga]
        if liga == "CHILE - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "CHINA - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "COLOMBIA - PRIMERA A":
            df = base[base.League == liga]
        if liga == "COLOMBIA - PRIMERA B":
            df = base[base.League == liga]
        if liga == "COSTA RICA - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "CROATIA - HNL":
            df = base[base.League == liga]
        if liga == "CROATIA - PRVA NL":
            df = base[base.League == liga]
        if liga == "CYPRUS - CYTA CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "CZECH REPUBLIC - FORTUNA:LIGA":
            df = base[base.League == liga]
        if liga == "DENMARK - 1ST DIVISION":
            df = base[base.League == liga]
        if liga == "DENMARK - SUPERLIGA":
            df = base[base.League == liga]
        if liga == "DOMINICAN REPUBLIC - LDF":
            df = base[base.League == liga]
        if liga == "ECUADOR - LIGA PRO":
            df = base[base.League == liga]
        if liga == "ECUADOR - SERIE B":
            df = base[base.League == liga]
        if liga == "EGYPT - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "ENGLAND - EFL CUP":
            df = base[base.League == liga]
        if liga == "ENGLAND - FA CUP":
            df = base[base.League == liga]
        if liga == "ENGLAND - LEAGUE ONE":
            df = base[base.League == liga]
        if liga == "ENGLAND - LEAGUE TWO":
            df = base[base.League == liga]
        if liga == "ENGLAND - NATIONAL LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - PREMIER LEAGUE 2":
            df = base[base.League == liga]
        if liga == "ESTONIA - ESILIIGA":
            df = base[base.League == liga]
        if liga == "ESTONIA - MEISTRILIIGA":
            df = base[base.League == liga]
        if liga == "EUROPE - CHAMPIONS LEAGUE":
            df = base[base.League == liga]
        if liga == "EUROPE - EUROPA CONFERENCE LEAGUE":
            df = base[base.League == liga]
        if liga == "EUROPE - EUROPA LEAGUE":
            df = base[base.League == liga]
        if liga == "FIJI - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "FINLAND - VEIKKAUSLIIGA":
            df = base[base.League == liga]
        if liga == "FINLAND - YKKONEN":
            df = base[base.League == liga]
        if liga == "FRANCE - LIGUE 1":
            df = base[base.League == liga]
        if liga == "FRANCE - LIGUE 2":
            df = base[base.League == liga]
        if liga == "FRANCE - NATIONAL":
            df = base[base.League == liga]
        if liga == "GEORGIA - CRYSTALBET EROVNULI LIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - 2. BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - 3. LIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - DFB POKAL":
            df = base[base.League == liga]
        if liga == "GHANA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "GREECE - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "GUATEMALA - LIGA NACIONAL":
            df = base[base.League == liga]
        if liga == "HONDURAS - LIGA NACIONAL":
            df = base[base.League == liga]
        if liga == "HONG KONG - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "HUNGARY - OTP BANK LIGA":
            df = base[base.League == liga]
        if liga == "ICELAND - BESTA DEILD KARLA":
            df = base[base.League == liga]
        if liga == "INDIA - I-LEAGUE":
            df = base[base.League == liga]
        if liga == "INDIA - ISL":
            df = base[base.League == liga]
        if liga == "INDONESIA - LIGA 1":
            df = base[base.League == liga]
        if liga == "IRAN - PERSIAN GULF PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "IRAQ - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "IRELAND - DIVISION 1":
            df = base[base.League == liga]
        if liga == "IRELAND - PREMIER DIVISION":
            df = base[base.League == liga]
        if liga == "ISRAEL - LIGAT HA'AL":
            df = base[base.League == liga]
        if liga == "ITALY - COPPA ITALIA":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE A":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE B":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE C":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE D":
            df = base[base.League == liga]
        if liga == "IVORY COAST - LIGUE 1":
            df = base[base.League == liga]
        if liga == "JAMAICA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "JAPAN - J1 LEAGUE":
            df = base[base.League == liga]
        if liga == "JAPAN - J2 LEAGUE":
            df = base[base.League == liga]
        if liga == "LITHUANIA - A LYGA":
            df = base[base.League == liga]
        if liga == "LUXEMBOURG - NATIONAL DIVISION":
            df = base[base.League == liga]
        if liga == "MALTA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "MEXICO - LIGA DE EXPANSION MX":
            df = base[base.League == liga]
        if liga == "MEXICO - LIGA MX":
            df = base[base.League == liga]
        if liga == "MOLDOVA - SUPER LIGA":
            df = base[base.League == liga]
        if liga == "MONGOLIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "MONTENEGRO - PRVA CRNOGORSKA LIGA":
            df = base[base.League == liga]
        if liga == "MOROCCO - BOTOLA PRO":
            df = base[base.League == liga]
        if liga == "MOZAMBIQUE - MOCAMBOLA":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - DERDE DIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - EERSTE DIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - EREDIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - TWEEDE DIVISIE":
            df = base[base.League == liga]
        if liga == "NICARAGUA - LIGA PRIMERA":
            df = base[base.League == liga]
        if liga == "NIGERIA - NPFL":
            df = base[base.League == liga]
        if liga == "NORTH MACEDONIA - 1. MFL":
            df = base[base.League == liga]
        if liga == "NORTHERN IRELAND - NIFL CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "NORTHERN IRELAND - NIFL PREMIERSHIP":
            df = base[base.League == liga]
        if liga == "NORWAY - ELITESERIEN":
            df = base[base.League == liga]
        if liga == "NORWAY - OBOS-LIGAEN":
            df = base[base.League == liga]
        if liga == "PANAMA - LPF":
            df = base[base.League == liga]
        if liga == "PARAGUAY - DIVISION INTERMEDIA":
            df = base[base.League == liga]
        if liga == "PARAGUAY - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "PERU - LIGA 1":
            df = base[base.League == liga]
        if liga == "PERU - LIGA 2":
            df = base[base.League == liga]
        if liga == "PHILIPPINES - PFL":
            df = base[base.League == liga]
        if liga == "POLAND - DIVISION 1":
            df = base[base.League == liga]
        if liga == "POLAND - EKSTRAKLASA":
            df = base[base.League == liga]
        if liga == "PORTUGAL - LIGA PORTUGAL":
            df = base[base.League == liga]
        if liga == "PORTUGAL - LIGA PORTUGAL 2":
            df = base[base.League == liga]
        if liga == "PORTUGAL - TAÇA DE PORTUGAL":
            df = base[base.League == liga]
        if liga == "QATAR - QSL":    
            df = base[base.League == liga]
        if liga == "ROMANIA - LIGA 1":
            df = base[base.League == liga]
        if liga == "ROMANIA - LIGA 2":   
            df = base[base.League == liga]
        if liga == "RUSSIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "SAN MARINO - CAMPIONATO SAMMARINESE":
            df = base[base.League == liga]
        if liga == "SAUDI ARABIA - SAUDI PROFESSIONAL LEAGUE":
            df = base[base.League == liga]
        if liga == "SCOTLAND - CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "SCOTLAND - LEAGUE ONE":
            df = base[base.League == liga]
        if liga == "SCOTLAND - LEAGUE TWO":
            df = base[base.League == liga]
        if liga == "SCOTLAND - PREMIERSHIP":
            df = base[base.League == liga]
        if liga == "SENEGAL - LIGUE 1":   
            df = base[base.League == liga]
        if liga == "SERBIA - PRVA LIGA":  
            df = base[base.League == liga]
        if liga == "SERBIA - SUPER LIGA": 
            df = base[base.League == liga]
        if liga == "SINGAPORE - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "SLOVAKIA - NIKE LIGA":
            df = base[base.League == liga]
        if liga == "SLOVENIA - PRVA LIGA":
            df = base[base.League == liga]
        if liga == "SOUTH AMERICA - COPA LIBERTADORES":
            df = base[base.League == liga]
        if liga == "SOUTH AMERICA - COPA SUDAMERICANA":
            df = base[base.League == liga]
        if liga == "SOUTH KOREA - K LEAGUE 1":
            df = base[base.League == liga]
        if liga == "SOUTH KOREA - K LEAGUE 2":
            df = base[base.League == liga]
        if liga == "SPAIN - COPA DEL REY":
            df = base[base.League == liga]
        if liga == "SPAIN - LALIGA":
            df = base[base.League == liga]
        if liga == "SPAIN - LALIGA2":   
            df = base[base.League == liga]
        if liga == "SPAIN - PRIMERA RFEF":
            df = base[base.League == liga]
        if liga == "SPAIN - SEGUNDA RFEF":
            df = base[base.League == liga]
        if liga == "SWEDEN - ALLSVENSKAN":
            df = base[base.League == liga]
        if liga == "SWEDEN - SUPERETTAN": 
            df = base[base.League == liga]
        if liga == "SWITZERLAND - CHALLENGE LEAGUE":
            df = base[base.League == liga]
        if liga == "SWITZERLAND - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "THAILAND - THAI LEAGUE 1":
            df = base[base.League == liga]
        if liga == "THAILAND - THAI LEAGUE 2":
            df = base[base.League == liga]
        if liga == "TUNISIA - LIGUE PROFESSIONNELLE 1":
            df = base[base.League == liga]
        if liga == "TURKEY - 1. LIG":    
            df = base[base.League == liga]
        if liga == "TURKEY - SUPER LIG":
            df = base[base.League == liga]
        if liga == "UGANDA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "UKRAINE - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "UNITED ARAB EMIRATES - UAE LEAGUE": 
            df = base[base.League == liga]
        if liga == "URUGUAY - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "URUGUAY - SEGUNDA DIVISION":
            df = base[base.League == liga]
        if liga == "USA - MLS":    
            df = base[base.League == liga]
        if liga == "USA - USL CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "UZBEKISTAN - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "VENEZUELA - LIGA FUTVE":
            df = base[base.League == liga]
        if liga == "VENEZUELA - LIGA FUTVE 2":
            df = base[base.League == liga]
        if liga == "VIETNAM - V.LEAGUE 1":
            df = base[base.League == liga]
        if liga == "WALES - CYMRU PREMIER":
            df = base[base.League == liga]
        
        df["FT_Goals_H"] = df["FT_Goals_H"].astype('int64')
        df["FT_Goals_A"] = df["FT_Goals_A"].astype('int64')
        df['FT_Odd_Over05'] = pd.to_numeric(df['FT_Odd_Over05'],errors = 'coerce')
        df['FT_Odd_Under05'] = pd.to_numeric(df['FT_Odd_Under05'],errors = 'coerce')
        
        total_count = len(df.index)
        df["Date"] = pd.to_datetime(df["Date"])
        df['Date'] = df['Date'].dt.date

        winHPLValues = 100 * df.FT_Odd_Over05 - 100
        winAPLValues = 100 * df.FT_Odd_Over05 - 100
        losePLValues = -100

        df.loc[(((df['FT_Goals_H']) + (df['FT_Goals_A'])) > 0), 'Result_FT'] = 'H'
        df.loc[(((df['FT_Goals_H']) + (df['FT_Goals_A'])) < 1), 'Result_FT'] = 'A'

        df['H'] = winHPLValues.where(df.Result_FT == 'H', other=losePLValues)
        df['A'] = winAPLValues.where(df.Result_FT == 'A', other=losePLValues)

        no_of_days = 0

        matchDates = df.Date.unique()

        if no_of_days > 0:
            matchDates = (matchDates[-no_of_days:])
                
        df2 = pd.DataFrame()

        rowsIndex = []
        rowsDate = []
        rowsH = []
        rowsA = []

        count = 0
        for mDate in matchDates:
            count += 1
            rowsDate.append(mDate)
            rowsH.append(df.loc[df['Date'] == mDate]['H'].sum())
            rowsA.append(df.loc[df['Date'] == mDate]['A'].sum())

        df2['Date'] = rowsDate
        df2['H'] = rowsH
        df2['A'] = rowsA

        df2 = df2.tail(101)
        df2 = df2.reset_index(drop=True)
        df2['Id'] = df2.reset_index()['index'].rename('index_copy')
        df2['Id'] = df2['Id'] + 1
        df2 = df2[['Id','Date','H','A']]

        df2['Hacu'] = df2.H.cumsum()
        df2['Aacu'] = df2.A.cumsum()

        df2['Hacu'].loc[0] = np.nan
        df2['Aacu'].loc[0] = np.nan

        def weighted_mean_H(s):
            d = df2.loc[s.index, 'Hacu']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_H_C(s):
            d = df2.loc[s.index, 'waHC']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_A(s):
            d = df2.loc[s.index, 'Aacu']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_A_C(s):
            d = df2.loc[s.index, 'waAC']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        df2['waH16'] = df2.rolling(16)['Hacu'].apply(weighted_mean_H, raw=False)
        df2['waH8'] = df2.rolling(8)['Hacu'].apply(weighted_mean_H, raw=False)
        df2['waHC'] = 2*df2.waH8-df2.waH16
        df2['waH4'] = df2.rolling(4)['waHC'].apply(weighted_mean_H_C, raw=False)

        df2['waA16'] = df2.rolling(16)['Aacu'].apply(weighted_mean_A, raw=False)
        df2['waA8'] = df2.rolling(8)['Aacu'].apply(weighted_mean_A, raw=False)
        df2['waAC'] = 2*df2.waA8-df2.waA16
        df2['waA4'] = df2.rolling(4)['waAC'].apply(weighted_mean_A_C, raw=False)

        df2['Hhull'] = df2['waH4']
        df2['Ahull'] = df2['waA4']

        df2['Hdist'] = (df2.Hacu / df2.Hhull)
        df2['Adist'] = (df2.Aacu / df2.Ahull)

        def r_function(s):
            f = s.loc[s.index.values[0]]
            l = s.loc[s.index.values[1]]
            return (l -f)/abs(f)

        df2['Hr'] = df2['Hhull'].rolling(2).apply(r_function, raw=False)
        df2['Ar'] = df2['Ahull'].rolling(2).apply(r_function, raw=False)

        def inc_H(s):
            x = df2.loc[s.index, 'Id']
            y = df2.loc[s.index, 'Hhull']
            slope, intercept = np.polyfit(x, y , 1)
            return slope

        def inc_A(s):
            x = df2.loc[s.index, 'Id']
            y = df2.loc[s.index, 'Ahull']
            slope, intercept = np.polyfit(x, y, 1)
            return slope
        
        df2['Hinc'] = df2['Hhull'].rolling(5).apply(inc_H, raw=False)
        df2['Ainc'] = df2['Ahull'].rolling(5).apply(inc_A, raw=False)

        df2['Hdp'] = df2['Hacu'].rolling(10).std()
        df2['Adp'] = df2['Aacu'].rolling(10).std()

        df2['Hamp'] = df2['Hacu'].rolling(10).max() / df2['Hacu'].rolling(10).min()
        df2['Aamp'] = df2['Aacu'].rolling(10).max() / df2['Aacu'].rolling(10).min()
        
        df3 = pd.DataFrame()

        def normaliz(dfS):
            actual_value = (dfS.loc[dfS.index.values[4]])
            try:
                n = (actual_value - dfS.min()) / (dfS.max() - dfS.min())
                if math.isnan(n):
                    return 0
            except ZeroDivisionError:
                return 0
            return n

        
        df3['Id'] = df2['Id'].iloc[23:]

        df3['Hhull'] = df2['Hhull'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Ahull'] = df2['Ahull'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hdist'] = df2['Hdist'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Adist'] = df2['Adist'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hr'] = df2['Hr'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Ar'] = df2['Ar'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hinc'] = df2['Hinc'].rolling(5).apply(normaliz, raw=False)
        df3['Ainc'] = df2['Ainc'].rolling(5).apply(normaliz, raw=False)

        df3['Hdp'] = df2['Hdp'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Adp'] = df2['Adp'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hamp'] = df2['Hamp'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Aamp'] = df2['Aamp'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['R'] = ''

        for index, row in df2.iterrows():
            if index > 26:
                try:
                    h = df2.iloc[(index+1)].H
                    a = df2.iloc[(index+1)].A
                    if h > a:
                        df3.loc[index, 'R'] = 'Over05'
                    else:
                        df3.loc[index, 'R'] = 'Under05'
                except LookupError:
                    pass

        selected_date = df3.iloc[-1]

        distance_columns = ['Hhull', 'Ahull', 'Hdist', 'Adist', 'Hr', 'Ar', 'Hinc', 'Ainc', 'Hdp', 'Adp', 'Hamp', 'Aamp']

        def euclidean_distance(row):
            """
            A simple euclidean distance function
            """
            inner_value = 0
            for k in distance_columns:
                inner_value += (row[k] - selected_date[k]) ** 2
            return math.sqrt(inner_value)

        def euclidean_distance_tr(row):
            inner_value = 0
            for k in distance_columns:
                inner_value += abs(row[k] - selected_date[k])
            return inner_value
        

        df3['eucli'] = df3.apply(euclidean_distance_tr, axis=1)
        
        
        df4 = pd.DataFrame()
        df4['R'] = df3['R']
        df4['eucli'] = df3['eucli']
        df4.sort_values(by=['eucli'], inplace=True)


        teoria_dos_retornos = {}
      
        try:
            #teoria_dos_retornos["Date"] = datetime.today().strftime('%Y-%m-%d')
            teoria_dos_retornos["League"] = liga
            teoria_dos_retornos["N1"] = df4[df4.eucli != 0]['R'].iloc[0]
        except:
            teoria_dos_retornos["N1"] = 0
        try:
            teoria_dos_retornos["N2"] = df4[df4.eucli != 0]['R'].iloc[1]
        except:
            teoria_dos_retornos["N2"] = 0
        try:
            teoria_dos_retornos["N3"] = df4[df4.eucli != 0]['R'].iloc[2]
        except:
            teoria_dos_retornos["N3"] = 0

        lista.append(teoria_dos_retornos)

lista = [ ]
TR()
df00 = pd.DataFrame(lista)
Jogos_do_Dia = jogos_do_dia.merge(df00, on=['League'])
Jogos_do_Dia.reset_index(inplace=True, drop=True)
Jogos_do_Dia.index = Jogos_do_Dia.index.set_names(['Nº'])
Jogos_do_Dia = Jogos_do_Dia.rename(index=lambda x: x + 1)

from futpythontrader import *
# Gerando os dados para excel
hoje = data.strftime('%Y-%m-%d')
nome = 'Teoria_dos_Retornos_Over_Under_05ft_ARKAD.csv'
df00.to_csv(f'./Teoria_dos_Retornos/{data}_{nome}', index = False)
df00


# In[7]:


def TR():
    for i in ligas:
        liga = i
        
        
        if liga == "ARMENIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ALBANIA - SUPERLIGA":
            df = base[base.League == liga]
        if liga == "ANDORRA - PRIMERA DIVISIÓ":
            df = base[base.League == liga]
        if liga == "ANGOLA - GIRABOLA":
            df = base[base.League == liga]
        if liga == "ARGENTINA - COPA DE LA LIGA PROFESIONAL":
            df = base[base.League == liga]
        if liga == "ARGENTINA - LIGA PROFESIONAL":
            df = base[base.League == liga]
        if liga == "ARGENTINA - PRIMERA NACIONAL":
            df = base[base.League == liga]
        if liga == "AUSTRALIA - A-LEAGUE":
            df = base[base.League == liga]
        if liga == "AUSTRIA - 2. LIGA":
            df = base[base.League == liga]
        if liga == "AUSTRIA - BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "AZERBAIJAN - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "BANGLADESH - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "BELARUS - VYSSHAYA LIGA":
            df = base[base.League == liga]
        if liga == "BELGIUM - CHALLENGER PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "BELGIUM - JUPILER PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "BOLIVIA - DIVISION PROFESIONAL":
            df = base[base.League == liga]
        if liga == "BOLIVIA - NACIONAL B":
            df = base[base.League == liga]
        if liga == "BOSNIA AND HERZEGOVINA - PREMIJER LIGA BIH":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO U20":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO U23":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO WOMEN":
            df = base[base.League == liga]
        if liga == "BRAZIL - COPA DO BRASIL":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE A":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE B":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE C":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE D":
            df = base[base.League == liga]
        if liga == "BULGARIA - PARVA LIGA":
            df = base[base.League == liga]
        if liga == "CAMEROON - ELITE ONE":
            df = base[base.League == liga]
        if liga == "CANADA - CANADIAN PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "CHILE - PRIMERA B":
            df = base[base.League == liga]
        if liga == "CHILE - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "CHINA - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "COLOMBIA - PRIMERA A":
            df = base[base.League == liga]
        if liga == "COLOMBIA - PRIMERA B":
            df = base[base.League == liga]
        if liga == "COSTA RICA - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "CROATIA - HNL":
            df = base[base.League == liga]
        if liga == "CROATIA - PRVA NL":
            df = base[base.League == liga]
        if liga == "CYPRUS - CYTA CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "CZECH REPUBLIC - FORTUNA:LIGA":
            df = base[base.League == liga]
        if liga == "DENMARK - 1ST DIVISION":
            df = base[base.League == liga]
        if liga == "DENMARK - SUPERLIGA":
            df = base[base.League == liga]
        if liga == "DOMINICAN REPUBLIC - LDF":
            df = base[base.League == liga]
        if liga == "ECUADOR - LIGA PRO":
            df = base[base.League == liga]
        if liga == "ECUADOR - SERIE B":
            df = base[base.League == liga]
        if liga == "EGYPT - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "ENGLAND - EFL CUP":
            df = base[base.League == liga]
        if liga == "ENGLAND - FA CUP":
            df = base[base.League == liga]
        if liga == "ENGLAND - LEAGUE ONE":
            df = base[base.League == liga]
        if liga == "ENGLAND - LEAGUE TWO":
            df = base[base.League == liga]
        if liga == "ENGLAND - NATIONAL LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - PREMIER LEAGUE 2":
            df = base[base.League == liga]
        if liga == "ESTONIA - ESILIIGA":
            df = base[base.League == liga]
        if liga == "ESTONIA - MEISTRILIIGA":
            df = base[base.League == liga]
        if liga == "EUROPE - CHAMPIONS LEAGUE":
            df = base[base.League == liga]
        if liga == "EUROPE - EUROPA CONFERENCE LEAGUE":
            df = base[base.League == liga]
        if liga == "EUROPE - EUROPA LEAGUE":
            df = base[base.League == liga]
        if liga == "FIJI - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "FINLAND - VEIKKAUSLIIGA":
            df = base[base.League == liga]
        if liga == "FINLAND - YKKONEN":
            df = base[base.League == liga]
        if liga == "FRANCE - LIGUE 1":
            df = base[base.League == liga]
        if liga == "FRANCE - LIGUE 2":
            df = base[base.League == liga]
        if liga == "FRANCE - NATIONAL":
            df = base[base.League == liga]
        if liga == "GEORGIA - CRYSTALBET EROVNULI LIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - 2. BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - 3. LIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - DFB POKAL":
            df = base[base.League == liga]
        if liga == "GHANA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "GREECE - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "GUATEMALA - LIGA NACIONAL":
            df = base[base.League == liga]
        if liga == "HONDURAS - LIGA NACIONAL":
            df = base[base.League == liga]
        if liga == "HONG KONG - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "HUNGARY - OTP BANK LIGA":
            df = base[base.League == liga]
        if liga == "ICELAND - BESTA DEILD KARLA":
            df = base[base.League == liga]
        if liga == "INDIA - I-LEAGUE":
            df = base[base.League == liga]
        if liga == "INDIA - ISL":
            df = base[base.League == liga]
        if liga == "INDONESIA - LIGA 1":
            df = base[base.League == liga]
        if liga == "IRAN - PERSIAN GULF PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "IRAQ - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "IRELAND - DIVISION 1":
            df = base[base.League == liga]
        if liga == "IRELAND - PREMIER DIVISION":
            df = base[base.League == liga]
        if liga == "ISRAEL - LIGAT HA'AL":
            df = base[base.League == liga]
        if liga == "ITALY - COPPA ITALIA":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE A":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE B":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE C":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE D":
            df = base[base.League == liga]
        if liga == "IVORY COAST - LIGUE 1":
            df = base[base.League == liga]
        if liga == "JAMAICA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "JAPAN - J1 LEAGUE":
            df = base[base.League == liga]
        if liga == "JAPAN - J2 LEAGUE":
            df = base[base.League == liga]
        if liga == "LITHUANIA - A LYGA":
            df = base[base.League == liga]
        if liga == "LUXEMBOURG - NATIONAL DIVISION":
            df = base[base.League == liga]
        if liga == "MALTA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "MEXICO - LIGA DE EXPANSION MX":
            df = base[base.League == liga]
        if liga == "MEXICO - LIGA MX":
            df = base[base.League == liga]
        if liga == "MOLDOVA - SUPER LIGA":
            df = base[base.League == liga]
        if liga == "MONGOLIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "MONTENEGRO - PRVA CRNOGORSKA LIGA":
            df = base[base.League == liga]
        if liga == "MOROCCO - BOTOLA PRO":
            df = base[base.League == liga]
        if liga == "MOZAMBIQUE - MOCAMBOLA":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - DERDE DIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - EERSTE DIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - EREDIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - TWEEDE DIVISIE":
            df = base[base.League == liga]
        if liga == "NICARAGUA - LIGA PRIMERA":
            df = base[base.League == liga]
        if liga == "NIGERIA - NPFL":
            df = base[base.League == liga]
        if liga == "NORTH MACEDONIA - 1. MFL":
            df = base[base.League == liga]
        if liga == "NORTHERN IRELAND - NIFL CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "NORTHERN IRELAND - NIFL PREMIERSHIP":
            df = base[base.League == liga]
        if liga == "NORWAY - ELITESERIEN":
            df = base[base.League == liga]
        if liga == "NORWAY - OBOS-LIGAEN":
            df = base[base.League == liga]
        if liga == "PANAMA - LPF":
            df = base[base.League == liga]
        if liga == "PARAGUAY - DIVISION INTERMEDIA":
            df = base[base.League == liga]
        if liga == "PARAGUAY - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "PERU - LIGA 1":
            df = base[base.League == liga]
        if liga == "PERU - LIGA 2":
            df = base[base.League == liga]
        if liga == "PHILIPPINES - PFL":
            df = base[base.League == liga]
        if liga == "POLAND - DIVISION 1":
            df = base[base.League == liga]
        if liga == "POLAND - EKSTRAKLASA":
            df = base[base.League == liga]
        if liga == "PORTUGAL - LIGA PORTUGAL":
            df = base[base.League == liga]
        if liga == "PORTUGAL - LIGA PORTUGAL 2":
            df = base[base.League == liga]
        if liga == "PORTUGAL - TAÇA DE PORTUGAL":
            df = base[base.League == liga]
        if liga == "QATAR - QSL":    
            df = base[base.League == liga]
        if liga == "ROMANIA - LIGA 1":
            df = base[base.League == liga]
        if liga == "ROMANIA - LIGA 2":   
            df = base[base.League == liga]
        if liga == "RUSSIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "SAN MARINO - CAMPIONATO SAMMARINESE":
            df = base[base.League == liga]
        if liga == "SAUDI ARABIA - SAUDI PROFESSIONAL LEAGUE":
            df = base[base.League == liga]
        if liga == "SCOTLAND - CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "SCOTLAND - LEAGUE ONE":
            df = base[base.League == liga]
        if liga == "SCOTLAND - LEAGUE TWO":
            df = base[base.League == liga]
        if liga == "SCOTLAND - PREMIERSHIP":
            df = base[base.League == liga]
        if liga == "SENEGAL - LIGUE 1":   
            df = base[base.League == liga]
        if liga == "SERBIA - PRVA LIGA":  
            df = base[base.League == liga]
        if liga == "SERBIA - SUPER LIGA": 
            df = base[base.League == liga]
        if liga == "SINGAPORE - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "SLOVAKIA - NIKE LIGA":
            df = base[base.League == liga]
        if liga == "SLOVENIA - PRVA LIGA":
            df = base[base.League == liga]
        if liga == "SOUTH AMERICA - COPA LIBERTADORES":
            df = base[base.League == liga]
        if liga == "SOUTH AMERICA - COPA SUDAMERICANA":
            df = base[base.League == liga]
        if liga == "SOUTH KOREA - K LEAGUE 1":
            df = base[base.League == liga]
        if liga == "SOUTH KOREA - K LEAGUE 2":
            df = base[base.League == liga]
        if liga == "SPAIN - COPA DEL REY":
            df = base[base.League == liga]
        if liga == "SPAIN - LALIGA":
            df = base[base.League == liga]
        if liga == "SPAIN - LALIGA2":   
            df = base[base.League == liga]
        if liga == "SPAIN - PRIMERA RFEF":
            df = base[base.League == liga]
        if liga == "SPAIN - SEGUNDA RFEF":
            df = base[base.League == liga]
        if liga == "SWEDEN - ALLSVENSKAN":
            df = base[base.League == liga]
        if liga == "SWEDEN - SUPERETTAN": 
            df = base[base.League == liga]
        if liga == "SWITZERLAND - CHALLENGE LEAGUE":
            df = base[base.League == liga]
        if liga == "SWITZERLAND - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "THAILAND - THAI LEAGUE 1":
            df = base[base.League == liga]
        if liga == "THAILAND - THAI LEAGUE 2":
            df = base[base.League == liga]
        if liga == "TUNISIA - LIGUE PROFESSIONNELLE 1":
            df = base[base.League == liga]
        if liga == "TURKEY - 1. LIG":    
            df = base[base.League == liga]
        if liga == "TURKEY - SUPER LIG":
            df = base[base.League == liga]
        if liga == "UGANDA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "UKRAINE - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "UNITED ARAB EMIRATES - UAE LEAGUE": 
            df = base[base.League == liga]
        if liga == "URUGUAY - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "URUGUAY - SEGUNDA DIVISION":
            df = base[base.League == liga]
        if liga == "USA - MLS":    
            df = base[base.League == liga]
        if liga == "USA - USL CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "UZBEKISTAN - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "VENEZUELA - LIGA FUTVE":
            df = base[base.League == liga]
        if liga == "VENEZUELA - LIGA FUTVE 2":
            df = base[base.League == liga]
        if liga == "VIETNAM - V.LEAGUE 1":
            df = base[base.League == liga]
        if liga == "WALES - CYMRU PREMIER":
            df = base[base.League == liga]
        
        df["FT_Goals_H"] = df["FT_Goals_H"].astype('int64')
        df["FT_Goals_A"] = df["FT_Goals_A"].astype('int64')
        df['FT_Odd_Over25'] = pd.to_numeric(df['FT_Odd_Over25'],errors = 'coerce')
        df['FT_Odd_Under25'] = pd.to_numeric(df['FT_Odd_Under25'],errors = 'coerce')
        
        total_count = len(df.index)
        df["Date"] = pd.to_datetime(df["Date"])
        df['Date'] = df['Date'].dt.date

        winHPLValues = 100 * df.FT_Odd_Over25 - 100
        winAPLValues = 100 * df.FT_Odd_Over25 - 100
        losePLValues = -100

        df.loc[(((df['FT_Goals_H']) + (df['FT_Goals_A'])) > 2), 'Result_FT'] = 'H'
        df.loc[(((df['FT_Goals_H']) + (df['FT_Goals_A'])) < 3), 'Result_FT'] = 'A'

        df['H'] = winHPLValues.where(df.Result_FT == 'H', other=losePLValues)
        df['A'] = winAPLValues.where(df.Result_FT == 'A', other=losePLValues)

        no_of_days = 0

        matchDates = df.Date.unique()

        if no_of_days > 0:
            matchDates = (matchDates[-no_of_days:])
                
        df2 = pd.DataFrame()

        rowsIndex = []
        rowsDate = []
        rowsH = []
        rowsA = []

        count = 0
        for mDate in matchDates:
            count += 1
            rowsDate.append(mDate)
            rowsH.append(df.loc[df['Date'] == mDate]['H'].sum())
            rowsA.append(df.loc[df['Date'] == mDate]['A'].sum())

        df2['Date'] = rowsDate
        df2['H'] = rowsH
        df2['A'] = rowsA

        df2 = df2.tail(101)
        df2 = df2.reset_index(drop=True)
        df2['Id'] = df2.reset_index()['index'].rename('index_copy')
        df2['Id'] = df2['Id'] + 1
        df2 = df2[['Id','Date','H','A']]

        df2['Hacu'] = df2.H.cumsum()
        df2['Aacu'] = df2.A.cumsum()

        df2['Hacu'].loc[0] = np.nan
        df2['Aacu'].loc[0] = np.nan

        def weighted_mean_H(s):
            d = df2.loc[s.index, 'Hacu']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_H_C(s):
            d = df2.loc[s.index, 'waHC']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_A(s):
            d = df2.loc[s.index, 'Aacu']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_A_C(s):
            d = df2.loc[s.index, 'waAC']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        df2['waH16'] = df2.rolling(16)['Hacu'].apply(weighted_mean_H, raw=False)
        df2['waH8'] = df2.rolling(8)['Hacu'].apply(weighted_mean_H, raw=False)
        df2['waHC'] = 2*df2.waH8-df2.waH16
        df2['waH4'] = df2.rolling(4)['waHC'].apply(weighted_mean_H_C, raw=False)

        df2['waA16'] = df2.rolling(16)['Aacu'].apply(weighted_mean_A, raw=False)
        df2['waA8'] = df2.rolling(8)['Aacu'].apply(weighted_mean_A, raw=False)
        df2['waAC'] = 2*df2.waA8-df2.waA16
        df2['waA4'] = df2.rolling(4)['waAC'].apply(weighted_mean_A_C, raw=False)

        df2['Hhull'] = df2['waH4']
        df2['Ahull'] = df2['waA4']

        df2['Hdist'] = (df2.Hacu / df2.Hhull)
        df2['Adist'] = (df2.Aacu / df2.Ahull)

        def r_function(s):
            f = s.loc[s.index.values[0]]
            l = s.loc[s.index.values[1]]
            return (l -f)/abs(f)

        df2['Hr'] = df2['Hhull'].rolling(2).apply(r_function, raw=False)
        df2['Ar'] = df2['Ahull'].rolling(2).apply(r_function, raw=False)

        def inc_H(s):
            x = df2.loc[s.index, 'Id']
            y = df2.loc[s.index, 'Hhull']
            slope, intercept = np.polyfit(x, y , 1)
            return slope

        def inc_A(s):
            x = df2.loc[s.index, 'Id']
            y = df2.loc[s.index, 'Ahull']
            slope, intercept = np.polyfit(x, y, 1)
            return slope
        
        df2['Hinc'] = df2['Hhull'].rolling(5).apply(inc_H, raw=False)
        df2['Ainc'] = df2['Ahull'].rolling(5).apply(inc_A, raw=False)

        df2['Hdp'] = df2['Hacu'].rolling(10).std()
        df2['Adp'] = df2['Aacu'].rolling(10).std()

        df2['Hamp'] = df2['Hacu'].rolling(10).max() / df2['Hacu'].rolling(10).min()
        df2['Aamp'] = df2['Aacu'].rolling(10).max() / df2['Aacu'].rolling(10).min()
        
        df3 = pd.DataFrame()

        def normaliz(dfS):
            actual_value = (dfS.loc[dfS.index.values[4]])
            try:
                n = (actual_value - dfS.min()) / (dfS.max() - dfS.min())
                if math.isnan(n):
                    return 0
            except ZeroDivisionError:
                return 0
            return n

        
        df3['Id'] = df2['Id'].iloc[23:]

        df3['Hhull'] = df2['Hhull'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Ahull'] = df2['Ahull'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hdist'] = df2['Hdist'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Adist'] = df2['Adist'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hr'] = df2['Hr'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Ar'] = df2['Ar'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hinc'] = df2['Hinc'].rolling(5).apply(normaliz, raw=False)
        df3['Ainc'] = df2['Ainc'].rolling(5).apply(normaliz, raw=False)

        df3['Hdp'] = df2['Hdp'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Adp'] = df2['Adp'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hamp'] = df2['Hamp'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Aamp'] = df2['Aamp'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['R'] = ''

        for index, row in df2.iterrows():
            if index > 26:
                try:
                    h = df2.iloc[(index+1)].H
                    a = df2.iloc[(index+1)].A
                    if h > a:
                        df3.loc[index, 'R'] = 'Over25'
                    else:
                        df3.loc[index, 'R'] = 'Under25'
                except LookupError:
                    pass

        selected_date = df3.iloc[-1]

        distance_columns = ['Hhull', 'Ahull', 'Hdist', 'Adist', 'Hr', 'Ar', 'Hinc', 'Ainc', 'Hdp', 'Adp', 'Hamp', 'Aamp']

        def euclidean_distance(row):
            """
            A simple euclidean distance function
            """
            inner_value = 0
            for k in distance_columns:
                inner_value += (row[k] - selected_date[k]) ** 2
            return math.sqrt(inner_value)

        def euclidean_distance_tr(row):
            inner_value = 0
            for k in distance_columns:
                inner_value += abs(row[k] - selected_date[k])
            return inner_value
        

        df3['eucli'] = df3.apply(euclidean_distance_tr, axis=1)
        
        
        df4 = pd.DataFrame()
        df4['R'] = df3['R']
        df4['eucli'] = df3['eucli']
        df4.sort_values(by=['eucli'], inplace=True)


        teoria_dos_retornos = {}
      
        try:
            #teoria_dos_retornos["Date"] = datetime.today().strftime('%Y-%m-%d')
            teoria_dos_retornos["League"] = liga
            teoria_dos_retornos["N1"] = df4[df4.eucli != 0]['R'].iloc[0]
        except:
            teoria_dos_retornos["N1"] = 0
        try:
            teoria_dos_retornos["N2"] = df4[df4.eucli != 0]['R'].iloc[1]
        except:
            teoria_dos_retornos["N2"] = 0
        try:
            teoria_dos_retornos["N3"] = df4[df4.eucli != 0]['R'].iloc[2]
        except:
            teoria_dos_retornos["N3"] = 0

        lista.append(teoria_dos_retornos)

lista = [ ]
TR()
df00 = pd.DataFrame(lista)
Jogos_do_Dia = jogos_do_dia.merge(df00, on=['League'])
Jogos_do_Dia.reset_index(inplace=True, drop=True)
Jogos_do_Dia.index = Jogos_do_Dia.index.set_names(['Nº'])
Jogos_do_Dia = Jogos_do_Dia.rename(index=lambda x: x + 1)

from futpythontrader import *
# Gerando os dados para excel
# data = date.today()  + timedelta(1)
hoje = data.strftime('%Y-%m-%d')
nome = 'Teoria_dos_Retornos_Over_Under_25_ARKAD.csv'
df00.to_csv(f'./Teoria_dos_Retornos/{data}_{nome}', index = False)
df00


# In[8]:


def TR():
    for i in ligas:
        liga = i
        
        if liga == "ARMENIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ALBANIA - SUPERLIGA":
            df = base[base.League == liga]
        if liga == "ANDORRA - PRIMERA DIVISIÓ":
            df = base[base.League == liga]
        if liga == "ANGOLA - GIRABOLA":
            df = base[base.League == liga]
        if liga == "ARGENTINA - COPA DE LA LIGA PROFESIONAL":
            df = base[base.League == liga]
        if liga == "ARGENTINA - LIGA PROFESIONAL":
            df = base[base.League == liga]
        if liga == "ARGENTINA - PRIMERA NACIONAL":
            df = base[base.League == liga]
        if liga == "AUSTRALIA - A-LEAGUE":
            df = base[base.League == liga]
        if liga == "AUSTRIA - 2. LIGA":
            df = base[base.League == liga]
        if liga == "AUSTRIA - BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "AZERBAIJAN - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "BANGLADESH - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "BELARUS - VYSSHAYA LIGA":
            df = base[base.League == liga]
        if liga == "BELGIUM - CHALLENGER PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "BELGIUM - JUPILER PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "BOLIVIA - DIVISION PROFESIONAL":
            df = base[base.League == liga]
        if liga == "BOLIVIA - NACIONAL B":
            df = base[base.League == liga]
        if liga == "BOSNIA AND HERZEGOVINA - PREMIJER LIGA BIH":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO U20":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO U23":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO WOMEN":
            df = base[base.League == liga]
        if liga == "BRAZIL - COPA DO BRASIL":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE A":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE B":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE C":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE D":
            df = base[base.League == liga]
        if liga == "BULGARIA - PARVA LIGA":
            df = base[base.League == liga]
        if liga == "CAMEROON - ELITE ONE":
            df = base[base.League == liga]
        if liga == "CANADA - CANADIAN PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "CHILE - PRIMERA B":
            df = base[base.League == liga]
        if liga == "CHILE - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "CHINA - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "COLOMBIA - PRIMERA A":
            df = base[base.League == liga]
        if liga == "COLOMBIA - PRIMERA B":
            df = base[base.League == liga]
        if liga == "COSTA RICA - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "CROATIA - HNL":
            df = base[base.League == liga]
        if liga == "CROATIA - PRVA NL":
            df = base[base.League == liga]
        if liga == "CYPRUS - CYTA CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "CZECH REPUBLIC - FORTUNA:LIGA":
            df = base[base.League == liga]
        if liga == "DENMARK - 1ST DIVISION":
            df = base[base.League == liga]
        if liga == "DENMARK - SUPERLIGA":
            df = base[base.League == liga]
        if liga == "DOMINICAN REPUBLIC - LDF":
            df = base[base.League == liga]
        if liga == "ECUADOR - LIGA PRO":
            df = base[base.League == liga]
        if liga == "ECUADOR - SERIE B":
            df = base[base.League == liga]
        if liga == "EGYPT - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "ENGLAND - EFL CUP":
            df = base[base.League == liga]
        if liga == "ENGLAND - FA CUP":
            df = base[base.League == liga]
        if liga == "ENGLAND - LEAGUE ONE":
            df = base[base.League == liga]
        if liga == "ENGLAND - LEAGUE TWO":
            df = base[base.League == liga]
        if liga == "ENGLAND - NATIONAL LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - PREMIER LEAGUE 2":
            df = base[base.League == liga]
        if liga == "ESTONIA - ESILIIGA":
            df = base[base.League == liga]
        if liga == "ESTONIA - MEISTRILIIGA":
            df = base[base.League == liga]
        if liga == "EUROPE - CHAMPIONS LEAGUE":
            df = base[base.League == liga]
        if liga == "EUROPE - EUROPA CONFERENCE LEAGUE":
            df = base[base.League == liga]
        if liga == "EUROPE - EUROPA LEAGUE":
            df = base[base.League == liga]
        if liga == "FIJI - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "FINLAND - VEIKKAUSLIIGA":
            df = base[base.League == liga]
        if liga == "FINLAND - YKKONEN":
            df = base[base.League == liga]
        if liga == "FRANCE - LIGUE 1":
            df = base[base.League == liga]
        if liga == "FRANCE - LIGUE 2":
            df = base[base.League == liga]
        if liga == "FRANCE - NATIONAL":
            df = base[base.League == liga]
        if liga == "GEORGIA - CRYSTALBET EROVNULI LIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - 2. BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - 3. LIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - DFB POKAL":
            df = base[base.League == liga]
        if liga == "GHANA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "GREECE - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "GUATEMALA - LIGA NACIONAL":
            df = base[base.League == liga]
        if liga == "HONDURAS - LIGA NACIONAL":
            df = base[base.League == liga]
        if liga == "HONG KONG - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "HUNGARY - OTP BANK LIGA":
            df = base[base.League == liga]
        if liga == "ICELAND - BESTA DEILD KARLA":
            df = base[base.League == liga]
        if liga == "INDIA - I-LEAGUE":
            df = base[base.League == liga]
        if liga == "INDIA - ISL":
            df = base[base.League == liga]
        if liga == "INDONESIA - LIGA 1":
            df = base[base.League == liga]
        if liga == "IRAN - PERSIAN GULF PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "IRAQ - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "IRELAND - DIVISION 1":
            df = base[base.League == liga]
        if liga == "IRELAND - PREMIER DIVISION":
            df = base[base.League == liga]
        if liga == "ISRAEL - LIGAT HA'AL":
            df = base[base.League == liga]
        if liga == "ITALY - COPPA ITALIA":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE A":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE B":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE C":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE D":
            df = base[base.League == liga]
        if liga == "IVORY COAST - LIGUE 1":
            df = base[base.League == liga]
        if liga == "JAMAICA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "JAPAN - J1 LEAGUE":
            df = base[base.League == liga]
        if liga == "JAPAN - J2 LEAGUE":
            df = base[base.League == liga]
        if liga == "LITHUANIA - A LYGA":
            df = base[base.League == liga]
        if liga == "LUXEMBOURG - NATIONAL DIVISION":
            df = base[base.League == liga]
        if liga == "MALTA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "MEXICO - LIGA DE EXPANSION MX":
            df = base[base.League == liga]
        if liga == "MEXICO - LIGA MX":
            df = base[base.League == liga]
        if liga == "MOLDOVA - SUPER LIGA":
            df = base[base.League == liga]
        if liga == "MONGOLIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "MONTENEGRO - PRVA CRNOGORSKA LIGA":
            df = base[base.League == liga]
        if liga == "MOROCCO - BOTOLA PRO":
            df = base[base.League == liga]
        if liga == "MOZAMBIQUE - MOCAMBOLA":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - DERDE DIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - EERSTE DIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - EREDIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - TWEEDE DIVISIE":
            df = base[base.League == liga]
        if liga == "NICARAGUA - LIGA PRIMERA":
            df = base[base.League == liga]
        if liga == "NIGERIA - NPFL":
            df = base[base.League == liga]
        if liga == "NORTH MACEDONIA - 1. MFL":
            df = base[base.League == liga]
        if liga == "NORTHERN IRELAND - NIFL CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "NORTHERN IRELAND - NIFL PREMIERSHIP":
            df = base[base.League == liga]
        if liga == "NORWAY - ELITESERIEN":
            df = base[base.League == liga]
        if liga == "NORWAY - OBOS-LIGAEN":
            df = base[base.League == liga]
        if liga == "PANAMA - LPF":
            df = base[base.League == liga]
        if liga == "PARAGUAY - DIVISION INTERMEDIA":
            df = base[base.League == liga]
        if liga == "PARAGUAY - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "PERU - LIGA 1":
            df = base[base.League == liga]
        if liga == "PERU - LIGA 2":
            df = base[base.League == liga]
        if liga == "PHILIPPINES - PFL":
            df = base[base.League == liga]
        if liga == "POLAND - DIVISION 1":
            df = base[base.League == liga]
        if liga == "POLAND - EKSTRAKLASA":
            df = base[base.League == liga]
        if liga == "PORTUGAL - LIGA PORTUGAL":
            df = base[base.League == liga]
        if liga == "PORTUGAL - LIGA PORTUGAL 2":
            df = base[base.League == liga]
        if liga == "PORTUGAL - TAÇA DE PORTUGAL":
            df = base[base.League == liga]
        if liga == "QATAR - QSL":    
            df = base[base.League == liga]
        if liga == "ROMANIA - LIGA 1":
            df = base[base.League == liga]
        if liga == "ROMANIA - LIGA 2":   
            df = base[base.League == liga]
        if liga == "RUSSIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "SAN MARINO - CAMPIONATO SAMMARINESE":
            df = base[base.League == liga]
        if liga == "SAUDI ARABIA - SAUDI PROFESSIONAL LEAGUE":
            df = base[base.League == liga]
        if liga == "SCOTLAND - CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "SCOTLAND - LEAGUE ONE":
            df = base[base.League == liga]
        if liga == "SCOTLAND - LEAGUE TWO":
            df = base[base.League == liga]
        if liga == "SCOTLAND - PREMIERSHIP":
            df = base[base.League == liga]
        if liga == "SENEGAL - LIGUE 1":   
            df = base[base.League == liga]
        if liga == "SERBIA - PRVA LIGA":  
            df = base[base.League == liga]
        if liga == "SERBIA - SUPER LIGA": 
            df = base[base.League == liga]
        if liga == "SINGAPORE - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "SLOVAKIA - NIKE LIGA":
            df = base[base.League == liga]
        if liga == "SLOVENIA - PRVA LIGA":
            df = base[base.League == liga]
        if liga == "SOUTH AMERICA - COPA LIBERTADORES":
            df = base[base.League == liga]
        if liga == "SOUTH AMERICA - COPA SUDAMERICANA":
            df = base[base.League == liga]
        if liga == "SOUTH KOREA - K LEAGUE 1":
            df = base[base.League == liga]
        if liga == "SOUTH KOREA - K LEAGUE 2":
            df = base[base.League == liga]
        if liga == "SPAIN - COPA DEL REY":
            df = base[base.League == liga]
        if liga == "SPAIN - LALIGA":
            df = base[base.League == liga]
        if liga == "SPAIN - LALIGA2":   
            df = base[base.League == liga]
        if liga == "SPAIN - PRIMERA RFEF":
            df = base[base.League == liga]
        if liga == "SPAIN - SEGUNDA RFEF":
            df = base[base.League == liga]
        if liga == "SWEDEN - ALLSVENSKAN":
            df = base[base.League == liga]
        if liga == "SWEDEN - SUPERETTAN": 
            df = base[base.League == liga]
        if liga == "SWITZERLAND - CHALLENGE LEAGUE":
            df = base[base.League == liga]
        if liga == "SWITZERLAND - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "THAILAND - THAI LEAGUE 1":
            df = base[base.League == liga]
        if liga == "THAILAND - THAI LEAGUE 2":
            df = base[base.League == liga]
        if liga == "TUNISIA - LIGUE PROFESSIONNELLE 1":
            df = base[base.League == liga]
        if liga == "TURKEY - 1. LIG":    
            df = base[base.League == liga]
        if liga == "TURKEY - SUPER LIG":
            df = base[base.League == liga]
        if liga == "UGANDA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "UKRAINE - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "UNITED ARAB EMIRATES - UAE LEAGUE": 
            df = base[base.League == liga]
        if liga == "URUGUAY - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "URUGUAY - SEGUNDA DIVISION":
            df = base[base.League == liga]
        if liga == "USA - MLS":    
            df = base[base.League == liga]
        if liga == "USA - USL CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "UZBEKISTAN - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "VENEZUELA - LIGA FUTVE":
            df = base[base.League == liga]
        if liga == "VENEZUELA - LIGA FUTVE 2":
            df = base[base.League == liga]
        if liga == "VIETNAM - V.LEAGUE 1":
            df = base[base.League == liga]
        if liga == "WALES - CYMRU PREMIER":
            df = base[base.League == liga]
        
        df["FT_Goals_H"] = df["FT_Goals_H"].astype('int64')
        df["FT_Goals_A"] = df["FT_Goals_A"].astype('int64')
        df['FT_Odd_BTTS_Yes'] = pd.to_numeric(df['FT_Odd_BTTS_Yes'],errors = 'coerce')
        df['FT_Odd_BTTS_No'] = pd.to_numeric(df['FT_Odd_BTTS_No'],errors = 'coerce')

        df['BTTS_Yes_No'] = df.apply(lambda row: 1 if (row['FT_Goals_H'] > 0 and row['FT_Goals_A'] > 0) else 0, axis=1)
        
        total_count = len(df.index)
        df["Date"] = pd.to_datetime(df["Date"])
        df['Date'] = df['Date'].dt.date

        winHPLValues = 100 * df.FT_Odd_BTTS_Yes - 100
        winAPLValues = 100 * df.FT_Odd_BTTS_No - 100
        losePLValues = -100

        df.loc[(df['BTTS_Yes_No'] == 1), 'Result_FT'] = 'H'
        df.loc[(df['BTTS_Yes_No'] == 0), 'Result_FT'] = 'A'

        df['H'] = winHPLValues.where(df.Result_FT == 'H', other=losePLValues)
        df['A'] = winAPLValues.where(df.Result_FT == 'A', other=losePLValues)

        no_of_days = 0

        matchDates = df.Date.unique()

        if no_of_days > 0:
            matchDates = (matchDates[-no_of_days:])
                
        df2 = pd.DataFrame()

        rowsIndex = []
        rowsDate = []
        rowsH = []
        rowsA = []

        count = 0
        for mDate in matchDates:
            count += 1
            rowsDate.append(mDate)
            rowsH.append(df.loc[df['Date'] == mDate]['H'].sum())
            rowsA.append(df.loc[df['Date'] == mDate]['A'].sum())

        df2['Date'] = rowsDate
        df2['H'] = rowsH
        df2['A'] = rowsA

        df2 = df2.tail(101)
        df2 = df2.reset_index(drop=True)
        df2['Id'] = df2.reset_index()['index'].rename('index_copy')
        df2['Id'] = df2['Id'] + 1
        df2 = df2[['Id','Date','H','A']]

        df2['Hacu'] = df2.H.cumsum()
        df2['Aacu'] = df2.A.cumsum()

        df2['Hacu'].loc[0] = np.nan
        df2['Aacu'].loc[0] = np.nan

        def weighted_mean_H(s):
            d = df2.loc[s.index, 'Hacu']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_H_C(s):
            d = df2.loc[s.index, 'waHC']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_A(s):
            d = df2.loc[s.index, 'Aacu']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_A_C(s):
            d = df2.loc[s.index, 'waAC']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        df2['waH16'] = df2.rolling(16)['Hacu'].apply(weighted_mean_H, raw=False)
        df2['waH8'] = df2.rolling(8)['Hacu'].apply(weighted_mean_H, raw=False)
        df2['waHC'] = 2*df2.waH8-df2.waH16
        df2['waH4'] = df2.rolling(4)['waHC'].apply(weighted_mean_H_C, raw=False)

        df2['waA16'] = df2.rolling(16)['Aacu'].apply(weighted_mean_A, raw=False)
        df2['waA8'] = df2.rolling(8)['Aacu'].apply(weighted_mean_A, raw=False)
        df2['waAC'] = 2*df2.waA8-df2.waA16
        df2['waA4'] = df2.rolling(4)['waAC'].apply(weighted_mean_A_C, raw=False)

        df2['Hhull'] = df2['waH4']
        df2['Ahull'] = df2['waA4']

        df2['Hdist'] = (df2.Hacu / df2.Hhull)
        df2['Adist'] = (df2.Aacu / df2.Ahull)

        def r_function(s):
            f = s.loc[s.index.values[0]]
            l = s.loc[s.index.values[1]]
            return (l -f)/abs(f)

        df2['Hr'] = df2['Hhull'].rolling(2).apply(r_function, raw=False)
        df2['Ar'] = df2['Ahull'].rolling(2).apply(r_function, raw=False)

        def inc_H(s):
            x = df2.loc[s.index, 'Id']
            y = df2.loc[s.index, 'Hhull']
            slope, intercept = np.polyfit(x, y , 1)
            return slope

        def inc_A(s):
            x = df2.loc[s.index, 'Id']
            y = df2.loc[s.index, 'Ahull']
            slope, intercept = np.polyfit(x, y, 1)
            return slope
        
        df2['Hinc'] = df2['Hhull'].rolling(5).apply(inc_H, raw=False)
        df2['Ainc'] = df2['Ahull'].rolling(5).apply(inc_A, raw=False)

        df2['Hdp'] = df2['Hacu'].rolling(10).std()
        df2['Adp'] = df2['Aacu'].rolling(10).std()

        df2['Hamp'] = df2['Hacu'].rolling(10).max() / df2['Hacu'].rolling(10).min()
        df2['Aamp'] = df2['Aacu'].rolling(10).max() / df2['Aacu'].rolling(10).min()
        
        df3 = pd.DataFrame()

        def normaliz(dfS):
            actual_value = (dfS.loc[dfS.index.values[4]])
            try:
                n = (actual_value - dfS.min()) / (dfS.max() - dfS.min())
                if math.isnan(n):
                    return 0
            except ZeroDivisionError:
                return 0
            return n

        
        df3['Id'] = df2['Id'].iloc[23:]

        df3['Hhull'] = df2['Hhull'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Ahull'] = df2['Ahull'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hdist'] = df2['Hdist'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Adist'] = df2['Adist'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hr'] = df2['Hr'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Ar'] = df2['Ar'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hinc'] = df2['Hinc'].rolling(5).apply(normaliz, raw=False)
        df3['Ainc'] = df2['Ainc'].rolling(5).apply(normaliz, raw=False)

        df3['Hdp'] = df2['Hdp'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Adp'] = df2['Adp'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hamp'] = df2['Hamp'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Aamp'] = df2['Aamp'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['R'] = ''

        for index, row in df2.iterrows():
            if index > 26:
                try:
                    h = df2.iloc[(index+1)].H
                    a = df2.iloc[(index+1)].A
                    if h > a:
                        df3.loc[index, 'R'] = 'BTTS_Yes'
                    else:
                        df3.loc[index, 'R'] = 'BTTS_No'
                except LookupError:
                    pass

        selected_date = df3.iloc[-1]

        distance_columns = ['Hhull', 'Ahull', 'Hdist', 'Adist', 'Hr', 'Ar', 'Hinc', 'Ainc', 'Hdp', 'Adp', 'Hamp', 'Aamp']

        def euclidean_distance(row):
            """
            A simple euclidean distance function
            """
            inner_value = 0
            for k in distance_columns:
                inner_value += (row[k] - selected_date[k]) ** 2
            return math.sqrt(inner_value)

        def euclidean_distance_tr(row):
            inner_value = 0
            for k in distance_columns:
                inner_value += abs(row[k] - selected_date[k])
            return inner_value
        

        df3['eucli'] = df3.apply(euclidean_distance_tr, axis=1)
        
        
        df4 = pd.DataFrame()
        df4['R'] = df3['R']
        df4['eucli'] = df3['eucli']
        df4.sort_values(by=['eucli'], inplace=True)


        teoria_dos_retornos = {}
      
        try:
            #teoria_dos_retornos["Date"] = datetime.today().strftime('%Y-%m-%d')
            teoria_dos_retornos["League"] = liga
            teoria_dos_retornos["N1"] = df4[df4.eucli != 0]['R'].iloc[0]
        except:
            teoria_dos_retornos["N1"] = 0
        try:
            teoria_dos_retornos["N2"] = df4[df4.eucli != 0]['R'].iloc[1]
        except:
            teoria_dos_retornos["N2"] = 0
        try:
            teoria_dos_retornos["N3"] = df4[df4.eucli != 0]['R'].iloc[2]
        except:
            teoria_dos_retornos["N3"] = 0

        lista.append(teoria_dos_retornos)
lista = [ ]
TR()
df00 = pd.DataFrame(lista)
Jogos_do_Dia = jogos_do_dia.merge(df00, on=['League'])
Jogos_do_Dia.reset_index(inplace=True, drop=True)
Jogos_do_Dia.index = Jogos_do_Dia.index.set_names(['Nº'])
Jogos_do_Dia = Jogos_do_Dia.rename(index=lambda x: x + 1)

from futpythontrader import *

# Gerando os dados para excel
# data = date.today()  + timedelta(1)
hoje = data.strftime('%Y-%m-%d')
nome = 'Teoria_dos_Retornos_BTTS_ARKAD.csv'
df00.to_csv(f'./Teoria_dos_Retornos/{data}_{nome}', index = False)
df00


# In[9]:


def TR():
    for i in ligas:
        liga = i
        
        if liga == "ARMENIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ALBANIA - SUPERLIGA":
            df = base[base.League == liga]
        if liga == "ANDORRA - PRIMERA DIVISIÓ":
            df = base[base.League == liga]
        if liga == "ANGOLA - GIRABOLA":
            df = base[base.League == liga]
        if liga == "ARGENTINA - COPA DE LA LIGA PROFESIONAL":
            df = base[base.League == liga]
        if liga == "ARGENTINA - LIGA PROFESIONAL":
            df = base[base.League == liga]
        if liga == "ARGENTINA - PRIMERA NACIONAL":
            df = base[base.League == liga]
        if liga == "AUSTRALIA - A-LEAGUE":
            df = base[base.League == liga]
        if liga == "AUSTRIA - 2. LIGA":
            df = base[base.League == liga]
        if liga == "AUSTRIA - BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "AZERBAIJAN - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "BANGLADESH - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "BELARUS - VYSSHAYA LIGA":
            df = base[base.League == liga]
        if liga == "BELGIUM - CHALLENGER PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "BELGIUM - JUPILER PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "BOLIVIA - DIVISION PROFESIONAL":
            df = base[base.League == liga]
        if liga == "BOLIVIA - NACIONAL B":
            df = base[base.League == liga]
        if liga == "BOSNIA AND HERZEGOVINA - PREMIJER LIGA BIH":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO U20":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO U23":
            df = base[base.League == liga]
        if liga == "BRAZIL - BRASILEIRO WOMEN":
            df = base[base.League == liga]
        if liga == "BRAZIL - COPA DO BRASIL":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE A":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE B":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE C":
            df = base[base.League == liga]
        if liga == "BRAZIL - SERIE D":
            df = base[base.League == liga]
        if liga == "BULGARIA - PARVA LIGA":
            df = base[base.League == liga]
        if liga == "CAMEROON - ELITE ONE":
            df = base[base.League == liga]
        if liga == "CANADA - CANADIAN PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "CHILE - PRIMERA B":
            df = base[base.League == liga]
        if liga == "CHILE - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "CHINA - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "COLOMBIA - PRIMERA A":
            df = base[base.League == liga]
        if liga == "COLOMBIA - PRIMERA B":
            df = base[base.League == liga]
        if liga == "COSTA RICA - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "CROATIA - HNL":
            df = base[base.League == liga]
        if liga == "CROATIA - PRVA NL":
            df = base[base.League == liga]
        if liga == "CYPRUS - CYTA CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "CZECH REPUBLIC - FORTUNA:LIGA":
            df = base[base.League == liga]
        if liga == "DENMARK - 1ST DIVISION":
            df = base[base.League == liga]
        if liga == "DENMARK - SUPERLIGA":
            df = base[base.League == liga]
        if liga == "DOMINICAN REPUBLIC - LDF":
            df = base[base.League == liga]
        if liga == "ECUADOR - LIGA PRO":
            df = base[base.League == liga]
        if liga == "ECUADOR - SERIE B":
            df = base[base.League == liga]
        if liga == "EGYPT - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "ENGLAND - EFL CUP":
            df = base[base.League == liga]
        if liga == "ENGLAND - FA CUP":
            df = base[base.League == liga]
        if liga == "ENGLAND - LEAGUE ONE":
            df = base[base.League == liga]
        if liga == "ENGLAND - LEAGUE TWO":
            df = base[base.League == liga]
        if liga == "ENGLAND - NATIONAL LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "ENGLAND - PREMIER LEAGUE 2":
            df = base[base.League == liga]
        if liga == "ESTONIA - ESILIIGA":
            df = base[base.League == liga]
        if liga == "ESTONIA - MEISTRILIIGA":
            df = base[base.League == liga]
        if liga == "EUROPE - CHAMPIONS LEAGUE":
            df = base[base.League == liga]
        if liga == "EUROPE - EUROPA CONFERENCE LEAGUE":
            df = base[base.League == liga]
        if liga == "EUROPE - EUROPA LEAGUE":
            df = base[base.League == liga]
        if liga == "FIJI - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "FINLAND - VEIKKAUSLIIGA":
            df = base[base.League == liga]
        if liga == "FINLAND - YKKONEN":
            df = base[base.League == liga]
        if liga == "FRANCE - LIGUE 1":
            df = base[base.League == liga]
        if liga == "FRANCE - LIGUE 2":
            df = base[base.League == liga]
        if liga == "FRANCE - NATIONAL":
            df = base[base.League == liga]
        if liga == "GEORGIA - CRYSTALBET EROVNULI LIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - 2. BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - 3. LIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - BUNDESLIGA":
            df = base[base.League == liga]
        if liga == "GERMANY - DFB POKAL":
            df = base[base.League == liga]
        if liga == "GHANA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "GREECE - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "GUATEMALA - LIGA NACIONAL":
            df = base[base.League == liga]
        if liga == "HONDURAS - LIGA NACIONAL":
            df = base[base.League == liga]
        if liga == "HONG KONG - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "HUNGARY - OTP BANK LIGA":
            df = base[base.League == liga]
        if liga == "ICELAND - BESTA DEILD KARLA":
            df = base[base.League == liga]
        if liga == "INDIA - I-LEAGUE":
            df = base[base.League == liga]
        if liga == "INDIA - ISL":
            df = base[base.League == liga]
        if liga == "INDONESIA - LIGA 1":
            df = base[base.League == liga]
        if liga == "IRAN - PERSIAN GULF PRO LEAGUE":
            df = base[base.League == liga]
        if liga == "IRAQ - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "IRELAND - DIVISION 1":
            df = base[base.League == liga]
        if liga == "IRELAND - PREMIER DIVISION":
            df = base[base.League == liga]
        if liga == "ISRAEL - LIGAT HA'AL":
            df = base[base.League == liga]
        if liga == "ITALY - COPPA ITALIA":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE A":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE B":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE C":
            df = base[base.League == liga]
        if liga == "ITALY - SERIE D":
            df = base[base.League == liga]
        if liga == "IVORY COAST - LIGUE 1":
            df = base[base.League == liga]
        if liga == "JAMAICA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "JAPAN - J1 LEAGUE":
            df = base[base.League == liga]
        if liga == "JAPAN - J2 LEAGUE":
            df = base[base.League == liga]
        if liga == "LITHUANIA - A LYGA":
            df = base[base.League == liga]
        if liga == "LUXEMBOURG - NATIONAL DIVISION":
            df = base[base.League == liga]
        if liga == "MALTA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "MEXICO - LIGA DE EXPANSION MX":
            df = base[base.League == liga]
        if liga == "MEXICO - LIGA MX":
            df = base[base.League == liga]
        if liga == "MOLDOVA - SUPER LIGA":
            df = base[base.League == liga]
        if liga == "MONGOLIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "MONTENEGRO - PRVA CRNOGORSKA LIGA":
            df = base[base.League == liga]
        if liga == "MOROCCO - BOTOLA PRO":
            df = base[base.League == liga]
        if liga == "MOZAMBIQUE - MOCAMBOLA":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - DERDE DIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - EERSTE DIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - EREDIVISIE":
            df = base[base.League == liga]
        if liga == "NETHERLANDS - TWEEDE DIVISIE":
            df = base[base.League == liga]
        if liga == "NICARAGUA - LIGA PRIMERA":
            df = base[base.League == liga]
        if liga == "NIGERIA - NPFL":
            df = base[base.League == liga]
        if liga == "NORTH MACEDONIA - 1. MFL":
            df = base[base.League == liga]
        if liga == "NORTHERN IRELAND - NIFL CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "NORTHERN IRELAND - NIFL PREMIERSHIP":
            df = base[base.League == liga]
        if liga == "NORWAY - ELITESERIEN":
            df = base[base.League == liga]
        if liga == "NORWAY - OBOS-LIGAEN":
            df = base[base.League == liga]
        if liga == "PANAMA - LPF":
            df = base[base.League == liga]
        if liga == "PARAGUAY - DIVISION INTERMEDIA":
            df = base[base.League == liga]
        if liga == "PARAGUAY - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "PERU - LIGA 1":
            df = base[base.League == liga]
        if liga == "PERU - LIGA 2":
            df = base[base.League == liga]
        if liga == "PHILIPPINES - PFL":
            df = base[base.League == liga]
        if liga == "POLAND - DIVISION 1":
            df = base[base.League == liga]
        if liga == "POLAND - EKSTRAKLASA":
            df = base[base.League == liga]
        if liga == "PORTUGAL - LIGA PORTUGAL":
            df = base[base.League == liga]
        if liga == "PORTUGAL - LIGA PORTUGAL 2":
            df = base[base.League == liga]
        if liga == "PORTUGAL - TAÇA DE PORTUGAL":
            df = base[base.League == liga]
        if liga == "QATAR - QSL":    
            df = base[base.League == liga]
        if liga == "ROMANIA - LIGA 1":
            df = base[base.League == liga]
        if liga == "ROMANIA - LIGA 2":   
            df = base[base.League == liga]
        if liga == "RUSSIA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "SAN MARINO - CAMPIONATO SAMMARINESE":
            df = base[base.League == liga]
        if liga == "SAUDI ARABIA - SAUDI PROFESSIONAL LEAGUE":
            df = base[base.League == liga]
        if liga == "SCOTLAND - CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "SCOTLAND - LEAGUE ONE":
            df = base[base.League == liga]
        if liga == "SCOTLAND - LEAGUE TWO":
            df = base[base.League == liga]
        if liga == "SCOTLAND - PREMIERSHIP":
            df = base[base.League == liga]
        if liga == "SENEGAL - LIGUE 1":   
            df = base[base.League == liga]
        if liga == "SERBIA - PRVA LIGA":  
            df = base[base.League == liga]
        if liga == "SERBIA - SUPER LIGA": 
            df = base[base.League == liga]
        if liga == "SINGAPORE - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "SLOVAKIA - NIKE LIGA":
            df = base[base.League == liga]
        if liga == "SLOVENIA - PRVA LIGA":
            df = base[base.League == liga]
        if liga == "SOUTH AMERICA - COPA LIBERTADORES":
            df = base[base.League == liga]
        if liga == "SOUTH AMERICA - COPA SUDAMERICANA":
            df = base[base.League == liga]
        if liga == "SOUTH KOREA - K LEAGUE 1":
            df = base[base.League == liga]
        if liga == "SOUTH KOREA - K LEAGUE 2":
            df = base[base.League == liga]
        if liga == "SPAIN - COPA DEL REY":
            df = base[base.League == liga]
        if liga == "SPAIN - LALIGA":
            df = base[base.League == liga]
        if liga == "SPAIN - LALIGA2":   
            df = base[base.League == liga]
        if liga == "SPAIN - PRIMERA RFEF":
            df = base[base.League == liga]
        if liga == "SPAIN - SEGUNDA RFEF":
            df = base[base.League == liga]
        if liga == "SWEDEN - ALLSVENSKAN":
            df = base[base.League == liga]
        if liga == "SWEDEN - SUPERETTAN": 
            df = base[base.League == liga]
        if liga == "SWITZERLAND - CHALLENGE LEAGUE":
            df = base[base.League == liga]
        if liga == "SWITZERLAND - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "THAILAND - THAI LEAGUE 1":
            df = base[base.League == liga]
        if liga == "THAILAND - THAI LEAGUE 2":
            df = base[base.League == liga]
        if liga == "TUNISIA - LIGUE PROFESSIONNELLE 1":
            df = base[base.League == liga]
        if liga == "TURKEY - 1. LIG":    
            df = base[base.League == liga]
        if liga == "TURKEY - SUPER LIG":
            df = base[base.League == liga]
        if liga == "UGANDA - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "UKRAINE - PREMIER LEAGUE":
            df = base[base.League == liga]
        if liga == "UNITED ARAB EMIRATES - UAE LEAGUE": 
            df = base[base.League == liga]
        if liga == "URUGUAY - PRIMERA DIVISION":
            df = base[base.League == liga]
        if liga == "URUGUAY - SEGUNDA DIVISION":
            df = base[base.League == liga]
        if liga == "USA - MLS":    
            df = base[base.League == liga]
        if liga == "USA - USL CHAMPIONSHIP":
            df = base[base.League == liga]
        if liga == "UZBEKISTAN - SUPER LEAGUE":
            df = base[base.League == liga]
        if liga == "VENEZUELA - LIGA FUTVE":
            df = base[base.League == liga]
        if liga == "VENEZUELA - LIGA FUTVE 2":
            df = base[base.League == liga]
        if liga == "VIETNAM - V.LEAGUE 1":
            df = base[base.League == liga]
        if liga == "WALES - CYMRU PREMIER":
            df = base[base.League == liga]
        
        df["FT_Goals_H"] = df["FT_Goals_H"].astype('int64')
        df["FT_Goals_A"] = df["FT_Goals_A"].astype('int64')
        df['FT_Odd_Over45'] = pd.to_numeric(df['FT_Odd_Over45'],errors = 'coerce')
        df['FT_Odd_Under45'] = pd.to_numeric(df['FT_Odd_Under45'],errors = 'coerce')
        
        total_count = len(df.index)
        df["Date"] = pd.to_datetime(df["Date"])
        df['Date'] = df['Date'].dt.date

        winHPLValues = 100 * df.FT_Odd_Over45 - 100
        winAPLValues = 100 * df.FT_Odd_Over45 - 100
        losePLValues = -100

        df.loc[(((df['FT_Goals_H']) + (df['FT_Goals_A'])) > 4), 'Result_FT'] = 'H'
        df.loc[(((df['FT_Goals_H']) + (df['FT_Goals_A'])) < 5), 'Result_FT'] = 'A'

        df['H'] = winHPLValues.where(df.Result_FT == 'H', other=losePLValues)
        df['A'] = winAPLValues.where(df.Result_FT == 'A', other=losePLValues)

        no_of_days = 0

        matchDates = df.Date.unique()

        if no_of_days > 0:
            matchDates = (matchDates[-no_of_days:])
                
        df2 = pd.DataFrame()

        rowsIndex = []
        rowsDate = []
        rowsH = []
        rowsA = []

        count = 0
        for mDate in matchDates:
            count += 1
            rowsDate.append(mDate)
            rowsH.append(df.loc[df['Date'] == mDate]['H'].sum())
            rowsA.append(df.loc[df['Date'] == mDate]['A'].sum())

        df2['Date'] = rowsDate
        df2['H'] = rowsH
        df2['A'] = rowsA

        df2 = df2.tail(101)
        df2 = df2.reset_index(drop=True)
        df2['Id'] = df2.reset_index()['index'].rename('index_copy')
        df2['Id'] = df2['Id'] + 1
        df2 = df2[['Id','Date','H','A']]

        df2['Hacu'] = df2.H.cumsum()
        df2['Aacu'] = df2.A.cumsum()

        df2['Hacu'].loc[0] = np.nan
        df2['Aacu'].loc[0] = np.nan

        def weighted_mean_H(s):
            d = df2.loc[s.index, 'Hacu']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_H_C(s):
            d = df2.loc[s.index, 'waHC']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_A(s):
            d = df2.loc[s.index, 'Aacu']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        def weighted_mean_A_C(s):
            d = df2.loc[s.index, 'waAC']
            w = df2.loc[s.index, 'Id']
            return (d * w).sum() / w.sum()

        df2['waH16'] = df2.rolling(16)['Hacu'].apply(weighted_mean_H, raw=False)
        df2['waH8'] = df2.rolling(8)['Hacu'].apply(weighted_mean_H, raw=False)
        df2['waHC'] = 2*df2.waH8-df2.waH16
        df2['waH4'] = df2.rolling(4)['waHC'].apply(weighted_mean_H_C, raw=False)

        df2['waA16'] = df2.rolling(16)['Aacu'].apply(weighted_mean_A, raw=False)
        df2['waA8'] = df2.rolling(8)['Aacu'].apply(weighted_mean_A, raw=False)
        df2['waAC'] = 2*df2.waA8-df2.waA16
        df2['waA4'] = df2.rolling(4)['waAC'].apply(weighted_mean_A_C, raw=False)

        df2['Hhull'] = df2['waH4']
        df2['Ahull'] = df2['waA4']

        df2['Hdist'] = (df2.Hacu / df2.Hhull)
        df2['Adist'] = (df2.Aacu / df2.Ahull)

        def r_function(s):
            f = s.loc[s.index.values[0]]
            l = s.loc[s.index.values[1]]
            return (l -f)/abs(f)

        df2['Hr'] = df2['Hhull'].rolling(2).apply(r_function, raw=False)
        df2['Ar'] = df2['Ahull'].rolling(2).apply(r_function, raw=False)

        def inc_H(s):
            x = df2.loc[s.index, 'Id']
            y = df2.loc[s.index, 'Hhull']
            slope, intercept = np.polyfit(x, y , 1)
            return slope

        def inc_A(s):
            x = df2.loc[s.index, 'Id']
            y = df2.loc[s.index, 'Ahull']
            slope, intercept = np.polyfit(x, y, 1)
            return slope
        
        df2['Hinc'] = df2['Hhull'].rolling(5).apply(inc_H, raw=False)
        df2['Ainc'] = df2['Ahull'].rolling(5).apply(inc_A, raw=False)

        df2['Hdp'] = df2['Hacu'].rolling(10).std()
        df2['Adp'] = df2['Aacu'].rolling(10).std()

        df2['Hamp'] = df2['Hacu'].rolling(10).max() / df2['Hacu'].rolling(10).min()
        df2['Aamp'] = df2['Aacu'].rolling(10).max() / df2['Aacu'].rolling(10).min()
        
        df3 = pd.DataFrame()

        def normaliz(dfS):
            actual_value = (dfS.loc[dfS.index.values[4]])
            try:
                n = (actual_value - dfS.min()) / (dfS.max() - dfS.min())
                if math.isnan(n):
                    return 0
            except ZeroDivisionError:
                return 0
            return n

        
        df3['Id'] = df2['Id'].iloc[23:]

        df3['Hhull'] = df2['Hhull'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Ahull'] = df2['Ahull'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hdist'] = df2['Hdist'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Adist'] = df2['Adist'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hr'] = df2['Hr'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Ar'] = df2['Ar'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hinc'] = df2['Hinc'].rolling(5).apply(normaliz, raw=False)
        df3['Ainc'] = df2['Ainc'].rolling(5).apply(normaliz, raw=False)

        df3['Hdp'] = df2['Hdp'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Adp'] = df2['Adp'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['Hamp'] = df2['Hamp'].iloc[23:].rolling(5).apply(normaliz, raw=False)
        df3['Aamp'] = df2['Aamp'].iloc[23:].rolling(5).apply(normaliz, raw=False)

        df3['R'] = ''

        for index, row in df2.iterrows():
            if index > 26:
                try:
                    h = df2.iloc[(index+1)].H
                    a = df2.iloc[(index+1)].A
                    if h > a:
                        df3.loc[index, 'R'] = 'Over45'
                    else:
                        df3.loc[index, 'R'] = 'Under45'
                except LookupError:
                    pass

        selected_date = df3.iloc[-1]

        distance_columns = ['Hhull', 'Ahull', 'Hdist', 'Adist', 'Hr', 'Ar', 'Hinc', 'Ainc', 'Hdp', 'Adp', 'Hamp', 'Aamp']

        def euclidean_distance(row):
            """
            A simple euclidean distance function
            """
            inner_value = 0
            for k in distance_columns:
                inner_value += (row[k] - selected_date[k]) ** 2
            return math.sqrt(inner_value)

        def euclidean_distance_tr(row):
            inner_value = 0
            for k in distance_columns:
                inner_value += abs(row[k] - selected_date[k])
            return inner_value
        

        df3['eucli'] = df3.apply(euclidean_distance_tr, axis=1)
        
        
        df4 = pd.DataFrame()
        df4['R'] = df3['R']
        df4['eucli'] = df3['eucli']
        df4.sort_values(by=['eucli'], inplace=True)


        teoria_dos_retornos = {}
      
        try:
            #teoria_dos_retornos["Date"] = datetime.today().strftime('%Y-%m-%d')
            teoria_dos_retornos["League"] = liga
            teoria_dos_retornos["N1"] = df4[df4.eucli != 0]['R'].iloc[0]
        except:
            teoria_dos_retornos["N1"] = 0
        try:
            teoria_dos_retornos["N2"] = df4[df4.eucli != 0]['R'].iloc[1]
        except:
            teoria_dos_retornos["N2"] = 0
        try:
            teoria_dos_retornos["N3"] = df4[df4.eucli != 0]['R'].iloc[2]
        except:
            teoria_dos_retornos["N3"] = 0

        lista.append(teoria_dos_retornos)

lista = [ ]
TR()
df00 = pd.DataFrame(lista)
Jogos_do_Dia = jogos_do_dia.merge(df00, on=['League'])
Jogos_do_Dia.reset_index(inplace=True, drop=True)
Jogos_do_Dia.index = Jogos_do_Dia.index.set_names(['Nº'])
Jogos_do_Dia = Jogos_do_Dia.rename(index=lambda x: x + 1)

from futpythontrader import *
# Gerando os dados para excel
data = date.today()  + timedelta(1)
hoje = data.strftime('%Y-%m-%d')
nome = 'Teoria_dos_Retornos_Over_Under_45_ARKAD.csv'
df00.to_csv(f'./Teoria_dos_Retornos/{data}_{nome}', index = False)
df00


# In[ ]:




