import pandas as pd

class cambios:

    def __init__(self):
        df=pd.read_csv('USA_Housing.csv')
        self.df=df

    