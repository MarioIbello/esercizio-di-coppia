import pandas as pd
import matplotlib.pyplot as plt
import os

#class
class StarDataPlotter:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
    #controllo dati
    def load_data(self):
        """Carica i dati dal file e verifica che le colonne richieste esistano."""
        if not os.path.exists(self.filename):
            print(f"Errore: Il file '{self.filename}' non è stato trovato.")
            return False

        try:
            self.data = pd.read_csv(self.filename, delim_whitespace=True, comment='#', header=None, 
                                    names=["MsuH", "m_ini", "logL", "logTe", "M_ass", "b_ass", "y_ass", 
                                           "m_app", "b_y", "dist", "abs_dist", "ID_parent", "age_parent"])
            print("File caricato con successo!")

            if self.data.empty:
                print("Errore: Il DataFrame è vuoto. Controlla il file.")
                return False

            #verifica delle colonne
            required_columns = {'M_ass', 'b_y', 'age_parent'}
            if not required_columns.issubset(self.data.columns):
                print("Errore: Il file non contiene le colonne 'M_ass', 'b_y' o 'age_parent'.")
                print("Colonne disponibili:", self.data.columns)
                return False

            print("Prime righe del DataFrame:")
            print(self.data.head())
            return True

        except Exception as e:
            print(f"Errore durante il caricamento del file: {e}")
            return False

    def plot_color_magnitude_by_age_bins(self, num_bins=7):
        """Crea un grafico colore-magnitudine con bin di età."""
        if self.data is None:
            print("Errore: Dati non caricati. Assicurati di chiamare il metodo load_data() prima di fare il plot.")
            return

        #bin di età
        self.data['age_bin'] = pd.cut(self.data['age_parent'], bins=num_bins)
        age_bins = self.data['age_bin'].unique()

        #grafico
        plt.figure(figsize=(10, 6))

        for age_bin in age_bins:
            subset = self.data[self.data['age_bin'] == age_bin]
            plt.scatter(subset['b_y'], subset['M_ass'], label=f'Età: {age_bin}', alpha=0.7)

        #etichette
        plt.title('Magnitudine Assoluta (M_ass) vs Colore (b-y) per diversi Bins di Età')
        plt.xlabel('Colore (b-y)')
        plt.ylabel('Magnitudine Assoluta (M_ass)')
        plt.gca().invert_yaxis()  #inverte l'asse y
        plt.legend(title='Bins di Età')
        plt.grid(True)
        plt.show()

plotter = StarDataPlotter("Nemo_6670.dat")

if plotter.load_data():
    plotter.plot_color_magnitude_by_age_bins(num_bins=7)