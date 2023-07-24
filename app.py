import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta
from io import BytesIO
import xlsxwriter

st.set_page_config(
    page_title='Teoria do Retornos - Grupo Arkad - FLASHSCORE',
)

def pagina_01():
    st.subheader("Jogos do Dia")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./Jogos_do_Dia/{dia}_Jogos_do_Dia.csv")
        
        return data_jogos

    df_jogos = load_data_jogos()

    df_jogos.dropna(inplace=True)
    df_jogos = df_jogos.reset_index(drop=True)
    df_jogos.index += 1

    st.dataframe(df_jogos)

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
        file_name=f'Jogos_do_Dia_{dia}.xlsx',
        mime='application/vnd.ms-excel')   

def pagina_02():
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
    


def pagina_03():
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
    


def pagina_04():
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
    

def pagina_05():
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
    

    
def pagina_06():
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
    
def pagina_07():
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


def pagina_08():
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

def pagina_09():
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

paginas = ['Jogos do Dia',
           'TR - Match Odds', 
           'TR - Over/Under 2.5FT', 
           'TR - BTTS',
           'LAY AWAY NEW',
           'LAY GOLEADA',
           'BTTS_YES',
           'LAY 0 X 1',
           'OVER2_5']

escolha = st.sidebar.radio('',paginas)

if escolha == 'Jogos do Dia':
    pagina_01()
if escolha == 'TR - Match Odds':
    pagina_02()
if escolha == 'TR - Over/Under 2.5FT':
    pagina_03()
if escolha == 'TR - BTTS':
    pagina_04()
if escolha == 'LAY AWAY NEW':
    pagina_05()
if escolha == 'LAY GOLEADA':
    pagina_06()
if escolha == 'BTTS_YES':
    pagina_07()
if escolha == 'LAY 0X1':
    pagina_08()
if escolha == 'OVER2_5':
    pagina_09()
