import pymysql.cursors
import pandas as pd
from abc import (ABC)
import sqlalchemy


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
