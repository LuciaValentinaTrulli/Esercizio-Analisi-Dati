import Metodi as m

def main():
    df = None
    while True:
        print("\nMenu:")
        print("1) Caricamento e Esplorazione Iniziale")
        print("2) Pulizia dei Dati")
        print("3) Analisi Esplorativa dei Dati (EDA)")
        print("4) Preparazione dei Dati per la Modellazione")
        print("0) Esci")
        choice = input("Scegli un'opzione: ")

        if choice == '1':
            while True:
                print("\n1) Caricamento e Esplorazione Iniziale")
                print("1.1) Carica Dati")
                print("1.2) Info sul Dataset")
                print("1.3) Descrizione del Dataset")
                print("1.4) Distribuzione dei Valori")
                print("1.5) Valori Mancanti")
                print("0) Torna al Menu Principale")
                sub_choice = input("Scegli un'opzione: ")

                if sub_choice == '1.1':
                    file_path = 'Lezione 18 luglio/clienti.csv'
                    df = m.carica_dati(file_path)
                elif sub_choice == '1.2' and df is not None:
                    m.info(df)
                elif sub_choice == '1.3' and df is not None:
                    m.descrizione(df)
                elif sub_choice == '1.4' and df is not None:
                    m.distribuzione(df)
                elif sub_choice == '1.5' and df is not None:
                    m.valori_mancanti(df)
                elif sub_choice == '0':
                    break
                else:
                    print("Opzione non valida o dataset non caricato. Riprova.")

        elif choice == '2':
            while True:
                print("\n2) Pulizia dei Dati")
                print("2.1) Elimina Mancanti")
                print("2.2) Correggi Anomalie")
                print("0) Torna al Menu Principale")
                sub_choice = input("Scegli un'opzione: ")

                if sub_choice == '2.1' and df is not None:
                    df = m.elimina_mancanti(df)
                elif sub_choice == '2.2' and df is not None:
                    df = m.correggi_anomalie(df)
                elif sub_choice == '0':
                    break
                else:
                    print("Opzione non valida o dataset non caricato. Riprova.")

        elif choice == '3':
            while True:
                print("\n3) Analisi Esplorativa dei Dati (EDA)")
                print("3.1) Aggiungi Colonna Costo_per_GB")
                print("3.2) Raggruppa per Età")
                print("3.3) Raggruppa per Durata Abbonamento")
                print("3.4) Raggruppa per Tariffa Mensile")
                print("3.5) Raggruppa per Churn")
                print("3.6) Correlazione")
                print("0) Torna al Menu Principale")
                sub_choice = input("Scegli un'opzione: ")

                if sub_choice == '3.1' and df is not None:
                    df = m.aggiungo_colonna(df)
                elif sub_choice == '3.2' and df is not None:
                    m.raggruppare_per_età(df)
                elif sub_choice == '3.3' and df is not None:
                    m.raggruppare_per_durata_abbonamento(df)
                elif sub_choice == '3.4' and df is not None:
                    m.raggruppare_per_tariffa_mensile(df)
                elif sub_choice == '3.5' and df is not None:
                    m.raggruppare_per_Churn(df)
                elif sub_choice == '3.6' and df is not None:
                    m.correlazione(df)
                elif sub_choice == '0':
                    break
                else:
                    print("Opzione non valida o dataset non caricato. Riprova.")

        elif choice == '4':
            while True:
                print("\n4) Preparazione dei Dati per la Modellazione")
                print("4.1) Converti Churn in Formato Numerico")
                print("4.2) Normalizzazione")
                print("0) Torna al Menu Principale")
                sub_choice = input("Scegli un'opzione: ")

                if sub_choice == '4.1' and df is not None:
                    df = m.converti_Churn(df)
                elif sub_choice == '4.2' and df is not None:
                    try:
                        m.normalizzazione(df)
                    except:
                        print("Eseguire prima pulizia dati e creazione colonna Costo per GB")
                elif sub_choice == '0':
                    break
                else:
                    print("Opzione non valida o dataset non caricato. Riprova.")

        elif choice == '0':
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")


main()