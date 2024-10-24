import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta
from io import BytesIO
import xlsxwriter

st.set_page_config(
    page_title='Teoria do Retornos - Grupo Arkad - FLASHSCORE',
)  

def pagina_01():
    st.subheader("Teoria dos Retornos - Match Odds")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./Teoria_dos_Retornos/{dia}_Teoria_dos_Retornos_Match_Odds_arkad.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'Teoria_dos_Retornos_Match_Odds_arkad_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    


def pagina_02():
    st.subheader("Teoria dos Retornos - Over/Under 2.5 FT")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./Teoria_dos_Retornos/{dia}_Teoria_dos_Retornos_Over_Under_25_ARKAD.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'Teoria_dos_Retornos_Over_Under_25_ARKAD_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    
def pagina_03():
    st.subheader("Teoria dos Retornos - Over/Under 0.5 FT")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./Teoria_dos_Retornos/{dia}_Teoria_dos_Retornos_Over_Under_05ft_ARKAD.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'Teoria_dos_Retornos_Over_Under_05ft_ARKAD_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    
def pagina_04():
    st.subheader("Teoria dos Retornos - Over/Under 4.5 FT")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./Teoria_dos_Retornos/{dia}_Teoria_dos_Retornos_Over_Under_45_ARKAD.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'Teoria_dos_Retornos_Over_Under_45ft_ARKAD_{dia}.xlsx',
        mime='application/vnd.ms-excel')    

def pagina_05():
    st.subheader("Teoria dos Retornos - Ambas Marcam")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./Teoria_dos_Retornos/{dia}_Teoria_dos_Retornos_BTTS_ARKAD.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'Teoria_dos_Retornos_BTTS_ARKAD_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    

def pagina_06():
    st.subheader("LAY AWAY NEW")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_lay_away_new.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'Lay_Away_New_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    

    
def pagina_07():
    st.subheader("Lay Goleada")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_lay_goleada.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'lay_goleada_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    
def pagina_08():
    st.subheader("BTTS_YES")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_btts_yes.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'btts_yes_{dia}.xlsx',
        mime='application/vnd.ms-excel')


def pagina_09():
    st.subheader("LAY 0 X 1")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_Lay_0x1.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'lay0x1_{dia}.xlsx',
        mime='application/vnd.ms-excel')

def pagina_10():
    st.subheader("OVER2_5")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_over2_5.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'OVER2_5_{dia}.xlsx',
        mime='application/vnd.ms-excel')

def pagina_11():
    st.subheader("Lay_1x0")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_Lay_1x0.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'Lay_1x0_{dia}.xlsx',
        mime='application/vnd.ms-excel')    

def pagina_12():
    st.subheader("lay_home_new")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_lay_home_new.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'lay_home_new_{dia}.xlsx',
        mime='application/vnd.ms-excel')       

def pagina_13():
    st.subheader("over05ht")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_over05ht.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'over05ht_{dia}.xlsx',
        mime='application/vnd.ms-excel') 
    
    
def pagina_14():
    st.subheader("LAY_AWAY_NEW_retorno")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_LAY_AWAY_NEW_retorno.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data
 # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'LAY_AWAY_NEW_retorno_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    
    
def pagina_15():
    st.subheader("AI_LAY_AWAY_retorno")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_AI_LAY_AWAY_retorno.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data    
    
    
    
    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'AI_LAY_AWAY_retorno_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    
def pagina_16():
    st.subheader("AI_LAY_AWAY")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_AI_LAY_AWAY.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data    
    
    
    
    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'AI_LAY_AWAY_{dia}.xlsx',
        mime='application/vnd.ms-excel')


def pagina_17():
    st.subheader("AI_LAY_AWAY_ODDS_BETFAIR")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/Entradas_Betfair_Back_Lay_AWAY_{dia}.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data    
    
    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'AI_LAY_AWAY_ODDS_BETFAIR_{dia}.xlsx',
        mime='application/vnd.ms-excel') 
    
    
def pagina_18():
    st.subheader("AI_LAY_HOME_ODDS_BETFAIR")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/Entradas_Betfair_Back_Lay_Home_{dia}.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data    
    
    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'AI_LAY_HOME_ODDS_BETFAIR_{dia}.xlsx',
        mime='application/vnd.ms-excel')    

# def pagina_19():
#     st.subheader("Lay_0x2_EVENTOS_RAROS")

#     dia = st.date_input(
#         "Data de Análise",
#         date.today())

#     ########## Importando os Jogos do Dia ##########

