import pandas as pd
import seaborn as sns

prices = pd.read_csv("bonarea_gasolineras.csv")
sns.set_theme(style="whitegrid")

def box_95():
    g = sns.catplot(data=prices, kind='box', x="Dia_Semana", y="GASOLINA S/P 95")
    sns.stripplot(x='Dia_Semana', y='GASOLINA S/P 95', data=prices, alpha=0.3,jitter=False,color='k')
    g.despine(left=True)
    g.set_axis_labels("Weekday", "GASOLINA S/P 95 Price Euro/litre")


def box_98():
    g = sns.catplot(data=prices, kind='box', x="Dia_Semana", y="GASOLINA S/P 98")
    sns.stripplot(x='Dia_Semana', y='GASOLINA S/P 98', data=prices, alpha=0.3,jitter=False,color='k')
    g.despine(left=True)
    g.set_axis_labels("Weekday", "GASOLINA S/P 98 Price Euro/litre")

def box_A():
    g = sns.catplot(data=prices, kind='box', x="Dia_Semana", y="GASOIL A")
    sns.stripplot(x='Dia_Semana', y='GASOIL A', data=prices, alpha=0.3,jitter=False,color='k')
    g.despine(left=True)
    g.set_axis_labels("Weekday", "GASOIL A Price Euro/litre")

def box_Blue():
    g = sns.catplot(data=prices, kind='box', x="Dia_Semana", y="ADBLUE")
    sns.stripplot(x='Dia_Semana', y='ADBLUE', data=prices, alpha=0.3,jitter=False,color='k')
    g.despine(left=True)
    g.set_axis_labels("Weekday", "ADBLUE Price Euro/litre")


box_95()