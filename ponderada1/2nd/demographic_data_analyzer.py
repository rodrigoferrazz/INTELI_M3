import pandas as pd
from unittest import main


def calculate_demographic_data(print_data=True):
    # Ler o dataset
    df = pd.read_csv("adult.data.csv")

    # 1. Quantidade de pessoas por raça
    race_count = df['race'].value_counts()

    # 2. Média de idade dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentual de pessoas com diploma de Bachelors
    percentage_bachelors = round((df['education'].value_counts(normalize=True)['Bachelors'] * 100), 1)

    # 4. Pessoas com ensino avançado (Bachelors, Masters, Doctorate)
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # % com salário > 50K
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # 5. Mínimo de horas trabalhadas por semana
    min_work_hours = df['hours-per-week'].min()

    # % dos que trabalham mín. horas e ganham >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 6. País com maior % de pessoas com >50K
    country_earnings = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()['>50K'] * 100
    highest_earning_country = country_earnings.idxmax()
    highest_earning_country_percentage = round(country_earnings.max(), 1)

    # 7. Ocupação mais popular para >50K na Índia
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Número de pessoas de cada raça:\n", race_count) 
        print("Idade média dos homens:", average_age_men)
        print(f"Porcentagem com diploma de Bacharelado: {percentage_bachelors}%")
        print(f"Porcentagem com educação avançada que ganham >50K: {higher_education_rich}%")
        print(f"Porcentagem sem educação avançada que ganham >50K: {lower_education_rich}%")
        print("Mínimo de horas de trabalho por semana:", min_work_hours, "horas/semana")
        print(f"Porcentagem de ricos entre os que trabalham o mínimo de horas: {rich_percentage}%")
        print("País com maior porcentagem de pessoas ricas:", highest_earning_country)
        print("Maior porcentagem de pessoas ricas em um país:", highest_earning_country_percentage)
        print("Ocupação mais comum na Índia entre os que ganham > 50K:", top_IN_occupation)

    # ⚠️ return sempre deve ser executado
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


if __name__ == "__main__":
    calculate_demographic_data()
    main(module='test', exit=False)