#     @st.cache
#     def load_data_jogos():
#         data_jogos = pd.read_csv(f"./JOGOS/{dia}_Lay_0x2_EVENTOS_RAROS.csv")
        
#         return data_jogos

#     df_jogos = load_data_jogos()

#     df_jogos.dropna(inplace=True)
#     df_jogos = df_jogos.reset_index(drop=True)
#     df_jogos.index += 1

#     st.table(df_jogos)

#     # Define a função que retorna a planilha em formato XLSX
#     def download_excel():
#         output = BytesIO()
#         writer = pd.ExcelWriter(output, engine='xlsxwriter')
#         df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
#         writer.save()
#         processed_data = output.getvalue()
#         return processed_data    
    
#     # Cria o botão de download
#     button = st.download_button(
#         label='Download',
#         data=download_excel(),
#         file_name=f'Lay_0x2_EVENTOS_RAROS_{dia}.xlsx',
#         mime='application/vnd.ms-excel')    

# def pagina_20():
#     st.subheader("Lay_2x0_EVENTOS_RAROS")

#     dia = st.date_input(
#         "Data de Análise",
#         date.today())

#     ########## Importando os Jogos do Dia ##########

#     @st.cache
#     def load_data_jogos():
#         data_jogos = pd.read_csv(f"./JOGOS/{dia}_Lay_2x0_EVENTOS_RAROS.csv")
        
#         return data_jogos

#     df_jogos = load_data_jogos()

#     df_jogos.dropna(inplace=True)
#     df_jogos = df_jogos.reset_index(drop=True)
#     df_jogos.index += 1

#     st.table(df_jogos)

#     # Define a função que retorna a planilha em formato XLSX
#     def download_excel():
#         output = BytesIO()
#         writer = pd.ExcelWriter(output, engine='xlsxwriter')
#         df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
#         writer.save()
#         processed_data = output.getvalue()
#         return processed_data    
    
#     # Cria o botão de download
#     button = st.download_button(
#         label='Download',
#         data=download_excel(),
#         file_name=f'Lay_2x0_EVENTOS_RAROS_{dia}.xlsx',
#         mime='application/vnd.ms-excel')    

# def pagina_21():
#     st.subheader("Lay_2x2_EVENTOS_RAROS")

#     dia = st.date_input(
#         "Data de Análise",
#         date.today())

#     ########## Importando os Jogos do Dia ##########

#     @st.cache
#     def load_data_jogos():
#         data_jogos = pd.read_csv(f"./JOGOS/{dia}_Lay_2x2_EVENTOS_RAROS.csv")
        
#         return data_jogos

#     df_jogos = load_data_jogos()

#     df_jogos.dropna(inplace=True)
#     df_jogos = df_jogos.reset_index(drop=True)
#     df_jogos.index += 1

#     st.table(df_jogos)

#     # Define a função que retorna a planilha em formato XLSX
#     def download_excel():
#         output = BytesIO()
#         writer = pd.ExcelWriter(output, engine='xlsxwriter')
#         df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
#         writer.save()
#         processed_data = output.getvalue()
#         return processed_data    
    
#     # Cria o botão de download
#     button = st.download_button(
#         label='Download',
#         data=download_excel(),
#         file_name=f'Lay_2x2_EVENTOS_RAROS_{dia}.xlsx',
#         mime='application/vnd.ms-excel')    

# def pagina_22():
#     st.subheader("Lay_1x3_EVENTOS_RAROS")

#     dia = st.date_input(
#         "Data de Análise",
#         date.today())

#     ########## Importando os Jogos do Dia ##########

#     @st.cache(allow_output_mutation=False)
#     def load_data_jogos():
#         data_jogos = pd.read_csv(f"./JOGOS/{dia}_Lay_1x3_EVENTOS_RAROS.csv")
        
#         return data_jogos

#     df_jogos = load_data_jogos()

#     df_jogos.dropna(inplace=True)
#     df_jogos = df_jogos.reset_index(drop=True)
#     df_jogos.index += 1

#     st.table(df_jogos)

#     # Define a função que retorna a planilha em formato XLSX
#     def download_excel():
#         output = BytesIO()
#         writer = pd.ExcelWriter(output, engine='xlsxwriter')
#         df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
#         writer.save()
#         processed_data = output.getvalue()
#         return processed_data    
    
#     # Cria o botão de download
#     button = st.download_button(
#         label='Download',
#         data=download_excel(),
#         file_name=f'Lay_1x3_EVENTOS_RAROS_{dia}.xlsx',
#         mime='application/vnd.ms-excel')    

