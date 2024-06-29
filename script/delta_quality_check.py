import numpy as np
import pandas as pd

# put your list path with excel results
list_path = [
    r'source\2024-06-20.csv'
    r'source\2024-06-21.csv'
    r'source\2024-06-22.csv'
]


def generate_dataframes(list_path):

    dataframes = []

    for path in list_path:
        df = pd.read_csv(path, delimiter=';')
        dataframes.append(df)

    if not dataframes:
        return pd.DataFrame()

    df_merged = dataframes[0]

    for index, df in enumerate(dataframes[1:]):
        df_merged = pd.merge(df_merged, df, how='outer',
                             on='data', suffixes=('', f'_{index+1}'))

    return df_merged


def compare_results(df_merged):

    comparison_results = np.all([
        df_merged[df_merged.columns.tolist()[1]] == df_merged[col]
        for col in df_merged.columns[1:]
    ], axis=0)

    additional_condition = np.any([
        (df_merged[df_merged.columns.tolist()
         [1]].isna() & df_merged[col].notna())
        for col in df_merged.columns[1:]
    ], axis=0)

    reference_date = df_merged['data'].min()
    date_condition = df_merged['data'] > reference_date

    df_merged['Resultado'] = np.where(
        date_condition & (comparison_results | additional_condition),
        'Verdadeiro',
        'Falso'
    )

    if any(df_merged['Resultado'] == 'Falso'):
        print('Os dados fornecidos indicam que não é recomendável proceder com o delta.\n')

    print(df_merged[df_merged['Resultado'] == 'Falso'][['data', 'Resultado']])

    return df_merged.sort_values(by=['data'], ascending=True)


compare_results(generate_dataframes(list_path)).head(5)
