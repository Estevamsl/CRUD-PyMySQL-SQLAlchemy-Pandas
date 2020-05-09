import pymysql.cursors
import pandas as pd
from abc import (ABC)
import sqlalchemy
# do (from) Módulo __con__.__sqlalchemy__.connectionBD traz ((importa)(import)) CONNECTION
from __con__.__sqlalchemy__.connectionBD import CONNECTION


class CONSULT:
    @property
    def __c__(self):
        __cnn__ = CONNECTION().__CNN__  # Associação
        try:
            df = pd.read_sql_table('mercado', __cnn__)
            print(df.head())
        except:
            print('Não foi possível consultar no BD')
