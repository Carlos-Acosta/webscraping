import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def evolucion_precio_gasolinera(csv, identificador, producto):
    df = pd.read_csv(csv)
    df_id = df.loc[df['id'] == identificador]

    if df_id[producto].sum(axis = 0, skipna = True) == 0:
        print("There is no data for " + producto + " at " + identificador)
    else:
        sns.lineplot(x = "Fecha", y = producto, data=df_id)
        plt.title("Gasolinera " + identificador + ": Evolución temporal precio")
        plt.xticks(rotation=90)
        plt.show()
        
