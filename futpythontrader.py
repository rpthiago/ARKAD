import pandas as pd
import numpy as np
import math
import os
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
import requests
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def ontem():
    from datetime import date, datetime, timedelta
    dia = date.today() - timedelta(1)
    return dia

def hoje():
    from datetime import date, datetime, timedelta
    dia = date.today() + timedelta(0)
    return dia

def amanha():
    from datetime import date, datetime, timedelta
    dia = date.today() + timedelta(1)
    return dia

def reset_index(df):
    df = df.reset_index(drop=True)
    df.index += 1
    return df

def drop_reset_index(df):
    df = df.dropna()
    df = df.reset_index(drop=True)
    df.index += 1
    return df
    
def grafico(df, nome):
    df = df.reset_index(drop=True)
    df.index += 1
    df['Profit_acu'] = df.Profit.cumsum()
    profit = round(df.Profit_acu.tail(1).item(),2)
    ROI = round((df.Profit_acu.tail(1)/len(df)*100).item(),2)
    df.Profit_acu.plot(title=nome, xlabel='Entradas', ylabel='Stakes')
    print("Profit:",profit,"stakes em", len(df),"jogos")
    print("ROI:",ROI,"%")