# def pagina_23():
#     st.subheader("Lay_3x1_EVENTOS_RAROS")

#     dia = st.date_input(
#         "Data de Análise",
#         date.today())

#     ########## Importando os Jogos do Dia ##########

#     @st.cache
#     def load_data_jogos():
#         data_jogos = pd.read_csv(f"./JOGOS/{dia}_Lay_3x1_EVENTOS_RAROS.csv")
        
#         return data_jogos

#     df_jogos = load_data_jogos()

#     df_jogos.dropna(inplace=True)
#     df_jogos = df_jogos.reset_index(drop=True)
#     df_jogos.index += 1

#     st.table(df_jogos)

#     # Define a função que retorna a planilha em formato XLSX
#     def download_excel():
#         output = BytesIO()
#         writer = pd.ExcelWriter(output, engine='xlsxwriter')
#         df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
#         writer.save()
#         processed_data = output.getvalue()
#         return processed_data    
    
#     # Cria o botão de download
#     button = st.download_button(
#         label='Download',
#         data=download_excel(),
#         file_name=f'Lay_3x1_EVENTOS_RAROS_{dia}.xlsx',
#         mime='application/vnd.ms-excel')     


    
def pagina_19():
    st.subheader("LAY_0X1_RETORNOS")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_LAY_0X1_RETORNOS.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data    
    
    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'LAY_0X1_RETORNOS_{dia}.xlsx',
        mime='application/vnd.ms-excel')    
    

def pagina_20():
    st.subheader("LAY_1X0_RETORNOS")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_LAY_1X0_RETORNOS.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data    
    
    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'LAY_1X0_RETORNOS_{dia}.xlsx',
        mime='application/vnd.ms-excel')     
    
def pagina_21():
    st.subheader("lAI_LAY_AWAY_MODELOGERADO")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./JOGOS/{dia}_AI_LAY_AWAY_MODELOGERADO.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.table(df_jogos)

    # Define a função que retorna a planilha em formato XLSX
    def download_excel():
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data    
    
    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'AI_LAY_AWAY_MODELOGERADO_{dia}.xlsx',
        mime='application/vnd.ms-excel')  

    
paginas = ['TR - Match Odds', 
           'TR - Over/Under 2.5FT',
           'TR - Over/Under 0.5FT',
           'TR - Over/Under 4.5FT',
           'TR - BTTS',
           'LAY AWAY NEW',
           'LAY GOLEADA',
           'BTTS_YES',
           'LAY 0 X 1',
           'OVER2_5',
           'Lay_1x0',
           'lay_home_new',
           'over05ht',
           'LAY_AWAY_NEW_retorno',
           'AI_LAY_AWAY_retorno',
           'AI_LAY_AWAY',
           'AI_LAY_AWAY_ODDS_BETFAIR',
           'AI_LAY_HOME_ODDS_BETFAIR',
           'LAY_0X1_RETORNOS',
           'LAY_1X0_RETORNOS',
           'AI_LAY_AWAY_MODELOGERADO']

escolha = st.sidebar.radio('',paginas)

if escolha == 'TR - Match Odds':
    pagina_01()
if escolha == 'TR - Over/Under 2.5FT':
    pagina_02()
if escolha == 'TR - Over/Under 0.5FT':
    pagina_03()    
if escolha == 'TR - Over/Under 4.5FT':
    pagina_04()          
if escolha == 'TR - BTTS':
    pagina_05()
if escolha == 'LAY AWAY NEW':
    pagina_06()
if escolha == 'LAY GOLEADA':
    pagina_07()
if escolha == 'BTTS_YES':
    pagina_08()
if escolha == 'LAY 0 X 1':
    pagina_09()
if escolha == 'OVER2_5':
    pagina_10()
if escolha == 'Lay_1x0':
    pagina_11()
if escolha == 'lay_home_new':
    pagina_12()
if escolha == 'over05ht':
    pagina_13()
if escolha == 'LAY_AWAY_NEW_retorno':
    pagina_14()
if escolha == 'AI_LAY_AWAY_retorno':
    pagina_15()
if escolha == 'AI_LAY_AWAY':
    pagina_16()    
if escolha == 'AI_LAY_AWAY_ODDS_BETFAIR':
    pagina_17()     
if escolha == 'AI_LAY_HOME_ODDS_BETFAIR':
    pagina_18()
if escolha == 'LAY_0X1_RETORNOS':
    pagina_19()    
if escolha == 'LAY_1X0_RETORNOS':
    pagina_20()
if escolha == 'AI_LAY_AWAY_MODELOGERADO':
    pagina_21()   