#!/usr/bin/env python
# coding: utf-8

# In[1]:


from futpythontrader import *
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)


# In[2]:


key = 'a535168594f7c33f403cbd0c07c3b61d37105c253cd887672147bee92709a3b3'
url = "https://api.football-data-api.com/league-list?key="+key+"&chosen_leagues_only=true"

data1 = requests.get(url)
resp = data1.json()['data']
dados = pd.DataFrame.from_dict(resp)
dados = dados.sort_values(['name'])
dados = drop_reset_index(dados)
ligas = dados['name'].to_list()


# In[3]:


def TR_OverUnder25():
    for i in ligas:
        liga = i
        
        if liga == "Argentina Prim B Nacional":
            df1 = pd.read_csv("./Bases_de_Dados/Argentina Prim B Nacional_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Argentina Prim B Nacional_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Argentina Primera División":
            df1 = pd.read_csv("./Bases_de_Dados/Argentina Primera División_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Argentina Primera División_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Australia A-League":
            df1 = pd.read_csv("./Bases_de_Dados/Australia A-League_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Australia A-League_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Austria Bundesliga":
            df1 = pd.read_csv("./Bases_de_Dados/Austria Bundesliga_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Austria Bundesliga_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Belgium Pro League":
            df1 = pd.read_csv("./Bases_de_Dados/Belgium Pro League_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Belgium Pro League_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Bolivia LFPB":
            df1 = pd.read_csv("./Bases_de_Dados/Bolivia LFPB_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Bolivia LFPB_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Brazil Serie A":
            df1 = pd.read_csv("./Bases_de_Dados/Brazil Serie A_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Brazil Serie A_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Brazil Serie B":
            df1 = pd.read_csv("./Bases_de_Dados/Brazil Serie B_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Brazil Serie B_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Brazil Serie C":
            df1 = pd.read_csv("./Bases_de_Dados/Brazil Serie C_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Brazil Serie C_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Brazil Serie D":
            df1 = pd.read_csv("./Bases_de_Dados/Brazil Serie D_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Brazil Serie D_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Bulgaria First League":
            df1 = pd.read_csv("./Bases_de_Dados/Bulgaria First League_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Bulgaria First League_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Canada Canadian Premier League":
            df1 = pd.read_csv("./Bases_de_Dados/Canada Canadian Premier League_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Canada Canadian Premier League_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Chile Primera B":
            df1 = pd.read_csv("./Bases_de_Dados/Chile Primera B_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Chile Primera B_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Chile Primera División":
            df1 = pd.read_csv("./Bases_de_Dados/Chile Primera División_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Chile Primera División_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Chile Segunda División":
            df1 = pd.read_csv("./Bases_de_Dados/Chile Segunda División_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Chile Segunda División_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "China Chinese Super League":
            df1 = pd.read_csv("./Bases_de_Dados/China Chinese Super League_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Colombia Categoria Primera A_2022.csv")
            df = pd.concat([df1,df2])
        if liga == "Colombia Categoria Primera A":
            df1 = pd.read_csv("./Bases_de_Dados/Colombia Categoria Primera A_2023.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Colombia Categoria Primera B_2022.csv")
            df = pd.concat([df1,df2])
        if liga == "Colombia Categoria Primera B":
            df1 = pd.read_csv("./Bases_de_Dados/Colombia Categoria Primera B_2023.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Colombia Categoria Primera B_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Croatia Prva HNL":
            df1 = pd.read_csv("./Bases_de_Dados/Croatia Prva HNL_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Croatia Prva HNL_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Czech Republic First League":
            df1 = pd.read_csv("./Bases_de_Dados/Czech Republic First League_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Czech Republic First League_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Denmark 1st Division":
            df1 = pd.read_csv("./Bases_de_Dados/Denmark 1st Division_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Denmark 1st Division_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Denmark Superliga":
            df1 = pd.read_csv("./Bases_de_Dados/Denmark Superliga_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Denmark Superliga_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Ecuador Primera Categoría Serie A":
            df1 = pd.read_csv("./Bases_de_Dados/Ecuador Primera Categoría Serie A_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Ecuador Primera Categoría Serie A_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Egypt Egyptian Premier League":
            df1 = pd.read_csv("./Bases_de_Dados/Egypt Egyptian Premier League_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Egypt Egyptian Premier League_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "England Championship":
            df1 = pd.read_csv("./Bases_de_Dados/England Championship_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/England Championship_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "England EFL League One":
            df1 = pd.read_csv("./Bases_de_Dados/England EFL League One_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/England EFL League One_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "England EFL League Two":
            df1 = pd.read_csv("./Bases_de_Dados/England EFL League Two_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/England EFL League Two_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "England National League":
            df1 = pd.read_csv("./Bases_de_Dados/England National League_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/England National League_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "England Premier League":
            df1 = pd.read_csv("./Bases_de_Dados/England Premier League_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/England Premier League_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Finland Veikkausliiga":
            df1 = pd.read_csv("./Bases_de_Dados/Finland Veikkausliiga_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Finland Veikkausliiga_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "France Ligue 1":
            df1 = pd.read_csv("./Bases_de_Dados/France Ligue 1_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/France Ligue 1_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "France Ligue 2":
            df1 = pd.read_csv("./Bases_de_Dados/France Ligue 2_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/France Ligue 2_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Germany 2. Bundesliga":
            df1 = pd.read_csv("./Bases_de_Dados/Germany 2. Bundesliga_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Germany 2. Bundesliga_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Germany Bundesliga":
            df1 = pd.read_csv("./Bases_de_Dados/Germany Bundesliga_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Germany Bundesliga_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Greece Super League":
            df1 = pd.read_csv("./Bases_de_Dados/Greece Super League_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Greece Super League_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Hungary NB I":
            df1 = pd.read_csv("./Bases_de_Dados/Hungary NB I_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Hungary NB I_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Italy Serie A":
            df1 = pd.read_csv("./Bases_de_Dados/Italy Serie A_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Italy Serie A_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Italy Serie B":
            df1 = pd.read_csv("./Bases_de_Dados/Italy Serie B_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Italy Serie B_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Japan J1 League":
            df1 = pd.read_csv("./Bases_de_Dados/Japan J1 League_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Japan J1 League_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Japan J2 League":
            df1 = pd.read_csv("./Bases_de_Dados/Japan J2 League_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Japan J2 League_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Mexico Ascenso MX":
            df1 = pd.read_csv("./Bases_de_Dados/Mexico Ascenso MX_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Mexico Ascenso MX_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Mexico Liga MX":
            df1 = pd.read_csv("./Bases_de_Dados/Mexico Liga MX_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Mexico Liga MX_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Netherlands Eerste Divisie":
            df1 = pd.read_csv("./Bases_de_Dados/Netherlands Eerste Divisie_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Netherlands Eerste Divisie_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Netherlands Eredivisie":
            df1 = pd.read_csv("./Bases_de_Dados/Netherlands Eredivisie_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Netherlands Eredivisie_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Netherlands Tweede Divisie":
            df1 = pd.read_csv("./Bases_de_Dados/Netherlands Tweede Divisie_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Netherlands Tweede Divisie_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Norway Eliteserien":
            df1 = pd.read_csv("./Bases_de_Dados/Norway Eliteserien_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Norway Eliteserien_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Paraguay Division Profesional":
            df1 = pd.read_csv("./Bases_de_Dados/Paraguay Division Profesional_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Paraguay Division Profesional_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Peru Primera División":
            df1 = pd.read_csv("./Bases_de_Dados/Peru Primera División_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Peru Primera División_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Poland Ekstraklasa":
            df1 = pd.read_csv("./Bases_de_Dados/Poland Ekstraklasa_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Poland Ekstraklasa_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Portugal Liga NOS":
            df1 = pd.read_csv("./Bases_de_Dados/Portugal Liga NOS_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Portugal Liga NOS_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Portugal LigaPro":
            df1 = pd.read_csv("./Bases_de_Dados/Portugal LigaPro_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Portugal LigaPro_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Republic of Ireland Premier Division":
            df1 = pd.read_csv("./Bases_de_Dados/Republic of Ireland Premier Division_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Republic of Ireland Premier Division_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Romania Liga I":
            df1 = pd.read_csv("./Bases_de_Dados/Romania Liga I_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Romania Liga I_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Scotland Premiership":
            df1 = pd.read_csv("./Bases_de_Dados/Scotland Premiership_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Scotland Premiership_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Serbia SuperLiga":
            df1 = pd.read_csv("./Bases_de_Dados/Serbia SuperLiga_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Serbia SuperLiga_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Slovakia Super Liga":
            df1 = pd.read_csv("./Bases_de_Dados/Slovakia Super Liga_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Slovakia Super Liga_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Slovenia PrvaLiga":
            df1 = pd.read_csv("./Bases_de_Dados/Slovenia PrvaLiga_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Slovenia PrvaLiga_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "South Korea K League 1":
            df1 = pd.read_csv("./Bases_de_Dados/South Korea K League 1_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/South Korea K League 1_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "South Korea K League 2":
            df1 = pd.read_csv("./Bases_de_Dados/South Korea K League 2_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/South Korea K League 2_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Spain La Liga":
            df1 = pd.read_csv("./Bases_de_Dados/Spain La Liga_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Spain La Liga_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Spain Segunda División":
            df1 = pd.read_csv("./Bases_de_Dados/Spain Segunda División_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Spain Segunda División_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Sweden Allsvenskan":
            df1 = pd.read_csv("./Bases_de_Dados/Sweden Allsvenskan_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Sweden Allsvenskan_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Switzerland Super League":
            df1 = pd.read_csv("./Bases_de_Dados/Switzerland Super League_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Switzerland Super League_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Tunisia Ligue 1":
            df1 = pd.read_csv("./Bases_de_Dados/Tunisia Ligue 1_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Tunisia Ligue 1_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Turkey Süper Lig":
            df1 = pd.read_csv("./Bases_de_Dados/Turkey Süper Lig_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Turkey Süper Lig_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "USA MLS":
            df1 = pd.read_csv("./Bases_de_Dados/USA MLS_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/USA MLS_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "USA USL Championship":
            df1 = pd.read_csv("./Bases_de_Dados/USA USL Championship_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/USA USL Championship_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Ukraine Ukrainian Premier League":
            df1 = pd.read_csv("./Bases_de_Dados/Ukraine Ukrainian Premier League_20212022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Ukraine Ukrainian Premier League_20222023.csv")
            df = pd.concat([df1,df2])
        if liga == "Uruguay Primera División":
            df1 = pd.read_csv("./Bases_de_Dados/Uruguay Primera División_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Uruguay Primera División_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Uruguay Segunda División":
            df1 = pd.read_csv("./Bases_de_Dados/Uruguay Segunda División_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Uruguay Segunda División_2023.csv")
            df = pd.concat([df1,df2])
        if liga == "Venezuela Primera División":
            df1 = pd.read_csv("./Bases_de_Dados/Venezuela Primera División_2022.csv")
            df2 = pd.read_csv("./Bases_de_Dados/Venezuela Primera División_2023.csv")
            df = pd.concat([df1,df2])

        df['TotalGoals'] = df['FT_Goals_H'] + df['FT_Goals_A']

        df = drop_reset_index(df)

        total_count = len(df.index)
        df["Date"] = pd.to_datetime(df["Date"])
        df['Date'] = df['Date'].dt.date

        winHPLValues = 100 * df.FT_Odd_Over25 - 100
        winAPLValues = 100 * df.FT_Odd_Under25 - 100
        losePLValues = -100
        
        df.loc[((df['TotalGoals']) > 2), 'Over_Under'] = 'Over'
        df.loc[((df['TotalGoals']) < 3), 'Over_Under'] = 'Under'

        df['H'] = winHPLValues.where(df.Over_Under == 'Over', other=losePLValues)
        df['A'] = winAPLValues.where(df.Over_Under == 'Under', other=losePLValues)

        no_of_days = 0

        matchDates = df.Date.unique()

        if no_of_days > 0:
            matchDates = (matchDates[-no_of_days:])
                
        df2 = pd.DataFrame()

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

        distance_columns = ['Hhull','Ahull','Hdist','Adist','Hr','Ar','Hinc','Ainc','Hdp','Adp','Hamp','Aamp']
        
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
      
        teoria_dos_retornos["League"] = liga
        teoria_dos_retornos["N1"] = df4[df4.eucli != 0]['R'].iloc[0]
        teoria_dos_retornos["N2"] = df4[df4.eucli != 0]['R'].iloc[1]
        teoria_dos_retornos["N3"] = df4[df4.eucli != 0]['R'].iloc[2]
        lista.append(teoria_dos_retornos)
        print(liga)


# In[4]:


lista = [ ]
TR_OverUnder25()
df00 = pd.DataFrame(lista)


# In[5]:


# Gerando os dados para excel
data = hoje()
hoje = data.strftime('%Y-%m-%d')
nome = 'Teoria_dos_Retornos_Over_Under_25.csv'
df00.to_csv(f'./Teoria_dos_Retornos/{hoje}_{nome}', index = False)
df00

