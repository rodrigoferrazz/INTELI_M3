import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
# colocando data como índice e transformando para datetime
df.set_index('date', inplace=True)
df.index = pd.to_datetime(df.index)

# Clean data
# filtrando os percentuais
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    # defini arbitrariamente os figsizes com base na imagem de referência
    fig = plt.figure(figsize=(17, 6))
    # plotando o line plot vermelho
    plt.plot(df.index, df['value'], color='red')
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    fig.savefig('line_plot.png')

    # Save image and return fig (don't change this part)
    fig.savefig('imgs/line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # agrupando os valores por ano e mês e tirando a média
    df_bar = df.groupby([df.index.year, df.index.month])['value'].mean()

    # Draw bar plot
    # definindo lista de anos e meses
    years = [2016, 2017, 2018, 2019]
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    # em x, fica definido um array do numpy = [0, 1, 2, 3]
    x = np.arange(len(years))
    # tamanho definido tambem arbitrariamente para se parecer com o da foto original. dividi por 12 para todos os meses ocuparem o mesmo espaço final
    width = 0.4 / 12
    
    # plotando o gráfico
    fig, ax = plt.subplots(figsize=(10,8))
    
    # esse for coloca em month_values os valores correspondentes para cada ano e mês
    for i, m in enumerate(months):
        month_values = []
        for year in years:
            try:
                month_values.append(df_bar.loc[(year, m)])
                # esse except é necessário pois 2016 começa do mês 5 no df
            except KeyError:
                month_values.append(0)
                # calculando o formato das barras
                # aqui utilizei o módulo calendar para colocar o nome dos meses em inglês
        ax.bar(x + i*width, month_values, width=width, label=calendar.month_name[m])
    

    xticks_pos = x + width*(len(months)-1)/2
    ax.set_xticks(xticks_pos)
    # deixa os anos na vertical no eixo x
    ax.set_xticklabels([str(y) for y in years], rotation=90)
    
    # labels
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    ax.legend(title="Months", loc="upper left", bbox_to_anchor=(0, 1))

    # Save image and return fig (don't change this part)
    fig.savefig('imgs/bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    # definindo a ordem correta dos meses (sem isso, o gráfico começa de maio)
    month_order = [calendar.month_abbr[i] for i in range(1, 13)]
    # plotando os dois gráficos em uma figura só
    fig, axes = plt.subplots(1, 2, figsize=(25, 10))

    # a paleta deep é a que mais se assemelhava à figura de referência
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0], palette='deep')
    axes[0].set_title('Year-wise Box Plot (Trend)', fontsize=16)
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=month_order, palette='deep')
    axes[1].set_title('Month-wise Box Plot (Seasonality)', fontsize=16)
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('imgs/box_plot.png')
    return fig