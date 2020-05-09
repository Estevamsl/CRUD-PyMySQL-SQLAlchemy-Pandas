import pymysql.cursors
import pandas as pd
from abc import (ABC)
import sqlalchemy


class __Sql_Connection(ABC):
    @property
    def __CNN__(self):
        try:
            engine = sqlalchemy.create_engine(
                'mysql+pymysql://root:@localhost:3306/python')
            return engine
        except:
            print('Não foi possível se conectar ao BD')


class CONNECTION(__Sql_Connection):
    pass


class __Connection__:
    @property
    def __cnn__(self):
        try:
            db = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='python',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor

            )
            return db  # Irá retornar a conexão do BD

        except:
            print("Não foi possívele estabelecer a conexão")
        # else:
        #     print('Conexão realizada com sucesso')
