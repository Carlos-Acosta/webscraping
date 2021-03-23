import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def evolucion_precio_gasolinera(csv, identificador, producto):
    df = pd.read_csv(csv)
    df_id = df.loc[df['id'] == identificador]
    sns.lineplot(x = "Fecha", y = producto, data=df_id)
    plt.title("Gasolinera " + identificador + ": Evolución temporal precio")
    plt.xticks(rotation=90)
    plt.show()

evolucion_precio_gasolinera("bonarea_gasolineras.csv", "G058", "ADBLUE")
