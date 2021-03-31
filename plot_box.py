import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def box_price_one_id(csv, identificador, producto):
    df = pd.read_csv(csv)
    df_id = df.loc[df['id'] == identificador]
    sns.set_theme(style="whitegrid")
    g = sns.catplot(data=df_id, kind='box', x="Dia_Semana", y=producto)
    sns.stripplot(x='Dia_Semana', y=producto, data=df_id, alpha=0.3,jitter=False,color='k')
    g.despine(left=True)
    g.set_axis_labels("Weekday", producto + " Price Euro/litre")
    plt.xticks(rotation=90)
    plt.title("Estadísticas de " + producto + " por día de la semana")


def box_price_all_id(csv, producto):
    df = pd.read_csv(csv)
    sns.set_theme(style="whitegrid")
    g = sns.catplot(data=df, kind='box', x="Dia_Semana", y=producto)
    sns.stripplot(x='Dia_Semana', y=producto, data=df, alpha=0.3,jitter=False,color='k')
    g.despine(left=True)
    g.set_axis_labels("Weekday", producto + " Price Euro/litre")
    plt.xticks(rotation=90)
    plt.title("Estadísticas de " + producto + " por día de la semana")