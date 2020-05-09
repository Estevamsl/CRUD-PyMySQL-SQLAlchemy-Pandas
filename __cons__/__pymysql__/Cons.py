import pymysql.cursors
import pandas as pd
from abc import (ABC)
import sqlalchemy
# do (from) Módulo __con__.__sqlalchemy__.connectionBD traz ((importa)(import)) CONNECTION
# from __con__.__sqlalchemy__.connectionBD import CONNECTION
from __con__.__pymysql__.PymysqlBD import __Connection__


class __Consult__(ABC):
    @property
    def __cnst__(self):
        try:
            with __Connection__().__cnn__.cursor() as cursor:  # Irá realizar uma associação
                cursor.execute('SELECT * FROM MERCADO')
                __r__ = cursor.fetchall()
            print('\n')
            for r in __r__:
                print(r)
            print('\n')
        except:
            print("Não foi possível realizar a consulta no BD")
