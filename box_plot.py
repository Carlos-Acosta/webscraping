import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

prices = pd.read_csv("bonarea_gasolineras.csv")
sns.set_theme(style="whitegrid")

def box_price(producto):
    g = sns.catplot(data=prices, kind='box', x="Dia_Semana", y=producto)
    sns.stripplot(x='Dia_Semana', y=producto, data=prices, alpha=0.3,jitter=False,color='k')
    g.despine(left=True)
    g.set_axis_labels("Weekday", producto + " Price Euro/litre")
    plt.title("Estadísticas de " + producto + " por día de la semana")


box_price("GASOLINA S/P 95")