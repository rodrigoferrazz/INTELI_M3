import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Denfinir dataframe
df = pd.read_csv("medical_examination.csv")

# Função que define o sobrepeso
df["overweight"] = (df["weight"] / (df["height"] / 100) ** 2 > 25).astype(int)

# Função que define o sobrepeso
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)

# Função Catplot
def draw_cat_plot():

    # pd.melt() define as colunas abaixo como variáveis de identificação e torna em formato longo o df
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    # Agrupar os dados, .size faz a contagem de quantos dados tem em cada grupo, cria uma coluna 'total' com a contagem de cada grupo
    df_cat = df_cat.groupby(["cardio", "variable", "value"]) \
                   .size().reset_index(name="total")

    # Criar gráfico 
    fig = sns.catplot(
        data=df_cat,
        x="variable", y="total", hue="value",
        col="cardio", kind="bar"
    ).fig

    fig.savefig("imgs/catplot.png")
    return fig

# Função Heatmap
def draw_heat_map():
    # Limpeza dos dados
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Matriz de correlação que será usada para o heatmap
    corr = df_heat.corr()

    # Máscara para o triângulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Configuração da figura
    fig, ax = plt.subplots(figsize=(12, 12))

    # Heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        cbar_kws={"shrink": 0.5}
    )

    fig.savefig("imgs/heatmap.png")
    return fig
