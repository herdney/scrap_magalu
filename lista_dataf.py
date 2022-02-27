import pandas as pd


def criar_dataframe(lst1, lst2):
    df = pd.DataFrame(list(zip(lst1,lst2)), columns = ['Produto','Preço'])
    return df
