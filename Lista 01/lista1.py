"""Lista 01"""

from itertools import combinations
import pandas as pd


def get_all_combinations(n):
    """Return all possible combinations of n numbers"""
    combinations_list = [()]
    for i in range(1, n+1):
        combinations_i = list(combinations(range(1, n+1), i))
        combinations_list.extend(combinations_i)
    return combinations_list

def ex03():
    """Exercise 03: Lalonde dataset"""
    column_names = ['treated', 'age', 'education', 'black', 'hispanic',
                     'married', 'nodegree', 'RE74', 'RE75', 'RE78']
    df_treated = pd.read_csv('nswre74_treated.txt',
                             names=column_names,
                             sep=r"\s+|;|:",
                             engine='python')
    df_control = pd.read_csv('nswre74_control.txt',
                             names=column_names,
                             sep=r"\s+|;|:",
                             engine='python')
    df = pd.concat ([df_treated, df_control])

    df['u74'] = (df['RE74'] == 0).astype(int)
    df['u75'] = (df['RE75'] == 0).astype(int)

    new_column_names = ['treated', 'age', 'education', 'black', 'hispanic',
                        'married', 'nodegree', 'RE74', 'RE75', 'u74', 'u75', 'RE78']
    df = df.reindex(columns=new_column_names)

if __name__ == "__main__":
    ex03()
