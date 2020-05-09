import pymysql.cursors
import pandas as pd
from abc import (
    ABC
)
import sqlalchemy

from __con__.__sqlalchemy__.connectionBD import CONNECTION
from __con__.__pymysql__.PymysqlBD import __Connection__

from __cons__.__pymysql__.Cons import __Consult__
from __cons__.__sqlalchemy__.__ConsSqlalchemy import CONSULT

from delete.__delete__ import __Delete__


class __Update__(ABC):
    @staticmethod
    def __updat__(coluna: any, coluna_desejada: any, __id__: int) -> any:
        try:
            with __Connection__().__cnn__.cursor() as cursor:
                try:
                    cursor.execute(
                        'UPDATE mercado SET %s = %s WHERE id = %s', (coluna, coluna_desejada, __id__))
                    __Connection__().__cnn__.commit()
                except:
                    print("Houve um erro inesperado")
        except:
            print("Não foi possível realizar a atualização de dados do BD")
        else:
            print("Atualização realizada com sucesso")
