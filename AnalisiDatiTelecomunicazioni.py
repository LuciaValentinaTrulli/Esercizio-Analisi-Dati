""" Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset 
di clienti della compagnia di telecomunicazioni. L'esercizio mira a costruire un modello predittivo di 
base per la churn rate e scoprire correlazioni tra vari attributi del cliente e la loro fedeltà.

Dataset: 

ID_Cliente: Identificativo unico per ogni cliente
Età: Età del cliente
Durata_Abonnamento: Quanti mesi il cliente è stato abbonato
Tariffa_Mensile: Quanto il cliente paga al mese
Dati_Consumati: GB di dati consumati al mese
Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
Churn: Se il cliente ha lasciato la compagnia (Sì/No)

1)Caricamento e Esplorazione Iniziale:
Caricare i dati da un file CSV.
Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare 
colonne con valori mancanti. 
"""
import pandas as pd


def carica_dati(file_path):
    df = pd.read_csv(file_path)
    return df

def info(df):
    print("\nInfo sul dataset:")
    print(df.info())

def descrizione(df):
    print("\nDescrizione:")
    print(df.describe())


def distribuzione(df):
    print"\nDistribuzione dei valori 
    print(df[''].value_counts())

def valori_mancanti(df):
    print("\nValori mancanti per colonna:")
    print(df.isnull())

def pulisci_dati(df):
    # Gestire i valori mancanti
    df = df.dropna()  # Rimuove le righe con valori mancanti
    return df

def correggi_anomalie(df):
    # Correggere anomalie nei dati(valori negativi e 0)
    df = df[df['Età'] >= 0]
    df = df[df['Tariffa_Mensile'] > 0]
    return df





#test
file_path = 'Lezione 18 luglio/clienti.csv'
df = carica_dati(file_path)
print(df)
#df = pulisci_dati(df)
#df = correggi_anomalie(df)

