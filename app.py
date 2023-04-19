import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta
from io import BytesIO
import xlsxwriter

st.set_page_config(
    page_title='Teoria do Retornos - Grupo Arkad',
)

def pagina_01():
    st.subheader("Jogos do Dia")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./Teoria_dos_Retornos/{dia}_Jogos_do_Dia.csv")
        
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
        data_jogos = pd.read_csv(f"./Teoria_dos_Retornos/{dia}_Teoria_dos_Retornos_Match_Odds.csv")
        
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
        file_name=f'Teoria_dos_Retornos_Match_Odds_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    


def pagina_03():
    st.subheader("Teoria dos Retornos - Over/Under 0.5 FT")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./Teoria_dos_Retornos/{dia}_Teoria_dos_Retornos_Over_Under_05.csv")
        
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
        file_name=f'Teoria_dos_Retornos_Over_Under_05_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    


def pagina_04():
    st.subheader("Teoria dos Retornos - Over/Under 1.5 FT")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./Teoria_dos_Retornos/{dia}_Teoria_dos_Retornos_Over_Under_15.csv")
        
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
        file_name=f'Teoria_dos_Retornos_Over_Under_15_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    

def pagina_05():
    st.subheader("Teoria dos Retornos - Over/Under 2.5 FT")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./Teoria_dos_Retornos/{dia}_Teoria_dos_Retornos_Over_Under_25.csv")
        
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
        file_name=f'Teoria_dos_Retornos_Over_Under_25_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    

    
def pagina_06():
    st.subheader("Teoria dos Retornos - Over/Under 3.5 FT")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./Teoria_dos_Retornos/{dia}_Teoria_dos_Retornos_Over_Under_35.csv")
        
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
        file_name=f'Teoria_dos_Retornos_Over_Under_35_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    



    
def pagina_07():
    st.subheader("Teoria dos Retornos - Over/Under 4.5 FT")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./Teoria_dos_Retornos/{dia}_Teoria_dos_Retornos_Over_Under_45.csv")
        
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
        file_name=f'Teoria_dos_Retornos_Over_Under_45_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    


    

def pagina_08():
    st.subheader("Teoria dos Retornos - Ambas Marcam")

    dia = st.date_input(
        "Data de Análise",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():
        data_jogos = pd.read_csv(f"./Teoria_dos_Retornos/{dia}_Teoria_dos_Retornos_BTTS.csv")
        
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
        file_name=f'Teoria_dos_Retornos_BTTS_{dia}.xlsx',
        mime='application/vnd.ms-excel')














paginas = ['Jogos do Dia', 
           'TR - Match Odds', 
           'TR - Over/Under 0.5FT', 
           'TR - Over/Under 1.5FT',
           'TR - Over/Under 2.5FT',
           'TR - Over/Under 3.5FT',
           'TR - Over/Under 4.5FT',
           'TR - BTTS']
escolha = st.sidebar.radio('',paginas)

if escolha == 'Jogos do Dia':
    pagina_01()
if escolha == 'TR - Match Odds':
    pagina_02()
if escolha == 'TR - Over/Under 0.5FT':
    pagina_03()
if escolha == 'TR - Over/Under 1.5FT':
    pagina_04()
if escolha == 'TR - Over/Under 2.5FT':
    pagina_05()
if escolha == 'TR - Over/Under 3.5FT':
    pagina_06()
if escolha == 'TR - Over/Under 4.5FT':
    pagina_07()
if escolha == 'TR - BTTS':
    pagina_08()