import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Ler dados
    df = pd.read_csv("epa-sea-level.csv")

    # Criar gráfico de dispersão
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Linha de melhor ajuste (1880 até o final)
    slope, intercept, r, p, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years = pd.Series(range(1880, 2051))
    best_fit = slope * years + intercept
    plt.plot(years, best_fit)

    # Linha de melhor ajuste (2000 até o final)
    df_novo = df[df["Year"] >= 2000]
    slope_novo, intercept_novo, r_novo, p_novo, std_err_novo = linregress(df_novo["Year"], df_novo["CSIRO Adjusted Sea Level"])
    years_novo = pd.Series(range(2000, 2051))
    best_fit_novo = slope_novo * years_novo + intercept_novo
    plt.plot(years_novo, best_fit_novo, "green")

    # Labels e título exatamente como o teste espera
    plt.plot(years_novo, best_fit_novo, "green")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Ajustar ticks do eixo X
    plt.xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])

    # Salvar e retornar
    plt.savefig("sea_level_plot.png")
    return plt.gca()
