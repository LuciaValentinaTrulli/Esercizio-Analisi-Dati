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

2)Pulizia dei Dati:
Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).

3)Analisi Esplorativa dei Dati (EDA):
Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.

4)Preparazione dei Dati per la Modellazione:
Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.
"""
import pandas as pd

#1)Caricamento e Esplorazione Iniziale

def carica_dati(file_path):
    df = pd.read_csv(file_path)
    print(df)
    return df

def info(df):
    print("\nInfo sul dataset:")
    print(df.info())

def descrizione(df):
    print("\nDescrizione:")
    print(df.describe())

def distribuzione(df):
    print("\nDistribuzione dei valori:")
    print(df.value_counts())

def valori_mancanti(df):
    print("\nValori mancanti:")
    print(df.isnull())


#2)Pulizia dei Dati:

def elimina_mancanti(df): # Rimuove le righe con valori mancanti
    df = df.dropna() 
    print(df)
    return df

def correggi_anomalie(df): #trasformare tipo dato
    # Correggere anomalie nei dati(valori negativi e 0)
    df = df[df['Età'] >= 0]
    df = df[df['Tariffa_Mensile'] > 0]
    print(df)
    return df

#3)Analisi Esplorativa dei Dati (EDA)

#Costo_per_GB (tariffa mensile divisa per i dati consumati)
def aggiungo_colonna(df):
    df['Costo_per_GB'] = df['Tariffa_Mensile']/df['Dati_Consumati']
    print(df)
    return df

#Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abbonamento , Tariffa_Mensile e la Churn
def raggruppare_per_età(df):
    print("\nClienti per età")
    print(df.groupby('Età')['ID_Cliente'].count())

def raggruppare_per_durata_abbonamento(df):
    print("\nClienti per durata abbonamento")
    print(df.groupby('Durata_Abbonamento')['ID_Cliente'].count())

def raggruppare_per_tariffa_mensile(df):
    print("\nClienti per tariffa mensile")
    print(df.groupby('Tariffa_Mensile')['ID_Cliente'].count())

def raggruppare_per_Churn(df):
    print("\nClienti per Churn")
    print(df.groupby('Churn')['ID_Cliente'].count())

# Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili
def correlazione(df):
    # Convertire 'Churn' in formato numerico
    df['Churn'] = df['Churn'].apply(lambda x: 1 if x == 'Sì' else 0)

    # Calcolare la matrice di correlazione
    correlation_matrix = df.corr()

    print("\nMatrice di correlazione:")
    print(correlation_matrix)







#test
file_path = 'Lezione 18 luglio/clienti.csv'
df = carica_dati(file_path)
#info(df)
#descrizione(df)
#distribuzione(df)
#valori_mancanti(df)

#elimina_mancanti(df)
#correggi_anomalie(df)
aggiungo_colonna(df) 
#raggruppare_per_età(df)
correlazione(df)

