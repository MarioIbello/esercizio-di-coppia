import pandas as pd
import matplotlib.pyplot as plt
import os


#classe
class StarDataPlotter:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
#caricamento file e controllo dati
    def load_data(self):
        """Carica i dati dal file .dat e li memorizza in un DataFrame di Pandas."""
        if not os.path.exists(self.filename):
            print(f"Errore: il file '{self.filename}' non esiste nella directory corrente.")
            return False

        try:
            self.data = pd.read_csv(self.filename, delim_whitespace=True, comment='#', 
                                    names=["MsuH", "m_ini", "logL", "logTe", "M_ass", "b_ass", "y_ass", "m_app", 
                                           "b-y", "dist", "abs_dist", "ID_parent", "age_parent"])
            print("Dati caricati con successo.")
            return True
        except Exception as e:
            print(f"Errore durante il caricamento dei dati: {e}")
            return False

    def plot_color_magnitude(self):
        """Realizza un grafico colore-magnitudine, colorato in base all'età delle stelle."""
        if self.data is None:
            print("Errore: Dati non caricati. Assicurati di chiamare il metodo load_data() prima di fare il plot.")
            return

        #estrazione dati
        color = self.data["b-y"]
        magnitude = self.data["m_app"]
        age = self.data["age_parent"]

        #grafico
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(color, magnitude, c=age, cmap='viridis', s=10, alpha=0.7)
        plt.colorbar(scatter, label="Età delle stelle (Myr)")
        plt.xlabel("Colore (b-y)")
        plt.ylabel("Magnitudine apparente (m_app)")
        plt.gca().invert_yaxis()  #inverti asse
        plt.title("Grafico Colore-Magnitudine colorato in base all'età delle stelle")
        plt.show()



plotter = StarDataPlotter("Nemo_6670.dat")

if plotter.load_data():
    plotter.plot_color_magnitude()